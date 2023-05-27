import gradio as gr
import sys

# Set OPENAI_API_KEY environment variable outside this Python script, see README.md

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))
    documents = SimpleDirectoryReader(directory_path).load_data()
    index = GPTVectorStoreIndex.from_documents(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)
    index.storage_context.persist()
    return index

def chatbot(input_text):
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)
    #query_engine = index.as_query_engine()
    query_engine = index.as_query_engine(response_mode="tree_summarize")
    response = query_engine.query(input_text)
    #response = index.query(input_text, response_mode="compact")
    print(response.source_nodes)
    return response.response, response.source_nodes

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        exit()
    else:
        if args[1] == 'true': # args[0] is always name of the script
            from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, PromptHelper, StorageContext, load_index_from_storage
            from langchain import OpenAI
            index = construct_index("docs")
    # Start up UI, assumes index to be available, need to run one time with 'true' first after adding/changing content in folder docs
    iface = gr.Interface(fn=chatbot,
                        inputs=gr.components.Textbox(lines=7, label="Enter your text in your preferred language"),
                        outputs="text",
                        title="Dataether Chatbot")
    iface.launch(share=True)