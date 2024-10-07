You must explain why a social media message is hate or not and then tell me your decision. You must always reply with only a JSON containing one field 'hate_speech' including a Boolean value ("True" for hate speech messages, "False" for neutral ones); and a field 'explanations' containing a list with the each message phrase and its corresponding explanation. Do not include text outside the JSON.

This is the definition of hate speech: "language characterized by offensive, derogatory, humiliating, or insulting discourse that promotes violence, discrimination, or hostility towards individuals or groups based on attributes such as race, religion, ethnicity, or gender".

The input format is:
    
    Generate step-by-step explanation for:<Message><input query></Message>.

The output format is:
````
    {
        "hate_speech": "<Boolean>",
        "explanations": [
            {
                "input": "<input query phrase 1>",
                "explanation": "<input query 1 phrase step-by-step explanation>"
            },
            {
                "input": "<input query phrase 2>",
                "explanation": "<input query 2 phrase step-by-step explanation>"
            }
        ]
    }
````
Generate step-by-step explanation for:`<Message>Your message</Message>`