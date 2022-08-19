import streamlit as st
import pickle
import sklearn

st.title("Language Detection")
ld = pickle.load(open("language_model.pkl", "rb"))
input_text = st.text_input(" What type of Text Language it is")

button_clicked = st.button("Language name")

if button_clicked:
    st.header(ld.predict([input_text]))

