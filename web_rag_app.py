import streamlit as st
st.title("Hello test")
st.write("App is alive")




# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# # Streamlit app title
# st.title("Web-based RAG Q&A System")

# # Sidebar for API key and model selection
# st.sidebar.header("Settings")
# groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
# model_name = st.sidebar.selectbox("Select Groq Model", ["openai/gpt-oss-120b", "qwen/qwen3-32b"])  # Add more models as needed

# # Input for URL
# url = st.text_input("Enter the URL to load content from:", value="https://example.com")

# # Button to load and process the URL
# if st.button("Load and Process URL"):
#     if not groq_api_key:
#         st.error("Please enter your Groq API key.")
#     else:
#         with st.spinner("Loading and processing..."):
#             # Step 1: Load documents from the web
#             loader = WebBaseLoader(url)
#             documents = loader.load()

#             # Step 2: Split the documents into chunks
#             text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
#             chunks = text_splitter.split_documents(documents)

#             @st.cache_resource
#             def get_embeddings():
#                 return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            
           
#             vectorstore = FAISS.from_documents(chunks, embeddings)

#             # Step 4: Set up the retriever
#             retriever = vectorstore.as_retriever()

#             # Step 5: Define the prompt template
#             template = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the anser use your intelligence as well.

# Question: {question}

# Context: {context}

# Answer:"""
#             prompt = ChatPromptTemplate.from_template(template)

#             # Step 6: Set up the LLM using Groq API
#             llm = ChatGroq(model=model_name, temperature=0, api_key=groq_api_key)

#             # Step 7: Create the RAG chain
#             rag_chain = (
#                 {"context": retriever, "question": RunnablePassthrough()}
#                 | prompt
#                 | llm
#                 | StrOutputParser()
#             )

#             # Store the chain in session state
#             st.session_state.rag_chain = rag_chain
#             st.success("URL processed successfully! You can now ask questions.")

# # Input for query
# query = st.text_input("Enter your question:")

# # Button to ask question
# if st.button("Ask"):
#     if "rag_chain" not in st.session_state:
#         st.error("Please load and process a URL first.")
#     elif not query:
#         st.error("Please enter a question.")
#     else:
#         with st.spinner("Generating answer..."):
#             response = st.session_state.rag_chain.invoke(query)
#             st.write("**Answer:**")
#             st.write(response)
