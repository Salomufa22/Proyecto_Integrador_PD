import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv("cleanData.csv")

age = data['age']
data = data.drop(columns=['DEATH_EVENT', 'age', 'Age_Category'])

regresion = LinearRegression()
regresion.fit(data, age)
y_pred = regresion.predict(data)
mse = mean_squared_error(age, y_pred)

print(f"Edades reales: \n{age}\n")
print(f"Edades predichas: \n{y_pred}\n")
print(f"Comparación: \n{age - y_pred}\n")
print(f"Mean Squared Error: \n{mse}\n")