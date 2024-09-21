import numpy as np
import matplotlib.pyplot as plt

# Datos en formato de lista
data_languages = [
    ['Python', 25.95],
    ['Java', 21.42],
    ['JavaScript', 8.26],
    ['C#', 7.62],
    ['PHP', 7.37],
    ['C++', 6.31],
    ['R', 4.04],
    ['Objective-C', 3.15],
    ['Swift', 2.56],
    ['Matlab', 2.04],
    ['TypeScript', 1.57],
    ['Ruby', 1.53]
]

# Convertir datos a un array de numpy
data_array_languages = np.array(data_languages)

# Extraer columnas relevantes
programming_languages = data_array_languages[:, 0]  # Lenguajes
percentages = data_array_languages[:, 1].astype(float)  # Porcentajes

# Graficar porcentajes
plt.figure(figsize=(10, 6))
plt.barh(programming_languages, percentages, color='skyblue')
plt.title('Porcentaje de Lenguajes de Programación')
plt.xlabel('Porcentaje (%)')
plt.ylabel('Lenguaje')
plt.grid(axis='x')

# Guardar gráfico en formato SVG
plt.tight_layout()
plt.savefig('Porcentaje_Lenguajes_Programacion.svg', format='svg')
plt.show()
