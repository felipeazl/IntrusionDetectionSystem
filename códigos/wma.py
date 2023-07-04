import json
import datetime
import deteccaoAnomalias

# Abre o arquivo JSON
with open('fullData.json') as arquivo:
    dados = json.load(arquivo)

# função que calcula a WMA de cada lista com 10 elementos e retorna o novo valor
def cal_wma(list_values):
    weighted = [0.018, 0.036, 0.055, 0.073, 0.091, 0.109, 0.127, 0.145, 0.164, 0.182]
    wma = 0
    for i in range(0,10):
        wma = wma + (weighted[i] * list_values[i])
    return wma

#percorre todos os dados em janelas de 10 e armaze o calculo de wma dos dados de cada janela list_wma 
def gera_list_wma():
    # inicia a lista com os 9 primeiros iten, este valor foi obtido a partir do primeiro wam calculado do conjunto
    list_wma = [104976.0,104976.0,104976.0,104976.0,104976.0,104976.0,104976.0,104976.0,104976.0]
    #lista auxiliar utilizada para marcar os 10 elementos da janela atual
    aux_list = []
    for key in dados.keys():
        if len(aux_list) <= 10:
            aux_list.append(int(dados[key]["total_len"]))
            if len(aux_list) == 10:
                #soma = sum(aux_list)
                calculoWma = cal_wma(aux_list)
                list_wma.append(calculoWma)
                aux_list.pop(0)
    return list_wma
   
#função que organiza e retorna os dados para a geração do grafico
def gera_xy():
    list_timestamp = []
    list_len = []
    list_wma = gera_list_wma()
    #formato = "%Y-%m-%d %H:%M:%S"
    for key in dados.keys():
        dt = datetime.datetime.fromtimestamp(int(key))
        list_timestamp.append(dt)
        list_len.append(dados[key]["total_len"])
    listaAnomalias = deteccaoAnomalias.anomalia(list_len, list_wma)
    return list_timestamp, list_len, list_wma, listaAnomalias

