# t2c
Time to chat

# prerequisites

Assuming MacOS

Python3 with latest pip.

Prefer `brew` for installation tasks.

# prep

Source: https://medium.com/@sohaibshaheen/train-chatgpt-with-custom-data-and-create-your-own-chat-bot-using-macos-fb78c2f9646d

Install OpenAI library, GPT index and other required modules. Additional modules also depend on kind of content that will be used.

GPT index aka LlamaIndex. It allows the LLM to connect to the external data that is our knowledge base.

```
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

To get an overview of modules with version run `python3 -m pip list > pip_list.txt`

The OpenAI library needs to be configured with your account's secret key which is available on the website. See https://github.com/openai/openai-python/tree/main

Either set it as the OPENAI_API_KEY environment variable before using the library:

Create OpenAI key or use existing one, then set a environment variable `OPENAI_API_KEY` to contain the OpenAI key like:

`export OPENAI_API_KEY=someveryseceretkey`

Check with `printenv` or `echo $OPENAI_API_KEY`

Add files to folder `docs` see file `tree_docs.txt` created with command `tree docs > tree_docs.txt` for sample input used.

# run

`python3 app.py`

