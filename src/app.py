import streamlit as st
import joblib

category_model = joblib.load("models/category_model.joblib")
priority_model = joblib.load("models/priority_model.joblib")

st.title("Triage Automatico Ticket")

title = st.text_input("Oggetto")
body = st.text_area("Descrizione")

if st.button("Classifica"):
    text = title + " " + body

    cat = category_model.predict([text])[0]
    pri = priority_model.predict([text])[0]

    st.write("Categoria:", cat)
    st.write("Priorità:", pri)
