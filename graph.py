import matplotlib.pyplot as plt
import wma as wma
import matplotlib.dates as mdates
import metricas

dados = wma.gera_xy() #chama a função do arquivo wma que gera e retorna os dados para o grafico
NMSE = metricas.cal_nmse()
MAPE = metricas.cal_mape()

fig, graph = plt.subplots()

graph.plot(dados[0], dados[1], label='Medições') #eixo x = timestamp e eixo y = medições padrão
graph.plot(dados[0], dados[2], label='WMA') #eixo x = timestamp e eixo y = wma com base nas ultimas 10 medições anteriores

graph.legend()
graph.set_xlabel('Timestamp')
graph.set_ylabel('Valores')

graph.text(0.5, 0.95, f'NMSE = {NMSE}\nMAPE = {MAPE}%', horizontalalignment='center', verticalalignment='center', transform=graph.transAxes)

plt.show() #gera o grafico

# plt.figure(layout='constrained')
# plt.plot(dados[0], dados[1], label="Marcações")
# plt.plot(dados[0], dados[2], label="WMA")
# plt.xlabel("Timestamp")
# plt.ylabel("valores")
# plt.title("INCLUIR TÍTULO")
# plt.legend("legenda de testes");

# plt.show()