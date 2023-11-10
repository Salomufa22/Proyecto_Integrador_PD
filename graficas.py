import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("cleanData.csv")

#Parte 7
##########################
# Distribución de edades #
##########################
plt.figure(figsize=(6, 5))
plt.hist(data['Age_Category'])
plt.title('Distribución de edades')
plt.xlabel('Edades')
plt.ylabel('Número de personas por edad')
#plt.show()

################################
# Histograma Agrupado por Sexo #
################################
hombres = data[['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']][data['sex'] == 1.0]
mujeres = data[['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']][data['sex'] == 0.0]

cantHombres = [hombres['anaemia'][hombres['anaemia'] == 1].count(), 
               hombres['diabetes'][hombres['diabetes'] == 1].count(),
               hombres['smoking'][hombres['smoking'] == 1].count(),
               hombres['DEATH_EVENT'][hombres['DEATH_EVENT'] == 1].count()]

cantMujeres = [mujeres['anaemia'][mujeres['anaemia'] == 1].count(), 
               mujeres['diabetes'][mujeres['diabetes'] == 1].count(),
               mujeres['smoking'][mujeres['smoking'] == 1].count(),
               mujeres['DEATH_EVENT'][mujeres['DEATH_EVENT'] == 1].count()]

categoria = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']

x = np.arange(len(categoria))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, cantHombres, width, label='Hombres', color ="blue")
rects2 = ax.bar(x + width/2, cantMujeres, width, label='Mujeres', color ="red")

ax.set_xlabel('Categorías')
ax.set_ylabel('Cantidad')
ax.set_title('Histograma Agrupado por Sexo')
ax.set_xticks(x)
ax.set_xticklabels(categoria)
ax.legend()

fig.tight_layout()

#plt.show()


# Parte 8
datosSeleccionados = data[['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']]

cantSi = [datosSeleccionados['anaemia'][datosSeleccionados['anaemia'] == 1].count(), 
               datosSeleccionados['diabetes'][datosSeleccionados['diabetes'] == 1].count(),
               datosSeleccionados['smoking'][datosSeleccionados['smoking'] == 1].count(),
               datosSeleccionados['DEATH_EVENT'][datosSeleccionados['DEATH_EVENT'] == 1].count()]

cantNo = [datosSeleccionados['anaemia'][datosSeleccionados['anaemia'] == 0].count(), 
               datosSeleccionados['diabetes'][datosSeleccionados['diabetes'] == 0].count(),
               datosSeleccionados['smoking'][datosSeleccionados['smoking'] == 0].count(),
               datosSeleccionados['DEATH_EVENT'][datosSeleccionados['DEATH_EVENT'] == 0].count()]

categoria = ['Anémicos', 'Diabéticos', 'Fumadores', 'Muertos']


fig, axes = plt.subplots(2, 2)

axes = axes.flatten()

etiquetas = ['Si', 'No']
titulos = ['']
for i in range(4):
    axes[i].pie([cantSi[i], cantNo[i]], labels = etiquetas, autopct='%1.1f%%')
    axes[i].set_title(categoria[i])
plt.tight_layout()
plt.show()