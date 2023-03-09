# Phone Call Summarizer
### This app transcribes phone call audio, then summarizes the transcription into a short, succint summmary.
![image](https://user-images.githubusercontent.com/57726227/223763318-cb5a320c-cc2d-4c84-88f9-77bd6faf50b0.png)

##### The idea behind this project was to create a tool that would be useful for companies that record calls for "quality assurance purposes". Once a call is recorded, often times the resulting transcription can be long and cumbersome, filled with useless filler words that don't offer actionable insights for a customer service team.

##### By leveraging OpenAI's large language models, we can automate call summarizing, so at a glance, a business owner can see what their customers are calling for and understand their market better.

##### Local Development Env
Requirements:
```
pip install openai # for summarization of transcripts
pip install streamlit # for front end
pip install whisper # for speech-to-text transcription
```
##### Once you've cloned the project and downloaded the requirements. Create a folder called .streamlit within the phone-call-summarizer folder. Inside .streamlit, create a secrets.toml file. Here set 'pass' equal to your OpenAI API Key which you can generate by making an account with OpenAI here https://openai.com/blog/openai-api.

#### File Structure:
![image](https://user-images.githubusercontent.com/57726227/223767910-b8cab715-a9fe-4a87-ae6a-cd53433cae7f.png)
#### secrets.toml
![image](https://user-images.githubusercontent.com/57726227/223769141-07e9ce26-3d51-4f4f-ad1e-f00f54ef8228.png)

##### Once this has been completed, you should be able run the app locally with the terminal command:
```
steamlit run call-summarizer.py
```


Adapted from Avrab's gist, special thanks to him! https://gist.github.com/avrabyt/1ca1fee4712e9d59957c2e83da868bca
