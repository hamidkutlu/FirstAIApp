#pip install --upgrade langchain langchain-openai langchain-google-genai

#---------------------------------------
#-----------------BACKEND---------------
#---------------------------------------
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ['GOOGLE_API_KEY']  = "AIzaSyBpEPY3vExuZ9bFk5VDJk_tae0RGuZhIJ4"
gemini_flash_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash") # use "gemini-2.5-pro" for Gemini Pro model

# Create prompt template for generating tweets
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])
tweet_template.format(number =7, topic = "Submarine")

# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_flash_model

# Example of using the LLM chain
#response = tweet_chain.invoke({"number" : 5, "topic" : "Wars in Middle East"})
#print(response.content)



#---------------------------------------
#-----------------FRONTEND--------------
#---------------------------------------
import streamlit as st

st.header("Tweet Generator")

st.subheader("Generate tweeets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : 5, "topic" : "Wars in Middle East"})
    st.write(tweets.content)
    