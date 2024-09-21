import numpy as np
import matplotlib.pyplot as plt

# Datos
ranks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
dbms = np.array(['Oracle', 'MySQL', 'Microsoft SQL Server', 'PostgreSQL', 
                 'MongoDB', 'Redis', 'Snowflake', 'Elasticsearch', 
                 'IBM Db2', 'SQLite'])
scores_sep_2024 = np.array([1286.59, 1029.49, 807.76, 644.36, 
                             410.24, 149.43, 133.72, 128.79, 
                             123.05, 103.35])
scores_aug_2024 = scores_sep_2024 + np.array([28.11, 2.63, -7.41, 6.97, 
                                               -10.74, -3.28, -2.25, -1.04, 
                                               0.04, -1.44])
scores_sep_2023 = scores_sep_2024 + np.array([45.72, -82.00, -94.45, 23.61, 
                                               -29.18, -14.26, 12.83, -10.20, 
                                               -13.67, -25.85])

# Función para graficar
def plot_scores(scores, title):
    plt.figure(figsize=(10, 6))
    plt.bar(dbms, scores, color='skyblue')
    plt.title(title)
    plt.xlabel('DBMS')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig(f'scores_{title.replace(" ", "_")}.svg', format='svg')
    plt.show()

# Graficar cada tendencia
plot_scores(scores_sep_2024, 'Scores Sep 2024')
plot_scores(scores_aug_2024, 'Scores Aug 2024')
plot_scores(scores_sep_2023, 'Scores Sep 2023')
