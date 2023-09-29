import numpy as np
import requests
from datasets import load_dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]
ages = data['age']
ages = np.array(ages) # Conertir de lista a Numpy array.
m_ages = np.mean(ages)
print("El promedio de las edades es: " + str(m_ages))