import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("GitHub Actions - Answering all your questions")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    # Prompt
    template = "As an expert on GitHub Actions, please answer any user questions about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)
