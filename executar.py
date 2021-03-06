from Objetos import Kmeans, BancoDeDados
from Animacoes import rodar_animacao_2d
import sys
import copy


resultados = []
banco = BancoDeDados()


def iterar(kmeans):
    for iteracao in range(kmeans.iteracoes):
        kmeans.iteracoes_feitas += 1
        kmeans.classifica_amostras()
        kmeans.move_centroides()
        if not kmeans.houve_movimentacao:
            kmeans.calcula_distancia_total()
            return kmeans
    kmeans.calcula_distancia_total()
    return kmeans


def executar_k_means(clusters=4, movimento_minimo=0.0000001, execucoes=20, iteracoes=1000, animacao=False, velocidade_animacao=500):
    if animacao:
        kmeans = Kmeans(clusters, iteracoes, movimento_minimo, banco)
        kmeans.gera_posicoes_aleatorias()
        rodar_animacao_2d(kmeans, velocidade_animacao)
    else:
        menor_distancia_total = sys.maxsize
        melhor_execucao = 0
        for execucao in range(execucoes):
            kmeans = Kmeans(clusters, iteracoes, movimento_minimo, banco)
            kmeans.gera_posicoes_aleatorias()
            resultado = copy.deepcopy(iterar(kmeans))
            resultados.append(resultado)
            if resultado.distancia_total < menor_distancia_total:
                menor_distancia_total = resultado.distancia_total
                melhor_execucao = execucao

        for resultado in range(execucoes):
            print("Resultado %d" % (resultado+1))
            print("Iteracoes necessárias: %d" % resultados[resultado].iteracoes_feitas)
            print("Distância total: %f \n" % resultados[resultado].distancia_total)

        print("Melhor distância: %f" % menor_distancia_total)
        print("Na execução: %d" % melhor_execucao)
        resultados[melhor_execucao].plotar_mapa()

if __name__ == '__main__':
    executar_k_means()
