````json
[
    {
        "from": "system",
        "value": "You are an expert in explaining and detecting hate speech messages."
    },
    {
        "from": "human",
        "value": """You must explain why a social media message is hate or not and then tell me your decision. You must always reply with only a JSON containing one field 'hate_speech' including a Boolean value ("True" for hate speech messages, "False" for neutral ones); and a field 'explanations' containing a list with the each message phrase and its corresponding explanation. Do not include text outside the JSON.
        This is the definition of hate speech: "language characterized by offensive, derogatory, humiliating, or insulting discourse that promotes violence, discrimination, or hostility towards individuals or groups based on attributes such as race, religion, ethnicity, or gender".
        The input format is:
            Generate step-by-step explanation for:\n<Message>{{input query}}</Message>.
        The output format is:
            {
                "hate_speech": "{{Boolean}}",
                "explanations": [
                    {
                        "input": "{{input query phrase 1}}",
                        "explanation": "{{input query 1 phrase step-by-step explanation}}"
                    },
                    {
                        "input": "{{input query phrase 2}}",
                        "explanation": "{{input query 2 phrase step-by-step explanation}}"
                    }
                ]
            }
        Stick to the output format and generate the JSON for:\n<Message>these hoes like niggas that spend money not talk bout it</Message>"""
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "these hoes like niggas that spend money not talk bout it",
                    "explanation: "The phrase is NOT considered hate speech because it doesn't contain a hateful intention, even though the language used is derogatory. In certain contexts, there might be a discussion about societal trends related to spending habits. This phrase critiques materialistic attitudes and is not intended as hate speech."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>hes a beaner smh you can tell hes a mexican</Message>
        """

    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "True",
            "explanations": [
                {
                    "input": "hes a beaner smh you can tell hes a mexican",
                    "explanation": "The phrase is considered hate speech because it contains derogatory language promoting negative stereotypes about Mexican people."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>Stay beautiful you bitch</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "Stay beautiful you bitch",
                    "explanation": "The phrase is NOT considered hate speech because, even though it contains the derogatory term 'bitch' is preceded by a positive message 'stay beautiful' so this must be a message in a close relationship or friendship, and both parties understand and consent the tone and intention."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>!!!!!!!!! RT @C_G_Anderson: @viva_based she look like a tranny</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "she look like a tranny",
                    "explanation": "The tweet is NOT considered hate speech because it doesn't contain any direct threat, harassment or discrimination based on race, ethnicity, national origin, religion, gender, gender identity, disability, or sexual orientation. The term 'tranny' can be considered offensive, but in this context, it doesn't seem to be used with the intent to harm or discriminate against transgender people. It could be a casual, offensive remark, but it doesn't rise to the level of hate speech."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>RT @ShenikaRoberts: The shit you hear about me might be true or it might be faker than the bitch who told it to ya &#57361;</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "The shit you hear about me might be true or it might be faker than the bitch who told it to ya",
                    "explanation": "The intention behind this phrase is to express that the person doesn't care whether the rumors about them are true or not, and that the person who spread the rumors is more dishonest. The phrase uses strong language with the term 'bitch' which is derogatory towards women. The context of this phrase is a social media post, which could be interpreted as a defensive response to rumors or gossip about the person. The phrase is NOT considered hate speech, because it's not directed towards a specific individual or group, and it's not promoting violence or hatred. However, it does contain offensive language which might be inappropriate for some audiences."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>@T_Madison_x: The shit just blows me..claim you so faithful and down for somebody but still fucking with hoes! &#128514;&#128514;&#128514;</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "The shit just blows me..claim you so faithful and down for somebody but still fucking with hoes!",
                    "explanation": "The phrase is NOT considered hate speech because it's an expression of frustration or disappointment about someone's behavior. It's not intended to promote hate or harm towards a specific group."
                },
                {
                    "input": "&#128514;&#128514;&#128514;",
                    "explanation": "The emoji sequence is NOT considered hate speech because it's just a series of emojis that doesn't form a clear message or expression. It could be interpreted as a random or nonsense input."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>@__BrighterDays: I can not just sit up and HATE on another bitch .. I got too much shit going on!</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "I can not just sit up and HATE on another bitch ..",
                    "explanation": "The phrase is NOT considered hate speech because it does not promote or encourage hatred towards another person. The use of the word 'bitch' in this context could be seen as informal or colloquial language, rather than a derogatory term."
                },
                {
                    "input": "I got too much shit going on!",
                    "explanation": "The speaker is expressing that they have more important things to focus on in their life than to hate on someone else."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>&#8220; cause I'm tired of you big bitches coming for us skinny girls!!&#8221;</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "cause I'm tired of you big bitches coming for us skinny girls!!",
                    "explanation": "This phrase was likely used in a social media context, possibly in response to a post or comment about skinny girls. The term 'bitches' is used in a non-derogatory way to address a group of people, and the phrase does not promote violence or discrimination against any specific group. The user is expressing their annoyance at what they perceive as attacks on skinny girls by 'big bitches', not promoting hate."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>& you might not get ya bitch back & thats that</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "& you might not get ya bitch back & thats that",
                    "explanation": "The phrase is NOT considered hate speech because it doesn't contain any explicit hate or discrimination. It could be a part of a conversation or a song that's not meant to be taken literally. It could be a way of saying that someone needs to take action or they might lose something valuable. It's important to consider the context in which it was used."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>Keeks is a bitch she curves everyone lol I walked into a conversation like this. Smh</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "False",
            "explanations": [
                {
                    "input": "Keeks is a bitch she curves everyone",
                    "explanation": "The phrase 'Keeks is a bitch she curves everyone' is NOT considered hate speech because it's a statement about someone's behavior and not a direct attack on a specific group or person based on their race, ethnicity, gender, religion, sexual orientation, disability, or other protected characteristic. It's important to remember that the term 'bitch' can be considered derogatory, but in this context, it seems to be used more in the sense of someone being difficult or manipulative, rather than as a slur against women."
                },
                {
                    "input": "I walked into a conversation like this. Smh",
                    "explanation": "The phrase 'I walked into a conversation like this. Smh' is NOT considered hate speech because it's a statement expressing frustration or annoyance about overhearing a conversation, and it doesn't promote or attack any protected characteristic."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>'Our people'. Now is the time for the Aryan race 2 stand up and say 'no more'. Before the mongerls turn the world into a ghetto slum.</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "True",
            "explanations": [
                {
                    "input": "'Our people'",
                    "explanation": "'Our people' suggests a sense of exclusive ownership or superiority based on race, promoting division and exclusion."
                },
                {
                    "input": "Now is the time for the Aryan race 2 stand up and say 'no more'",
                    "explanation": "'Aryan race' evokes white supremacist ideology, advocating racial superiority and justifying discrimination against other races."
                },
                {
                    "input": "Before the mongerls turn the world into a ghetto slum.",
                    "explanation": "'Mongrels' dehumanizes and denigrates other racial or ethnic groups, promoting hatred and contempt. 'Ghetto slum' incites fear and xenophobia, portraying certain communities in a derogatory and prejudiced manner. Overall, the phrase promotes racial supremacy, dehumanizes marginalized groups, incites fear and hatred, and fosters division based on race."
                }
            ]
        }"""
    },
    {
        "from": "human",
        "value": """
            The output format is:
                {
                    "hate_speech": "{{Boolean}}",
                    "explanations": [
                        {
                            "input": "{{input query phrase 1}}",
                            "explanation": "{{input query 1 phrase step-by-step explanation}}"
                        },
                        {
                            "input": "{{input query phrase 2}}",
                            "explanation": "{{input query 2 phrase step-by-step explanation}}"
                        }
                    ]
                }
            Stick to the output format and generate the JSON for:\n<Message>Are you... asian? black? Hawaiian? gay? retarded? drunk?</Message>
        """
    },
    {
        "from": "gpt",
        "value": """{
            "hate_speech": "True",
            "explanations": [
                {
                    "input": "Are you... asian? black? Hawaiian? gay? retarded? drunk?",
                    "explanation": "The phrase is hate speech because it uses derogatory language in a questioning or derogatory manner, targeting marginalized groups: 'Asian', 'Black', 'Hawaiian' discriminates based on race or ethnicity. 'Gay' is used derogatorily, displaying homophobia. 'Retarded' term is offensive and ableist, targeting individuals with disabilities. 'Drunk' implies negative assumptions about behavior."
                }
            ]
        }"""
    }
]

````