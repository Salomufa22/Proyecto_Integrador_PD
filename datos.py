from datasets import load_dataset
import numpy as np
import pandas as pd

#Parte I
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
ages = data['age']
ages = np.array(ages) # Convertir de lista a Numpy array.
m_ages = np.mean(ages)
print("El promedio de las edades es: " + str(m_ages))

#Parte II
data = pd.DataFrame(data)

alive = data[data['is_dead']==0]
mean_ages_alive = alive['age'].mean()
print("El promedio de las edades de los vivos es: " + str(mean_ages_alive))

dead = data[data['is_dead']==1]
mean_ages_dead = dead['age'].mean()
print("El promedio de las edades de los muertos es: " + str(mean_ages_dead))


#Parte III
# Verificar tipos de datos en cada columna
data_types = data.dtypes
print("\nTipos de datos en cada columna:")
print(data_types)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
smokers = data[data['is_smoker']]
smoker_counts = smokers['is_male'].value_counts()
smoker_counts.index = ['Smoker Males', 'Smoker Females']
print("\nCantidad de hombres fumadores vs mujeres fumadoras:")
print(smoker_counts)

