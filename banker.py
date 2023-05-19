#import os for setup
import os

#import OpenAI as main LLM 
from langchain.llms import OpenAI

#streamlit for UI interface
import streamlit as st

#import pdf document loaders
from langchain.document_loaders import PyPDFLoader

#import chroma as the vector stores
from langchain.vectorstores import Chroma


#import vector store
from langchain.agents.agent_toolkits import(
    create_vectorstore_agent, 
    VectorStoreToolkit,
    VectorStoreInfo
)

os.environ['OPENAI_API_KEY'] = 'Your_API_KEY'

#create Instances
#A higher temperature (e.g., 0.9) results in more diverse and creative output, while a lower temperature (e.g., 0.2) makes the output more deterministic and focused
llm = OpenAI(temperature=0.9)

#load pdf Loader
loader = PyPDFLoader('annualreport.pdf')

#split pages from pdf
pages = loader.load_and_split()


#load document vectors in chromeDB
store = Chroma.from_documents(pages, collection_name = 'annualreport')

#vectorstore info object
vectorstore_info = VectorStoreInfo(
    name = "annual_report",
    description = "banking annual report as pdf",
    vectorstore=store
)

#convert document store into langchain toolkit
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)

#add toolkit to end-to-end LC
agent_executer = create_vectorstore_agent(
    llm = llm, 
    toolkit=toolkit, 
    verbose=True
)

st.title('Answering Questions without Fine Tuning')
# Create a text input box for the user
prompt = st.text_input('Input your prompt here')

# If the user hits enter
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executer.run(prompt)
    # ...and write it out to the screen
    st.write(response)

    # With a streamlit expander  
    with st.expander('Document Similarity Search'):
        # Find the relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Write out the first 
        st.write(search[0][0].page_content)