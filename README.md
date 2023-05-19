# LLM-OpenAI-Financialist-Bot
# README

This repository contains a Python script that utilizes the Langchain library for answering questions without fine-tuning. The script uses OpenAI's language model (LLM), Streamlit for the UI interface, and PDF document loaders to perform various tasks.

## Prerequisites
- Python 3.x
- Required libraries: `os`, `langchain.llms`, `streamlit`, `langchain.document_loaders`, `langchain.vectorstores`, `langchain.agents.agent_toolkits`

## Setup
1. Clone this repository to your local machine.
2. Install the required libraries mentioned above using the package manager of your choice.
3. Set up your OpenAI API key by assigning it to the `OPENAI_API_KEY` environment variable. For example:
   ```shell
   export OPENAI_API_KEY='Your_API_Key'
   
##Usage
1) Make sure you have the necessary dependencies installed and the OpenAI API key set.
2) Run the script by executing the following command in your terminal or command prompt:
    - streamlit run banker.py
3) The script will launch a Streamlit app with a text input box.
4) Enter your prompt in the text input box and press enter.
5) The script will utilize the Langchain library and OpenAI's LLM to generate a response based on your prompt.
6) The response will be displayed on the screen.
7) If you expand the "Document Similarity Search" section, the script will perform a similarity search with the provided prompt on a PDF document named 'annualreport.pdf'. The most relevant page's content will be displayed.
"# LLM-Finance" 
