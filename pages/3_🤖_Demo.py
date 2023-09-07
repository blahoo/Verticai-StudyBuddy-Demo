import streamlit as st
import os
import modules
import base64
from audiorecorder import audiorecorder
from streamlit_extras.app_logo import add_logo
import openai
from audio_recorder_streamlit import audio_recorder


add_logo(".\\assets\\logo_reverse.png")

#for debugging

#------------
# modules.chatTranscribe()

# modules.getContext()
# modules.chatCall()

# modules.chatSpeak()
#------------
# modules.context = [{"role": "user", "content": "prompt"},
#                    {"role": "user", "content": "prompt"},
#                    {"role": "user", "content": "prompt"},
#                    {"role": "user", "content": "prompt"}]
#------------

# Insert a chat message container.
with st.chat_message("assistant"):
    st.write("👋")

def chatgpt(prompt):
    modules.context.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message = st.empty()
        full_response = ""

        modules.chatCall()

        for response in openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = modules.context,
            stream = True
            ):
            
            # all this to get the word by word text output for the true gpt vibe
            msg_chunk = response["choices"][0].get("delta", {}).get("content")
            if msg_chunk is not None:
                full_response += msg_chunk
                message.markdown(full_response + "")

        message.markdown(full_response)

    modules.context.append({"role": "assistant", "content": full_response})

    return full_response


def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

not_pre_prompt = 0

print(not_pre_prompt)

for message in modules.context:
    print(message)
    if not_pre_prompt:
        with st.chat_message(message["role"]):    
            st.markdown(message["content"])
    not_pre_prompt = 1




if prompt := st.chat_input("Type here"):
    chatgpt(prompt)




old_audio = []
audio = []

print(old_audio)
print(audio)

old_audio = audio
audio = audiorecorder("Speech", "Submit", 'p')


if audio != old_audio and len(audio) > 0:

    print(audio)
    
    audio_out = open("sample.wav", "wb")
    audio_out.write(audio.tobytes())

    msg = modules.chatTranscribe(".\\sample.wav")

    text_to_speech = chatgpt(msg)

    audio_path = modules.chatSpeak(text_to_speech)

    autoplay_audio(audio_path)
    





