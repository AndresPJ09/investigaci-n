import matplotlib.pyplot as plt

# Datos ficticios
bad_smells = ['Duplicación de Código', 'Clases Grandes', 'Métodos Largos']
percentages = [50, 30, 20]
colors = ['#ffcc99', '#ff6666', '#99cc99']

plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=bad_smells, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Proporción de Bad Smells en el Patrón MVC - Artículo 20')
plt.axis('equal')
plt.savefig('grafico_circular_articulo_20.png')
plt.show()
