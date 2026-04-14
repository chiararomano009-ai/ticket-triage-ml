import streamlit as st
import joblib

# Caricamento modello categoria
category_model = joblib.load("models/category_model.joblib")

st.title("Triage Automatico Ticket")

title = st.text_input("Oggetto")
body = st.text_area("Descrizione")

def suggest_priority(text):
    text = text.lower()

    high_keywords = [
        "urgente", "bloccato", "bloccante", "errore grave",
        "impossibile", "fermo", "non funziona", "server", "accesso impossibile"
    ]
    medium_keywords = [
        "ritardo", "verifica", "problema", "anomalia",
        "sollecito", "aggiornamento", "non vedo", "controllo"
    ]

    if any(word in text for word in high_keywords):
        return "Alta"
    elif any(word in text for word in medium_keywords):
        return "Media"
    else:
        return "Bassa"

if st.button("Classifica"):
    if title.strip() == "" and body.strip() == "":
        st.warning("Inserisci almeno un testo")
    else:
        text = title + " " + body

        cat = category_model.predict([text])[0]
        pri = suggest_priority(text)

        st.success("Risultato classificazione")
        st.write("📂 Categoria:", cat)
        st.write("⚡ Priorità:", pri)
