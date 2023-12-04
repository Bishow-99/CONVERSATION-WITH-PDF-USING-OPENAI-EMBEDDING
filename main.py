import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader 
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains  import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from templates.html import user_template, bot_template, css


def get_pdf_data(pdf_files):
    text = ""
    for pdf in pdf_files:
        read_pdf = PdfReader(pdf)
        for page in read_pdf.pages:
            text+=page.extract_text()
    return text

def get_split_data(output_text):
    text_split = CharacterTextSplitter(separator="\n", chunk_size=1000, 
                                       chunk_overlap=200, length_function = len)
    chunks = text_split.split_text(output_text)
    return chunks


def get_stored_vector(splitted_text):
    embeddings = OpenAIEmbeddings()
    vector_database = FAISS.from_texts(texts = splitted_text, embedding = embeddings)
    return vector_database


def get_converstational_data(vector_database):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages = True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_database.as_retriever(),
        memory=memory
    )

    return conversation_chain

def handle_userinput(user_question):

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{output}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{output}}", message.content), unsafe_allow_html=True)


if __name__=="__main__":

    load_dotenv()

    st.set_page_config(page_title="Answer from your  PDF", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Answer from your PDF :books:")
    user_question = st.text_input("Ask about your documents")
    if user_question:
        handle_userinput(user_question)
    with st.sidebar:
        st.subheader("Process your Documents")
        pdf_files = st.file_uploader("Upoad PDF", accept_multiple_files=True)
        
        if st.button("Request"):
            with st.spinner("Loading"):
                output_text = get_pdf_data(pdf_files)
                splitted_text = get_split_data(output_text)
                vector_database = get_stored_vector(splitted_text)
                st.session_state.conversation = get_converstational_data(vector_database)


