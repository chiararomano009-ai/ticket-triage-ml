import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

df = pd.read_csv("data/tickets_dataset.csv")

df["text"] = (df["title"] + " " + df["body"]).apply(clean_text)

X = df["text"]
y_cat = df["category"]
y_pri = df["priority"]

X_train, X_test, y_train_cat, y_test_cat = train_test_split(X, y_cat, test_size=0.2)

pipeline_cat = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline_cat.fit(X_train, y_train_cat)

y_pred_cat = pipeline_cat.predict(X_test)

print("=== Categoria ===")
print("Accuracy:", accuracy_score(y_test_cat, y_pred_cat))
print(classification_report(y_test_cat, y_pred_cat))

# PRIORITÀ
X_train, X_test, y_train_pri, y_test_pri = train_test_split(X, y_pri, test_size=0.2)

pipeline_pri = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline_pri.fit(X_train, y_train_pri)

y_pred_pri = pipeline_pri.predict(X_test)

print("=== Priorità ===")
print("Accuracy:", accuracy_score(y_test_pri, y_pred_pri))
print(classification_report(y_test_pri, y_pred_pri))

joblib.dump(pipeline_cat, "models/category_model.joblib")
joblib.dump(pipeline_pri, "models/priority_model.joblib")

print("Modelli salvati!")
