# Ticket Triage Automatico con Machine Learning

## Descrizione
Questo progetto implementa un sistema di classificazione automatica dei ticket aziendali.

Il sistema classifica:
- Categoria: Amministrazione, Tecnico, Commerciale
- Priorità: Bassa, Media, Alta

## Dataset

Il dataset utilizzato per l’addestramento è di tipo sintetico ed è composto da circa 300 ticket.

Ogni ticket include:
- titolo (title)
- descrizione (body)
- categoria (Amministrazione, Tecnico, Commerciale)
- priorità (Bassa, Media, Alta)

Il dataset completo è disponibile nella cartella /data del repository.

## Tecnologie
- Python
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit

## Esecuzione

pip install -r requirements.txt  
python src/generate_dataset.py  
python src/train_models.py  
streamlit run src/app.py
Il progetto è completamente riproducibile seguendo i passaggi sopra indicati.
