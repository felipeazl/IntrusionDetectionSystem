import matplotlib.pyplot as plt

# Dados de exemplo
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
grupos = ['Grupo 1', 'Grupo 1', 'Grupo 1', 'Grupo 2', 'Grupo 2', 'Grupo 2', 'Grupo 3', 'Grupo 3', 'Grupo 3', 'Grupo 3']

# Criando o gráfico de barras
plt.bar(range(len(valores)), valores)

# Definindo a localização dos ticks no eixo x
posicoes = [0, 3, 6]  # Posições dos grupos
plt.xticks(posicoes)

# Definindo os rótulos dos ticks no eixo x
rotulos = ['Grupo 1', 'Grupo 2', 'Grupo 3']
plt.gca().set_xticklabels(rotulos)

# Exibindo o gráfico
plt.show()
