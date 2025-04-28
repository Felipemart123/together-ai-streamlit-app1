import streamlit as st
import openai

# Set your API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Python Code Generator")

# User input
user_prompt = st.text_area("Describe the Python code you want to generate:")

if st.button("Generate Code"):
    if not user_prompt.strip():
        st.error("Please enter a description first.")
    else:
        with st.spinner("Generating code..."):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes Python scripts."},
                    {"role": "user", "content": f"Write a Python script for: {user_prompt}"}
                ],
                temperature=0.2,
                max_tokens=500,
                top_p=0.7
            )

            generated_code = response.choices[0].message.content

        st.subheader("Generated Python Code:")
        st.code(generated_code, language="python")
