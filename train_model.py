import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Cargar el dataset
df = pd.read_csv('color_palettes.csv')

# Preprocesamiento del texto
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['color_palette']

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=80)

# Entrenamiento del modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar el vectorizador y el modelo RandomForest
joblib.dump(vectorizer, 'vectorizer_rf.pkl')
joblib.dump(model, 'model_rf.pkl')
