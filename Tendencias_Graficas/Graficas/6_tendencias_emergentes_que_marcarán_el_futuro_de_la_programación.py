import numpy as np
import matplotlib.pyplot as plt

# Datos en formato de lista
data = [
    ['Python', 100],
    ['Java', 70],
    ['Spring', 60],
    ['AWS', 50],
    ['Kubernetes', 40],
    ['Angular', 35],
    ['Docker', 35],
    ['JavaScript', 30],
    ['Spark', 25],
    ['Machine Learning', 25],
    ['React', 20],
    ['Go', 15],
    ['Microservices', 10],
    ['Blockchain', 10]
]

# Convertir datos a un array de numpy
data_array = np.array(data)

# Extraer columnas relevantes
search_terms = data_array[:, 0]  # Términos de búsqueda
frequencies = data_array[:, 1].astype(int)  # Frecuencias

# Graficar frecuencias
plt.figure(figsize=(10, 6))
plt.barh(search_terms, frequencies, color='skyblue')
plt.title('Frecuencia de Términos de Búsqueda (Normalizado)')
plt.xlabel('Frecuencia (normalizada)')
plt.ylabel('Términos de búsqueda')
plt.grid(axis='x')

# Guardar gráfico en formato SVG
plt.tight_layout()
plt.savefig('Search_Terms_Frequency.svg', format='svg')
plt.show()
