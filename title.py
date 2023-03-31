import streamlit as st

st.set_page_config(layout="wide")
import streamlit themes as stt
# Set the theme using the `set_theme` function
stt.set_theme('dark')
st.title(':blue[Bird Detecting & Counting App]')
st.title(':green[You can detect and count the number of birds by giving us :bird: images.]')


from PIL import Image
image = Image.open('b19_(15).JPEG')

st.image(image, caption='Beautiful Peacock')

import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file",type=['jpg','jpeg'])
if uploaded_file is not None:
    # To read file as bytes:
   # bytes_data = uploaded_file.getvalue()
   # st.write(bytes_data)

    # To convert to a string based IO:
   # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
   # st.write(stringio)

    # To read file as string:
    #string_data = StringIO.read()
    #st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
   # dataframe = pd.read_jpg(uploaded_file)
    #st.write(dataframe)
    st.image(uploaded_file)
