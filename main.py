# main.py

import logging
import sys

# LlamaIndex libraries
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Configure logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

try:
    # --- Model Configuration ---
    # Explicitly instantiate the models to be used
    #by default, LlamaIndex uses OpenAI models and request timeouts are short 120 seconds
    #llm = Ollama(model="llama3", request_timeout=600.0)
    #embed_model = OllamaEmbedding(model_name="llama3")
    #llama3 does not work properly due to performance issues, even with request_timeout increased

    print("Executing agent with the phi3 model...")
    llm = Ollama(
        model="phi3:mini", 
        request_timeout=600.0,
        context_window=6000
        
        )
    embed_model = OllamaEmbedding(model_name="phi3:mini")

    # Set the models globally in Settings
    # This is a good practice to ensure consistency
    Settings.llm = llm
    Settings.embed_model = embed_model
    
    # --- RAG Process ---
    # Load documents
    documents = SimpleDirectoryReader("data").load_data()
    logging.info("Loaded documents successfully.")

    # Create the index
    # The settings (llm and embed_model) will be used automatically here
    index = VectorStoreIndex.from_documents(documents)
    logging.info("Index created successfully.")

    # Create a query engine
    query_engine = index.as_query_engine()
    logging.info("Query engine created successfully.")

    # --- Querying the Agent ---
    response = query_engine.query("Qual a população de Curitiba?")

    # Print the response
    print("\n--- Agent's Response ---")
    print(response)

except Exception as e:
    logging.error(f"An error occurred: {e}")
    # This will help us debug connection issues with Ollama if they happen
    logging.error(
        "Please ensure the Ollama container is running and the 'llama3' model is available. "
        "You can check by running 'docker ps' and 'docker exec ollama ollama list'."
    )