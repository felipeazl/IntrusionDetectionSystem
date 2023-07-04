import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def geraGrafico(dados, NMSE, MAPE):
    fig, graph = plt.subplots()

    graph.plot(dados[0], dados[1], label='Medições', zorder=1) #eixo x = timestamp e eixo y = medições padrão
    graph.plot(dados[0], dados[2], label='WMA', zorder=1) #eixo x = timestamp e eixo y = wma com base nas ultimas 10 medições anteriores

    graph.legend()
    graph.set_xlabel('Timestamp')
    graph.set_ylabel('Valores')
    
    x_pontos = []
    y_pontos = []
    for i in dados[3]:
        x_pontos.append(dados[0][i])
        y_pontos.append(dados[1][i])

    plt.scatter(x_pontos, y_pontos, color='red', label='Pontos', zorder=2)

    total_anomalias = len(dados[3])
    graph.text(0.5, 0.95, f'NMSE = {NMSE}\nMAPE = {MAPE}%\nTotal Anomalias = {total_anomalias}', horizontalalignment='center', verticalalignment='center', transform=graph.transAxes)

    plt.savefig('grafico.png')
    plt.show() #gera o grafico
