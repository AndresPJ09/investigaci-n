import numpy as np
import matplotlib.pyplot as plt

# Datos en formato de lista
data = [
    ['Python', 1],
    ['Java', 0.4855],
    ['JavaScript', 0.4451],
    ['C++', 0.3749],
    ['TypeScript', 0.2497],
    ['SQL', 0.2258],
    ['C#', 0.2089],
    ['Go', 0.2052],
    ['C', 0.1989],
    ['HTML', 0.1817],
    ['Rust', 0.1506],
    ['Mathematica', 0.1275],
    ['PHP', 0.1196],
    ['Shell', 0.117],
    ['Lua', 0.1041],
    ['SAS', 0.0855]
]

# Convertir a un array de numpy
languages = np.array([item[0] for item in data])  # Lenguajes
popularity = np.array([item[1] for item in data])  # Popularidad

# Graficar
plt.figure(figsize=(10, 6))
plt.barh(languages, popularity, color='skyblue')
plt.xlabel('Popularidad')
plt.title('Popularidad de Lenguajes de Programación')
plt.grid(axis='x')

plt.savefig('The_Top_Programming_Languages_2024_Typescript_and_Rust_are_among_the_rising_stars.svg', format='svg')
# Mostrar la gráfica
plt.show()
