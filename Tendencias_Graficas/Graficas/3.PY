import numpy as np
import matplotlib.pyplot as plt

# Datos de preocupaciones
concerns = np.array([
    'User data collection', 
    'Skill shifts in the workforce', 
    'Job displacement', 
    'Existential risks', 
    'User accessibility', 
    'Perpetuating bias', 
    'Other'
])

counts = np.array([161, 155, 150, 136, 135, 118, 6])
percent_cases = np.array([44.4, 42.7, 41.3, 37.5, 37.2, 32.5, 1.7])

# Función para graficar las preocupaciones
def plot_concerns():
    plt.figure(figsize=(10, 6))
    plt.barh(concerns, counts, color='salmon')
    plt.title('Preocupaciones en la Fuerza Laboral')
    plt.xlabel('Número de Casos')
    plt.ylabel('Preocupación')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.savefig('preocupaciones_fuerza_laboral.svg', format='svg')
    plt.show()

# Graficar las preocupaciones
plot_concerns()
