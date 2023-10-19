# t2c

Time to chat

Inspiration: https://medium.com/@sohaibshaheen/train-chatgpt-with-custom-data-and-create-your-own-chat-bot-using-macos-fb78c2f9646d

# prerequisites

Assuming MacOS.

Python3 with latest pip.

Prefer `brew` for installation tasks.

# prep

Install OpenAI library, GPT index and other required modules. Additional modules also depend on kind of content that will be used.

Recently (April/May 2023) GPT index was replaced by LlamaIndex. Code is adjusted for that. Use `import GPTVectorStoreIndex` instead of `import GPTSimpleVectorIndex` with the correct (changed) properties. LlamaIndex allows the LLM to connect to the external data that is our knowledge base.

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

Feel free to use your own, any other data. Note that there is data exchange with OpenAI so don't use sensitive data.

Add files to folder `docs` (as this is ignored so data won't end up in the frepo, or point to any other folder).

Can create a file with overview of contents uses with command `tree docs > tree_docs.txt`. Install with `brew install tree` if not available.



# run

Must provide an additional argument, when `true` content will be (re)indexed, then start UI. Any other value will start UI assuming index is already available. No further proper checks done yet.

`python3 app.py true "docs"`

Or `gradio app.py <arg>` to launch in automatic reload mode.

Go to http://127.0.0.1:7860/ or the online Gradio url.

# prompts

## voor de calamiteiten set

Wat is het wettelijk kader bij bestrijding van crises?

Wat moet het Waterschap doen als de Roer te hoog komt te staan?

Wat moet het Waterschap doen om bij hoogwater in de Roer het peil met minstens 40 cm te verlagen?

Wat zijn de specifieke risico's op schade door hoogwater in de binnendijkse gebieden van de Hollandse IJssel stroomopwaarts van Krimpen aan de IJssel?

Wat zijn de specifieke risico's op schade door hoogwater in de binnendijkse gebieden van de Maas stroomopwaarts van Gennep?

Wat zijn de specifieke risico's op schade door hoogwater in de binnendijkse gebieden van de Maas stroomafwaarts van Roermond tot Sambeek?

Op welke manier werken Waterschapsbedrijf Limburg, Waterscha Limburg en WML Limburgs Drinkwater samen in geval van calamiteiten, en wat is hierbij de rol van VRZL?

Geef me van alle instanties die ik kan bellen in geval van calamiteiten de telefoonnummers.

Noem de plaatsen in Limburg waar hockeyvelden onderstromen bij hoogwater van de Maas.



## voor de algemene set

Vertel wat je weet over De Steeg.

Wat is de impact van onttrekkingsverbod op kapitaalintensieve teelten in Noord- en Midden-Limburg.

Geef een overzicht van bestanden die over _onderwerp x_ gaan.

# warnings

Warnings like

```
Multiple definitions in dictionary at byte 0x41ea0 for key /Im7
```

during index process can be ignored.

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

https://github.com/jerryjliu/llama_index/blob/main/docs/how_to/integrations/vector_stores.md Weaviate