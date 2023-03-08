# Import the required libraries
import openai
import streamlit as st
import whisper
from tempfile import NamedTemporaryFile

# Set the GPT-3 API key
openai.api_key = st.secrets["pass"]

st.title("Phone Call Summarizer")
st.subheader("Transcribes and summarizes the contents of a phone call into a short, succinct summary.")

audio_file = st.file_uploader("Upload an audio file", type=["mp3"])
st.write("Need an audio file? Click [here](https://drive.google.com/file/d/1PeAj5QJG1AvBsw-7FdDlRJSrlAdG5r_K/view?usp=share_link) for a sample phone call.")

if audio_file:
    with NamedTemporaryFile(suffix="mp3") as temp:
        temp.write(audio_file.getvalue())
        temp.seek(0)
        model = whisper.load_model("base")
        result = model.transcribe(temp.name)
        transcript = result["text"]
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Please summarize this phone call transcript into a few sentences: " + transcript,
            max_tokens = 516,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.subheader("Before:")
        st.write(transcript)
        st.subheader("After:")
        st.write(res)
else:
    transcript = st.text_area("Or enter a phone call transcript to summarize")
    if st.button("Generate Summary",type='primary'):
    # Use GPT-3 to generate a summary of the article
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Please summarize this phone call transcript into a few sentences: " + transcript,
            max_tokens = 516,
            temperature = 0.5,
        )
        # Print the generated summary
        res = response["choices"][0]["text"]
        st.subheader("Before:")
        st.write(transcript)
        st.subheader("After:")
        st.write(res)