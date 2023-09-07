import streamlit as st
import numpy as np
from PIL import Image
from modules import chatSetUp
from streamlit_extras.app_logo import add_logo
import base64
from pathlib import Path


st.set_page_config(page_title="verticai", page_icon=":graduation cap:", layout="wide")

add_logo(".\\assets\\logo_reverse.png")

st.image('.\\assets\\verticai.png')

def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")


st.text("\n\n\n") # adds space
st.text("\n\n\n") 
st.text("\n\n\n") 
st.text("\n\n\n") 
st.text("\n\n\n") 
st.text("\n\n\n") 
st.text("\n\n\n") 
st.text("\n\n\n") 



st.markdown("""
<style>
.big-font {
    font-size:25px !important;
    text-align: center
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font"> 75% of the world cannot speak English, 75% of products operate soley with English</p>', unsafe_allow_html=True)


st.text("\n\n\n") 
st.text("\n\n\n") 
st.text("\n\n\n") 

with st.container():
     left, mid = st.columns([1, 1])
     with left:
          with st.expander("What Is Verticai?"):
               st.write("Verticai uses top-of-the-line technology to help students in need with tutoring and mentorship!")
     with mid:
          with st.expander("Is Verticai Free?"):
               st.write("Yes, Verticai is completely free! However, there will be a paid version to enhance the quality of those who seek better education.")

with st.container():
     left, right = st.columns([1, 1])
     with left:
          with st.expander("What Is Verticai's End Goal?"):
               st.write("From anywhere in any country, Verticai wishes to give everyone a free mentor that can help them with their school work!")
     with right:
          with st.expander("Does Verticai use Streamlit?"):
               st.write("Yes! Streamlit's extremely compatible website capabilities help out with the web creation at Verticai!")

with st.container():
     mid, right = st.columns([1, 1])
     with mid:
          with st.expander("Answer Questions?"):
               st.write("So far, Verticai is in training and can only answer a few questions from various Canadian textbooks like Pearson, Nelson, etc.")
     
     with right:
          with st.expander("Does Verticai Support Cheating?"):
               st.write("No, Verticai implicitly supports good usage of education by giving everyone access to educational rescources.")

st.text("\n\n\n") # adds spacing


st.text("\n\n\n") 
st.text("\n\n\n")  


def img_to_bytes(img_path):
    img_bytes = Path('.\\assets\\graph.png').read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

st.markdown("<p style='text-align: center; color: grey;'>"+img_to_html('graph.png')+"</p>", unsafe_allow_html=True)


st.text("\n\n\n")      
st.text("\n\n\n") # adds spacing


st.header("Sign up for the BETA")
# Sign up for our early release
with st.form(key='my_form', clear_on_submit=True):
     email = st.text_input('Email')
     name = st.text_input('Name')
     st.form_submit_button('Sign up')
     


