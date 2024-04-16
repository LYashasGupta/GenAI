import streamlit as st
from openai import OpenAI

# Read API key from file
with open("keys/.open_api_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)

# Set colored page title
st.title(":rainbow[Python Code Review with OpenAI]")

# User input section
st.header(":orange[Enter Your Python Code]",divider='orange')
prompt = st.text_area("Enter your Python code here:", height=200)

# Button to trigger code review
if st.button("Review the Code"):
    st.markdown("<h2 style='color:blue;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text
    generated_text = response.choices[0].message.content
    st.write(generated_text)