import streamlit as st
import together

# Set your API key
together.api_key = st.secrets["TOGETHER_API_KEY"]

# Model to use
MODEL = "togethercomputer/CodeLlama-13b-Instruct"

st.title("Python Code Generator with Together AI")

# Get user input
user_prompt = st.text_area("Describe the Python code you want to generate:")

if st.button("Generate Code"):
    if not user_prompt.strip():
        st.error("Please enter a description first.")
    else:
        with st.spinner("Generating Python code..."):
            response = together.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes Python code based on user descriptions."},
                    {"role": "user", "content": f"Write a Python script for the following request:\n{user_prompt}"}
                ],
                max_tokens=300,
                temperature=0.2,
                top_p=0.7,
            )

            generated_code = response.choices[0].message.content

        st.subheader("Generated Python Code:")
        st.code(generated_code, language="python")
