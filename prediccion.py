import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Parte 11: Clasificación 1
print("#########################")
print("Parte 11: Clasificación 1")
print("#########################")

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
    criterion='gini',  # Otra opción: 'entropy'
    max_depth=10,  # Profundidad máxima del árbol
    min_samples_split=2,  # Número mínimo de muestras requeridas para dividir un nodo interno
    min_samples_leaf=1,  # Número mínimo de muestras requeridas en un nodo hoja
    random_state=42  # Semilla para reproducibilidad
)
tree2.fit(xTrain, yTrain)
y_predict2 = tree2.predict(xTest)
accuracy2 = accuracy_score(yTest, y_predict2)
print(f"\nAccuracy Score del Árbol Ajustado entrenado: {accuracy2}\n")


# Parte 12: Clasificación 2
print("#########################")
print("Parte 12: Clasificación 2")
print("#########################")

# 1. Ajusta un random forest
forest = RandomForestClassifier()
forest.fit(xTrain, yTrain)

# 2. Calcula su matriz de confusión
y_predict_forest = forest.predict(xTest)
accuracy = accuracy_score(yTest, y_predict_forest)
confMatrix = confusion_matrix(yTest, y_predict_forest)

print(f"Confussion Matrix de Random Forest: \n{confMatrix}\n")

# 3. Calcula F1-Score y compara con el accuracy
f1Score = f1_score(yTest, y_predict_forest, average=None)

print(f"Accuracy de Random Forest: \n{accuracy}\n")
print(f"F1 Score de Random Forest: \n{f1Score}\n")
print(f"Comparación: \n{accuracy - f1Score}\n")

# Crees que el accuracy captura completamente el rendimiento del modelo en este caso o no es suficiente?

# 4. Trata de cambiar los valores de los parámetros del random forest para conseguir el mejor resultado que puedas.
forest2 = RandomForestClassifier(
    n_estimators=150,
    criterion='entropy',
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)

forest2.fit(xTrain, yTrain)

y_predict_forest2 = forest2.predict(xTest)
accuracy2 = accuracy_score(yTest, y_predict_forest2)
confMatrix2 = confusion_matrix(yTest, y_predict_forest2)

print(f"Confussion Matrix de Random Forest ajustado: \n{confMatrix2}\n")

f1Score2 = f1_score(yTest, y_predict_forest2, average=None)

print(f"Accuracy de Random Forest ajustado: \n{accuracy2}\n")
print(f"F1 Score de Random Forest ajustado: \n{f1Score2}\n")
print(f"Comparación ajustado: \n{accuracy2 - f1Score2}\n")