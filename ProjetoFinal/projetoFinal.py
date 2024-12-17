from langchain_aws import BedrockLLM
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
import streamlit as st
import boto3

# Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

modelID = "amazon.titan-text-premier-v1:0"

# Configuração do LLM
llm = BedrockLLM(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={"max_tokens": 2000, "temperature": 0.9}
)

def my_chatbot(language, freeform_text):
    prompt = PromptTemplate(
        input_variables=["language", "freeform_text"],
        template="Você é um chatbot. Você está falando em {language}.\n\n{freeform_text}"
    )
    sequence = prompt | llm
    # Geração da resposta
    response = sequence.invoke({'language': language, 'freeform_text': freeform_text})
    return response


st.title("Id@mascenoBot")

language = st.sidebar.selectbox("Selecione o idioma", ["Portugues", "Ingles", "Espanhol"])

# Entrada de texto
freeform_text = st.sidebar.text_area(label="Qual a sua pergunta?", max_chars=100)

# Processamento da resposta
if st.sidebar.button("Enviar"):
    if freeform_text.strip():
        try:
            response = my_chatbot(language, freeform_text)
            st.write(response)
        except Exception as e:
            st.error(f"Erro ao processar a solicitação: {e}")
    else:
        st.warning("Por favor, insira uma pergunta.")



st.markdown(
    """
    <style>
    /* Cor de fundo */
  
    .stApp .st-emotion-cache-vmpjyt .st-emotion-cache-6qob1r{
        background-image:linear-gradient(-8deg, #000046 0%, #1cb5e0 100%);
    }

    /* Estilo do título */
    .title {
        font-size: 2.5rem;
        color: #ff6347;
        font-weight: bold;
        text-align: center;
    }

 div.stButton > button {
        background-color: #28a745; 
        color: white; 
        border: none; 
        border-radius: 5px; 
        padding: 10px 20px; 
        font-size: 16px; 
        cursor: pointer;
    }

    div.stButton > button:hover {
        background-color: #218838;
          color: white;
    }

     div.stButton > button:active {
        background-color: #218838;
          color: white;
    }
    """,
    unsafe_allow_html=True
)