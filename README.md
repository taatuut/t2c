# t2c
Time to chat

# prerequisites

Assuming MacOS

Python3 with latest pip

Prefer `brew` for installation tasks.

# prep

Source: https://medium.com/@sohaibshaheen/train-chatgpt-with-custom-data-and-create-your-own-chat-bot-using-macos-fb78c2f9646d

Install OpenAI library GPT index and other modules.

GPT index is also called LlamaIndex. It allows the LLM to connect to the external data that is our knowledge base.

```
python3 -m pip install --upgrade pip
python3 -m pip install openai gpt_index PyPDF2 gradio
```

Get OpenAI key
