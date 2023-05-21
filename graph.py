import matplotlib.pyplot as plt
import wma as wma

dados = wma.gera_xy() #chama a função do arquivo wma que gera e retorna os dados para o grafico

# fig, graph = plt.subplots()

# graph.plot(dados[0], dados[1], label='Medições') #eixo x = timestamp e eixo y = medições padrão
# graph.plot(dados[0], dados[2], label='WMA') #eixo x = timestamp e eixo y = wma com base nas ultimas 10 medições anteriores

# graph.set_xlabel('Timestamp')
# graph.set_ylabel('Valores')

# plt.show() #gera o grafico

plt.figure(layout='constrained')
plt.plot(dados[0], dados[1], label='Marcações')
plt.plot(dados[0], dados[2], label='WMA')
plt.xlabel("Timestamp")
plt.ylabel("valores")
plt.xticks(rotation=90)
plt.title("INCLUIR TÍTULO")
plt.legend('legenda de testes');
plt.show()