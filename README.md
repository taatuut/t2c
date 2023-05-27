# t2c

Time to chat

Inspiration: https://medium.com/@sohaibshaheen/train-chatgpt-with-custom-data-and-create-your-own-chat-bot-using-macos-fb78c2f9646d

# prerequisites

Assuming MacOS.

Python3 with latest pip.

Prefer `brew` for installation tasks.

# prep

Install OpenAI library, GPT index and other required modules. Additional modules also depend on kind of content that will be used.

Recently (May 2023) GPT index was renamed to LlamaIndex. Code is adjusted for that. LlamaIndex allows the LLM to connect to the external data that is our knowledge base.

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

# data

Using some public *Waterschap* documents found online. Sample set can be downloaded from https://www.dropbox.com/s/9b8rv11yg7x9p63/waterschaplimburg.nl.zip?dl=1

Add files to folder `docs` see file `tree_docs.txt` created with following command for sample input used:

`tree docs > tree_docs.txt`

# run

`python3 app.py`

Go to http://127.0.0.1:7860/ or the online Gradio url.

# prompts

Vertel wat je weet over De Steeg.

Wat is de impact van onttrekkingsverbod op kapitaalintensieve teelten in Noord- en Midden-Limburg.

Geef een overzicht van bestanden die over _onderwerp x_ gaan.

# fail :-)

```
openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details.
```

Time for a paid account :-)

# todo

Q1
Is response limited to the custom provided content only?

Q2
What data is exchanged/stored with/at OpenAI?

Q3
Could not find image processor class in the image processor config or the model config. Loading based on pattern matching with the model's feature extractor configuration.

https://discuss.huggingface.co/t/error-finding-processors-image-class-loading-based-on-pattern-matching-with-feature-extractor/31890/9

https://github.com/jerryjliu/llama_index/issues/872

# links

https://gpt-index.readthedocs.io/en/latest/index.html

https://github.com/jerryjliu/llama_index