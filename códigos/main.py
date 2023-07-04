import wma
import metricas
import graph
import json

week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'fullData']

for day in week_days:
    with open(f'./json/{day}.json', 'r') as f:
        jsonData = json.load(f)

    dados = wma.gera_xy(jsonData) #chama a função do arquivo wma que gera e retorna os dados para o grafico
    NMSE = metricas.cal_nmse(jsonData)
    MAPE = metricas.cal_mape(jsonData)

    graph.geraGrafico(dados, NMSE, MAPE, day)