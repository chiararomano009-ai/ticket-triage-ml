# Ticket Triage Automatico con Machine Learning

## Descrizione
Questo progetto implementa un sistema di classificazione automatica dei ticket aziendali.

Il sistema classifica:
- Categoria: Amministrazione, Tecnico, Commerciale
- Priorità: Bassa, Media, Alta

## Dataset
Dataset sintetico composto da 300 ticket.

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
