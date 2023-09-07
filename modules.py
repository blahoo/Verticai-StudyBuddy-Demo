import openai
from langdetect import detect 
from gtts import gTTS
from key import getOpenAiKey #make sure ur key aint blocked :skull:

# script_path = os.path.abspath(file)
# root_directory = os.path.dirname(script_path)

# model = whisper.load_model('base')
# if running localy, you can take advantage of actual whisper

context = []
key_setup = [False]


def getContext():
  return context

def chatSetUp(subject="math", grade="9", country="Canada"): #sets up prePrompt for context and sets up the openai api

  if not key_setup[0]:
    openai.api_key = getOpenAiKey()
    key_setup[0] = True


  pre_prompt = f"You are a highly knowledgeable high school tutor specializing in {subject} for grade {grade} students in {country}. Keep your answers short, brief, but concise and never go above 200 words. As a tutor your job is to answer all of the users subject specific questions. Feel free to provide ideas for other academic resources and provide study plans to the user.".format(subject, grade, country)

  return pre_prompt;


def chatTranscribe(audio_path):

  # audio_path = os.path.join(".\\", "sample.wav") --for testing
  if not key_setup[0]:
    openai.api_key = getOpenAiKey()
    key_setup[0] = True

  with open(audio_path, "rb") as audio_file:
    transcript = (openai.Audio.transcribe("whisper-1", audio_file))['text']


  print("transcript:", transcript)

  return transcript


def chatCall():
  if not key_setup[0]:
    openai.api_key = getOpenAiKey()
    key_setup[0] = True



def chatSpeak(input_text): #text to speech with free google libs B)
  
  lang_code = detect(input_text)
  print("Detected language:", lang_code)

  tts = gTTS(text = input_text, lang = lang_code)  # Specify the language ('en' for English)
  tts.save("output.mp3")  # Save to an MP3 file

  return(".\\output.mp3")



