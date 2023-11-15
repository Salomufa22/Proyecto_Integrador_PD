import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("cleanData.csv")

# 1. Grafica la distribución de clases (con la librería de tu preferencia) para analizar si este dataset está balanceado o no
data = data.drop(['Age_Category'], axis=1)
data.hist(bins=20, figsize=(15, 10))
plt.tight_layout()
plt.show()

X = data.drop(['DEATH_EVENT'], axis=1)
y = data['DEATH_EVENT']

# 2. Realiza la partición del dataset en conjunto de entrenamiento y test
xTrain, xTest, yTrain, yTest = train_test_split(X, y, stratify=y)

# 3. Ajusta un árbol de decisión y calcula el accuracy sobre el conjunto de test.
tree = DecisionTreeClassifier()
tree.fit(xTrain, yTrain)
y_predict = tree.predict(xTest)
accuracy = accuracy_score(yTest, y_predict)
print(f"\nAccuracy Score del Arbol entrenado: {accuracy}\n")

# 4. Trata de mover los valores de los parámetros para lograr la mayor accuracy que puedas.
tree2 = DecisionTreeClassifier(
    criterion='gini',  
    max_depth=10,  
    min_samples_split=2,  
    min_samples_leaf=1,  
    random_state=42  
)
tree2.fit(xTrain, yTrain)
y_predict2 = tree2.predict(xTest)
accuracy2 = accuracy_score(yTest, y_predict2)
print(f"\nAccuracy Score del Árbol Ajustado entrenado: {accuracy2}\n")