from openai import OpenAI
import streamlit as st

f = open("keys/.open_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.title(":rainbow[GenerativeAI]")
st.header('AI Generator App', divider='orange')

# client.create_completion("Hello world")

prompt = st.text_input('Enter a data science topic')
if st.button("Generate"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role":"system","content":"Generate 5 data Science questions and answer for MCQ test in MCQ format."},
            {"role":"user","content":prompt}
    ]
    )

    if response.choices:
        st.write(response.choices[0].message.content)