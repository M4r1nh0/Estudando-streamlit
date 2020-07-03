import streamlit as st
import pandas as pd
import numpy as np

#text/Titlle
st.title('Iniciando streamlit')

#header/subheadear
st.header('Isso é um header')
st.subheader('Isso é um subheader')

#text
st.text('Isso é um texto')

#markdown
st.markdown('### Isso é markdown')

#Error/Coloe texto
st.success('Sucesso')
st.info('Info')
st.warning('isso é perigoso')
st.error('This is an error')

#get help info about python
st.help(range)

#writing texto
st.write('text with write')
st.write(range(10))

#imagens
from PIL import Image
img = Image.open("example.jpg")
st.image(img, width=300, caption="Simple")

#Videos

#vid_file = open('video.mp4', 'rb')
#vid_byte = vid_file.read()
#st.video(vid_file)

#radio
status = st.radio('What is your status',('Active','Inactive'))

if status == "Active":
    st.success('vc esta ativo')
else:
    st.warning('Inactive')

#selectbox

box = st.selectbox('Yout occupation', ["Programmer","DataScientis", "Web "])
st.write("you select this option", box)

#multiselect
location = st.multiselect("Where do you work? ",('London', 'Curitiba', 'new york', 'Rondonia'))
st.write('you select', len(location),'Locations')

#slider

age = st.slider('what is your level',1,5)
