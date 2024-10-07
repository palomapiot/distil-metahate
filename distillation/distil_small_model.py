import pandas as pd
from datasets import Dataset
from unsloth import FastLanguageModel, is_bfloat16_supported
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer
from transformers import TrainingArguments

# Load model
max_seq_length = 4096
dtype = None
load_in_4bit = True

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/llama-3-8b-Instruct-bnb-4bit",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
    token="hf_token"
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha=32,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=3407,
    use_rslora=False,
    loftq_config=None,
)

# Data preparation
df = pd.read_csv('/data/Llama-3-70B-Rationales.tsv', sep='\t', skiprows=[0], names=['id', 'label', 'text', 'rationales'])
df = df[['text', 'rationales']]


def row_to_list(row):
    return [
        {"from": "human", "value": row["text"]},
        {"from": "gpt", "value": row["rationales"]}
    ]


df["conversations"] = df.apply(row_to_list, axis=1)
df_conversations = df[["conversations"]]
dataset = Dataset.from_pandas(df_conversations)

tokenizer = get_chat_template(
    tokenizer,
    chat_template="llama-3",
    mapping={"role": "from", "content": "value", "user": "human", "assistant": "gpt"}
)


def formatting_prompts_func(examples):
    conversations = examples["conversations"]
    texts = [tokenizer.apply_chat_template(c, tokenize=False, add_generation_prompt=False) for c in conversations]
    return {"text": texts, }


dataset = dataset.map(formatting_prompts_func, batched=True)

# Train the model
trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    dataset_num_proc=2,
    packing=False,
    args=TrainingArguments(
        per_device_train_batch_size=8,
        gradient_accumulation_steps=4,
        warmup_steps=40,
        max_steps=1000,
        learning_rate=2.5e-5,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=10,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="/outputs",
    ),
)
trainer_stats = trainer.train()

# Save model
model.save_pretrained("/models/Llama-3-8B-Distil-MetaHate")
tokenizer.save_pretrained("/models/Llama-3-8B-Distil-MetaHate")
