# This project takes phone call transcripts and produces succinct summaries of them using
# OpenAI's LLM GPT-3. Keyword extraction via Lexigram is also implemnted to produce tags
# that will help organize phone calls by topic.


# Import the required libraries
import openai
import streamlit as st

# Set the GPT-3 API key
openai.api_key = st.secrets["pass"]

audio = st.file_uploader("Upload an audio file", type=["mp3"])

transcript = st.text_area("Enter your phone call transcript to summarize")
if st.button("Generate Summary",type='primary'):
    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Please summarize this phone call transcript for me in a few sentences: " + transcript,
            max_tokens = 516,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)

'''
if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

if len(article_text)>100:
    if st.button("Generate Summary",type='primary'):
    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Please summarize this scientific article for me in a few sentences: " + article_text,
            max_tokens = out_token,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to summarize!")

output_size = st.radio(label = "What kind of output do you want?", 
                    options= ["To-The-Point", "Concise", "Detailed"])

'''