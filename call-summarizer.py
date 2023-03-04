# This project takes phone call transcripts and produces succinct summaries of them using
# OpenAI's LLM GPT-3. Keyword extraction via Lexigram is also implemnted to produce tags
# that will help organize phone calls by topic.

# Import the required libraries
import openai
import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

# Set the GPT-3 API key
openai.api_key = st.secrets["pass"]

audio_file = st.file_uploader("Upload an audio file", type=["mp3"])
if audio_file:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio_file.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)
        transcript = result["text"]
else:
    transcript = st.text_area("Enter your phone call transcript to summarize")

if st.button("Generate Summary",type='primary'):
    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Please summarize this phone call transcript between an insuree and their insurer in a few sentences: " + transcript,
            max_tokens = 516,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.success(res)
