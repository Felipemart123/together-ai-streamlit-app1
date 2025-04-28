import streamlit as st
import together

# Set your API key from Streamlit secrets
together.api_key = st.secrets["TOGETHER_API_KEY"]

# Set the Together AI model you want to use
MODEL = "togethercomputer/CodeLlama-13b-Instruct"  # Good for code generation

st.title("Python Code Generator with Together AI")

# Text input from the user
user_prompt = st.text_area("Enter a description of the Python code you want:")

# Button to trigger code generation
if st.button("Generate Code"):
    if user_prompt.strip() == "":
        st.error("Please enter a description first!")
    else:
        with st.spinner("Generating code..."):
            response = together.Complete.create(
                prompt=f"Write a Python script for the following request:\n{user_prompt}",
                model=MODEL,
                max_tokens=300,
                temperature=0.2,
                top_p=0.7,
            )
            generated_code = response['output']['choices'][0]['text']

        # Display the result
        st.subheader("Generated Python Code:")
        st.code(generated_code, language="python")
