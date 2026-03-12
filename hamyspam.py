# ==========================================================
# PROYECTO: DETECCIÓN DE SPAM Y HAM CON NAIVE BAYES
# Autor: Joseph de Jesús Lemus Pineda
# Descripción:
# Este programa entrena un modelo de Machine Learning para
# clasificar mensajes como SPAM o HAM utilizando TF-IDF
# y el algoritmo Naive Bayes.
# ==========================================================


# ==========================================================
# 1. IMPORTACIÓN DE LIBRERÍAS
# ==========================================================

import re
import pandas as pd


# ==========================================================
# 2. CREACIÓN DEL DATASET
# Se generan 30 mensajes de SPAM y 30 mensajes de HAM
# que serán utilizados para entrenar el modelo.
# ==========================================================

spam_messages = [
"Congratulations! You have been selected to win a brand new iPhone. Click here to claim your prize now.",
"Limited time offer! Get 80% discount on all products if you buy today.",
"You are the lucky winner of a $1000 gift card. Claim it before it expires.",
"Earn money from home with this simple method. Start making $500 a day.",
"Your account has been temporarily suspended. Verify your information immediately.",
"Special promotion just for you. Buy one get one free only today.",
"Hot singles are waiting to meet you in your area. Click here now.",
"You have an unclaimed reward. Log in now to receive your prize.",
"Act fast! This exclusive investment opportunity guarantees huge profits.",
"Congratulations! Your email has won our international lottery.",
"Your payment was declined. Update your billing information now.",
"Last chance to claim your free vacation tickets. Offer ends tonight.",
"Make money online with no experience required. Join now.",
"You have been selected for a free trial of our premium service.",
"Your package delivery failed. Click here to reschedule immediately.",
"Get rich quickly using this proven system used by thousands.",
"Important notice: your bank account requires verification.",
"You are pre-approved for a personal loan up to $10,000.",
"Download this app now and receive free rewards instantly.",
"Only a few spots left. Register now before it's too late.",
"Your profile has been chosen for a special bonus reward.",
"Click here to unlock your exclusive membership benefits.",
"You have received a confidential financial proposal.",
"Earn passive income every day with this investment strategy.",
"Your subscription will expire soon. Renew now to avoid interruption.",
"Win big prizes by entering our online contest today.",
"Exclusive deal: save 70% on luxury watches today.",
"Security alert! Someone tried to access your account.",
"You have been randomly selected for a special survey reward.",
"Final notice: claim your bonus before midnight tonight."
]


ham_messages = [
"Hey, are we still meeting after school today?",
"Don't forget to bring the homework tomorrow.",
"I sent you the document by email, check if you received it.",
"Let me know when you arrive home safely.",
"Are you available to study together this weekend?",
"Thanks for helping me with the assignment yesterday.",
"I will call you later when I finish my class.",
"Can you send me the notes from today's lecture?",
"We should start working on the project soon.",
"I'll be a little late to the meeting today.",
"Did you understand the last math problem?",
"Let's go eat something after the exam.",
"I just finished the report, I'll send it to you now.",
"Remember we have a presentation tomorrow morning.",
"I think the teacher changed the deadline.",
"Text me when you get to the bus station.",
"I'm already at the library waiting for you.",
"Do you want to practice English later?",
"I will bring my laptop so we can finish the work.",
"The class today was actually very interesting.",
"Let me know if you need help with the code.",
"I just uploaded the files to the shared folder.",
"Can we move the meeting to tomorrow?",
"I'm going to the store, do you need anything?",
"I'll send you the pictures from the trip later.",
"Don't worry, we'll figure out the solution together.",
"I'm reviewing the material for tomorrow's test.",
"Tell me if the program runs correctly on your computer.",
"Let's schedule another session to finish the project.",
"See you tomorrow morning at school."
]


# ==========================================================
# 3. CREACIÓN DEL DATAFRAME
# Se combinan los mensajes y se agregan sus etiquetas
# (spam o ham).
# ==========================================================

messages = spam_messages + ham_messages
labels = ["spam"] * len(spam_messages) + ["ham"] * len(ham_messages)

df = pd.DataFrame({
    "mensaje": messages,
    "tipo": labels
})


# ==========================================================
# 4. LIMPIEZA DE TEXTO
# Se eliminan elementos que no aportan valor semántico:
# - Conversión a minúsculas
# - Eliminación de URLs
# - Eliminación de menciones
# - Eliminación de números
# - Eliminación de caracteres especiales
# ==========================================================

def limpiar_texto(texto):

    texto = texto.lower()
    texto = re.sub(r'http\S+|www\S+', '', texto)
    texto = re.sub(r'@\w+', '', texto)
    texto = re.sub(r'\d+', '', texto)
    texto = re.sub(r'[^a-z\s]', '', texto)
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto


df["mensaje_limpio"] = df["mensaje"].apply(limpiar_texto)


# ==========================================================
# 5. TOKENIZACIÓN Y ELIMINACIÓN DE STOPWORDS
# Se divide el texto en palabras y se eliminan palabras
# comunes que no aportan significado (stopwords).
# ==========================================================

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

stop_words = set(stopwords.words("spanish"))


def procesar_texto(texto):

    palabras = texto.split()

    palabras_filtradas = [p for p in palabras if p not in stop_words]

    return " ".join(palabras_filtradas)


df["mensaje_procesado"] = df["mensaje_limpio"].apply(procesar_texto)


# ==========================================================
# 6. ENTRENAMIENTO DEL MODELO
# Se convierte el texto en vectores numéricos usando TF-IDF
# ==========================================================

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["mensaje_procesado"])
y = df["tipo"]


# ==========================================================
# 7. DIVISIÓN DE DATOS
# 80% entrenamiento
# 20% prueba
# ==========================================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# ==========================================================
# 8. MODELO NAIVE BAYES
# Se utiliza Multinomial Naive Bayes para clasificar texto
# ==========================================================

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(X_train, y_train)


# ==========================================================
# 9. EVALUACIÓN DEL MODELO
# Se genera una matriz de confusión y se calcula el accuracy
# ==========================================================

predicciones = modelo.predict(X_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, predicciones)

print("Matriz de confusión:")
print(cm)


from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predicciones)

print("Accuracy del modelo:", accuracy)


# ==========================================================
# 10. PREDICCIÓN EN TIEMPO REAL
# El modelo clasifica un mensaje nuevo indicando
# el nivel de confianza de la predicción.
# ==========================================================

mensaje_nuevo = ["Congratulations you won a free prize click now"]

print("Mensaje a evaluar:", mensaje_nuevo[0])


mensaje_limpio = limpiar_texto(mensaje_nuevo[0])
mensaje_procesado = procesar_texto(mensaje_limpio)

vector = vectorizer.transform([mensaje_procesado])

prediccion = modelo.predict(vector)

probabilidades = modelo.predict_proba(vector)

confianza = max(probabilidades[0]) * 100


print("Predicción:", prediccion[0])
print("Confianza del modelo:", round(confianza, 2), "%")
