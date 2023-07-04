import statistics

# peguntas
# vamos calcular o desvio padrão de qual lista??
# da diferença de um ponto para o outro?
# da lista normal 
# da lista de wma


def anomalia(listaReal, listaWMA):
    posicaoAnomalia = []
    desvioPadrao = statistics.stdev(listaWMA)*3

    for i in range(0, len(listaReal)):
        if listaReal[i] > listaWMA[i]:
            dif = listaReal[i] - listaWMA[i]
        else:
            dif = listaWMA[i] - listaReal[i]
        
        if dif > desvioPadrao:
            posicaoAnomalia.append(i)
            # print("anomalia")
        # else:
            # print("normal")
    return posicaoAnomalia


# def anomaliaSimples(valorReal, valorEsperado, listaWMA):
#     desvioPadrao = statistics.stdev(listaWMA)*3
#     if valorReal > valorEsperado:
#         dif = valorReal - valorEsperado
#     else:
#         dif = valorEsperado - valorReal
    
#     if dif > desvioPadrao:
#         print("anomalia")
#     else:
#         print("normal")