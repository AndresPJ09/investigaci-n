import numpy as np
import matplotlib.pyplot as plt

# Datos en formato de lista
data_solutions = [
    ['Automatización del Marketing', 16],
    ['Herramientas de análisis para Big Data y sistemas predictivos', 22],
    ['Formación de los empleados', 51],
    ['Cloud', 64],
    ['Ciberseguridad', 66],
    ['Database', 70],
    ['Equipamiento e infraestructura', 81]
]

# Convertir datos a un array de numpy
data_array_solutions = np.array(data_solutions)

# Extraer columnas relevantes
solutions = data_array_solutions[:, 0]  # Soluciones
percentages_solutions = data_array_solutions[:, 1].astype(float)  # Porcentajes

# Graficar porcentajes
plt.figure(figsize=(10, 6))
plt.barh(solutions, percentages_solutions, color='lightgreen')
plt.title('Porcentaje de Soluciones')
plt.xlabel('Porcentaje (%)')
plt.ylabel('Solución')
plt.grid(axis='x')

# Guardar gráfico en formato SVG
plt.tight_layout()
plt.savefig('Porcentaje_Soluciones.svg', format='svg')
plt.show()
