import numpy as np
import matplotlib.pyplot as plt

# Datos en formato de lista
data1 = [
    [2017, 1, 2],
    [2018, 1, 3],
    [2019, 2, 4],
    [2020, 3, 5],
    [2021, 5, 8],
    [2022, 7, 10],
    [2023, 10, 15],
    [2024, 15, 30],
    [2025, 25, 45]
]

# Convertir datos a un array de numpy
data_array1 = np.array(data1)

# Extraer columnas relevantes
years1 = data_array1[:, 0]  # Años
low_values = data_array1[:, 1]  # Valores bajos
high_values = data_array1[:, 2]  # Valores altos

# Graficar valores
plt.figure(figsize=(10, 6))
plt.plot(years1, low_values, marker='o', color='blue', label='Bajo ($Billions)')
plt.plot(years1, high_values, marker='o', color='orange', label='Alto ($Billions)')
plt.title('Proyección de Valores (2017-2025)')
plt.xlabel('Año')
plt.ylabel('Valor ($Billions)')
plt.legend()
plt.grid()

# Guardar gráfico en formato SVG
plt.tight_layout()
plt.savefig('Proyeccion_Valores.svg', format='svg')
plt.show()
