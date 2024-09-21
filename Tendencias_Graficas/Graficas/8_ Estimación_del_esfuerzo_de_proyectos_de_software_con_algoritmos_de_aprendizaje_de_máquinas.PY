import numpy as np
import matplotlib.pyplot as plt

# Datos en formato de lista
data2 = [
    [1995, 17, 31, 53],
    [2000, 28, 23, 49],
    [2005, 35, 19, 53],
    [2010, 37, 21, 42],
    [2015, 29, 19, 52]
]

# Convertir datos a un array de numpy
data_array2 = np.array(data2)

# Extraer columnas relevantes
years2 = data_array2[:, 0]  # Años
successes = data_array2[:, 1]  # Éxitos
failures = data_array2[:, 2]  # Fracasos
underestimates = data_array2[:, 3]  # Sub-estimados

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.bar(years2 - 0.2, successes, width=0.2, label='Éxitos', color='green')
plt.bar(years2, failures, width=0.2, label='Fracasos', color='red')
plt.bar(years2 + 0.2, underestimates, width=0.2, label='Sub-estimados', color='yellow')
plt.title('Resultados por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.xticks(years2)
plt.legend()
plt.grid(axis='y')

# Guardar gráfico en formato SVG
plt.tight_layout()
plt.savefig('Resultados_por_Año.svg', format='svg')
plt.show()
