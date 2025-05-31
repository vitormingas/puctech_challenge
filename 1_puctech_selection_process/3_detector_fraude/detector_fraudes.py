# detector_fraudes.py

# Mini Detector de Fraudes em Transações
# vitormingas - 2025

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Carregar o dataset real (creditcard.csv)
df = pd.read_csv("creditcard.csv")

# 2. Separar os dados (X = features, y = rótulos)
X = df.drop("Class", axis=1)  # todas as colunas exceto 'Class'
y = df["Class"]               # 0 = normal, 1 = fraude

# 3. Dividir os dados entre treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Treinar modelo de classificação
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 5. Fazer previsões
y_pred = modelo.predict(X_test)

# 6. Avaliação com métricas de desempenho
print("📊 Relatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=["Normal", "Fraude"]))