import wma
import metricas
import graph

dados = wma.gera_xy() #chama a função do arquivo wma que gera e retorna os dados para o grafico
NMSE = metricas.cal_nmse()
MAPE = metricas.cal_mape()

graph.geraGrafico(dados, NMSE, MAPE)