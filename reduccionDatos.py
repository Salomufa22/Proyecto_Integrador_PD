import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import plotly.express as px

data = pd.read_csv("cleanData.csv")

deathEvent = data['DEATH_EVENT']
data = data.drop(columns=['DEATH_EVENT', 'Age_Category'])

dataArray = data.values
deathEventArray = deathEvent.values

X_embedded = TSNE(
    n_components=3,
    learning_rate='auto',
    init='random',
    perplexity=3
).fit_transform(dataArray)

# Crear un DataFrame con los resultados y la etiqueta de clase
df_embedded = pd.DataFrame(data=X_embedded, columns=['Dimension_1', 'Dimension_2', 'Dimension_3'])
df_embedded['Death_Event'] = deathEventArray

# Crear el gráfico de dispersión 3D con Plotly
fig = px.scatter_3d(
    df_embedded, 
    x='Dimension_1', 
    y='Dimension_2', 
    z='Dimension_3', 
    color='Death_Event',
    labels={'Death_Event': 'Death Event'},
    title='Gráfico de Dispersión 3D con t-SNE'
)

# Mostrar el gráfico
fig.show()

