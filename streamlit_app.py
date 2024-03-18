# gpt3 professional email generator by stefanrmmr - version June 2022

import os
#import openai
import streamlit as st


#added by Yohannes
import transformers
import torch

from transformers.utils import logging
logging.set_verbosity_error()

from transformers import pipeline 


# DESIGN implement changes to the standard streamlit UI/UX
st.set_page_config(page_title="Amharic - English Translator", page_icon="img/rephraise_logo.png",)
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -4rem;}</style>''',
    unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-znku1x a {color: #9d03fc;}</style>''',
    unsafe_allow_html=True)  # lightmode
# Design change height of text input fields headers
st.markdown('''<style>.css-qrbaxs {min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design change spinner color to primary color
st.markdown('''<style>.stSpinner > div > div {border-top-color: #9d03fc;}</style>''',
    unsafe_allow_html=True)
# Design change min height of text input box
st.markdown('''<style>.css-15tx938{min-height: 0.0rem;}</style>''',
    unsafe_allow_html=True)
# Design hide top header line
hide_decoration_bar_style = '''<style>header {visibility: hidden;}</style>'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# Design hide "made with streamlit" footer menu area
hide_streamlit_footer = """<style>#MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}</style>"""
st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


# Connect to OpenAI GPT-3, fetch API key from Streamlit secrets
#openai.api_key = os.getenv("OPENAI_API_KEY")


def translate (input_text, source_language, destination_language):

    # iterate through all seperate topics
    #for topic in range(len(contents)):
        #input_text = contents[input_text]
        #source_language = contents[source_language]
        #destination_language = contents[destination_language]

    translator = pipeline(task="translation",
                      model="facebook/nllb-200-distilled-600M",
                      torch_dtype=torch.bfloat16)

    if (source_language == 'Amahric'):
            source_language = 'amh_Ethi'
            destination_language = 'eng_Latn'
    else:
            source_language = 'eng_Latn'
            destination_language = 'amh_Ethi' 
                      
    text_translated = translator(input_text,
                             src_lang = source_language,
                             tgt_lang = destination_language)    
    return text_translated

def main_gpt3emailgen():

    st.image('img/image_banner.png')  # TITLE and Creator information
    st.markdown('Translate Amharic to English or English to Amharic based on your direct comments - powered by Artificial Intelligence (OpenAI GPT-3) Implemented by '
        '[stefanrmmr](https://www.linkedin.com/in/stefanrmmr/) - '
        'view project source code on '
        '[GitHub](https://github.com/stefanrmmr/gpt3_email_generator)')
    st.write('\n')  # add spacing

   # st.subheader('\nWhat is your email all about?\n')
    
    with st.expander("SECTION - Lnguage Input", expanded=True):

        source_language = st.selectbox('Source Language', ('Amahric', 'English'), index=0)
        input_text = st.text_input('Enter message to be transalted below', 'message')
       
        input_contents = []  # input data vector
        
        #Determine the destination language
        if (source_language == 'Amahric'):
              destination_language = 'English'
        else:
              destination_language = 'Amharic'
        
        if (input_text != ""):
            input_contents.append(str(input_text)) #input text to be translation
            input_contents.append(str(source_language)) #source language
            input_contents.append(str(destination_language)) #destination language
      
        
    if (len(input_contents) >= 1):  # initiate gpt3 mail gen process
                        #if (len(input_sender) != 0):
                        translated_text = translate(input_text, source_language, destination_language)
                        #st.markdown(translated_text)

if __name__ == '__main__':
    # call main function
    main_gpt3emailgen()
