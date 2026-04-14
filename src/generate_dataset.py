import random
import pandas as pd

random.seed(42)

N_TICKETS = 300

CATEGORIES = ["Amministrazione", "Tecnico", "Commerciale"]
PRIORITIES = ["Bassa", "Media", "Alta"]

admin_titles = [
    "Pagamento fattura non registrato",
    "Richiesta copia fattura",
    "Verifica bonifico inviato",
    "Problema con scadenza pagamento"
]

tech_titles = [
    "Errore in fase di login",
    "Piattaforma bloccata",
    "Sistema non disponibile",
    "Problema accesso utente"
]

sales_titles = [
    "Richiesta preventivo",
    "Informazioni su ordine",
    "Disponibilità prodotto",
    "Aggiornamento consegna"
]

def generate_ticket(category, priority):
    if category == "Amministrazione":
        title = random.choice(admin_titles)
    elif category == "Tecnico":
        title = random.choice(tech_titles)
    else:
        title = random.choice(sales_titles)

    body = f"Richiesta relativa a {title.lower()} con priorità {priority.lower()}."
    return title, body

data = []

for i in range(N_TICKETS):
    category = random.choice(CATEGORIES)
    priority = random.choice(PRIORITIES)
    title, body = generate_ticket(category, priority)

    data.append({
        "id": i,
        "title": title,
        "body": body,
        "category": category,
        "priority": priority
    })

df = pd.DataFrame(data)
df.to_csv("data/tickets_dataset.csv", index=False)

print("Dataset creato!")
