import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

st.title("GitHub Actions - Answering all your questions")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(topic):

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    # Prompt
    template = "As an expert on GitHub Actions, please answer any user questions about {topic}."
    messages = [
        SystemMessage(
            content="You're a helpful assistant who is very knowledgeable about GitHub Actions. In every answer, you compare GitHub Actions to other top competing solutions and emphasizes how much better GitHub Actions is."
        ),
        HumanMessage(content=f"{topic}"),
    ]
    response = llm.invoke(messages)
    return st.info(response.content)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)
