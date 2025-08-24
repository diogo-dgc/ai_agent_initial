# AI Agent Initial
![Version](https://img.shields.io/badge/version-v1.0.0-blue)
![Status](https://img.shields.io/badge/status-ready-green)

## 📖 Project Summary
This project marks the beginning of my learning journey in Artificial Intelligence, focusing on the development of AI agents and automation flows. The main goal is to build a functional **Retrieval-Augmented Generation (RAG)** agent, capable of answering questions based on a local knowledge base.

Version `v1.0.0` implements a minimalist RAG agent that reads a text document and answers questions about its content. It uses an open-source **Large Language Model (LLM)** running locally, demonstrating a robust and autonomous approach.

## 🚀 Technologies
The project was developed with the following technologies and frameworks:

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-0.10.0-orange.svg)
![Ollama](https://img.shields.io/badge/Ollama-1.0.0-lightgreen.svg)
![Docker](https://img.shields.io/badge/Docker-20.10-blue.svg?logo=docker)
![Git](https://img.shields.io/badge/Git-2.30-red.svg?logo=git)
![VSCode](https://img.shields.io/badge/VSCode-1.80-blue.svg?logo=visualstudiocode)

## 📋 Prerequisites
To run this project, you need to have the following tools installed and configured.

### 1. Python and Virtual Environment
It is highly recommended to use a virtual environment to isolate the project's dependencies.
```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

# 🚀 Get started
Follow these steps to set up and run the agent for the first time.

## Start Ollama and pull the model

```Bash

# Start the Ollama container
docker run -d -v ollama_data:/root/.ollama -p 11434:11434 --name ollama_agent ollama/ollama

# Download the Phi3 model, optimized for local machines
docker exec ollama_agent ollama pull phi3:mini
```
Alternatively, you can use the native Ollama application for macOS, available at ollama.com.

## Install Python Dependencies

```Bash

# With the virtual environment activated, install the necessary libraries:
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
```

# 🚀 How to Run
Once all the above steps are complete, you can run the agent with the following command. Make sure Ollama is running.

```Bash
python3 main.py
```