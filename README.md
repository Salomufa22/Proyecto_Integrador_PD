# Proyecto_Integrador_PD Análisis de Datos y Machine Learning

El proyecto de este curso tiene como objetivo principal analizar un conjunto de datos de registros médicos de pacientes que padecieron insuficiencia cardíaca durante un período de seguimiento. Para lograr esto, se llevarán a cabo las siguientes etapas:

## Instalación de la librería 'datasets' de Huggingface

Para comenzar, es necesario instalar la librería 'datasets' de Huggingface. Puedes hacerlo utilizando el siguiente comando:
`pip install datasets`

## Conjunto de Datos
El conjunto de datos que vamos a utilizar se enfoca en pacientes con insuficiencia cardíaca y contiene 13 características clínicas. Estas características son las siguientes:
* Edad: edad del paciente en años.
* Anemia: presencia o ausencia de disminución de glóbulos rojos o hemoglobina (booleano).
* Presión arterial alta: indicación de si el paciente tiene hipertensión (booleano).
* Creatinina fosfoquinasa (CPK): nivel de la enzima CPK en la sangre en mcg/L.
* Diabetes: indicación de si el paciente tiene diabetes (booleano).
* Fracción de eyección: porcentaje de sangre que sale del corazón en cada contracción (porcentaje).
* Plaquetas: cantidad de plaquetas en la sangre en kiloplaquetas/mL.
* Sexo: género del paciente (binario).
* Creatinina sérica: nivel de creatinina sérica en la sangre en mg/dL.
* Sodio sérico: nivel de sodio sérico en la sangre en mEq/L.
* Fumar: indicación de si el paciente fuma o no (booleano).
* Tiempo: período de seguimiento en días.
* (Objetivo) Evento de fallecimiento: indicación de si el paciente falleció durante el período de seguimiento (booleano).

## Descargar el Dataset
Podemos descargarlo usando la librería instalada debemos ejecutar el siguiente framento de código:
```
from datasets import load_dataset
dataset = load_dataset("mstz/heart_failure")
```
El dataset contiene una estructura similar a un diccionario con particiones de datos y características, debido a que este dataset sólo contiene una partición llamada train, accedemos a todos los registos indexando por esa partición
`data = dataset["train"]`



¡Gracias por tu interés en el proyecto! Mantente atento a las actualizaciones a medida que continúo construyendo la base de datos.


## Contacto
Realizado por: Laura Salomé Murcia Farfán
Cohorte 38 ADA SCHOOL
Si tienes alguna pregunta o comentario, no dudes en ponerte en contacto conmigo a través de los problemas (issues) del repositorio.
