import math
import sys
from Objetos.centroide import Centroide
import numpy as np
import matplotlib.pyplot as plt


class Kmeans:
    def __init__(self, numero_centroides, banco):
        self.numero_centroides = numero_centroides
        self.centroides = [Centroide(i) for i in range(numero_centroides)]
        self.banco = banco

    def gera_posicoes_aleatorias(self):
        for i in range(4):
            if i == 3:
                self.centroides[i].posicao = [-1.3820529975920155, -48.477489181332565]
                self.centroides[i].fixo = True
            else:
                self.centroides[i].gera_posicao_aleatoria(self.banco)

    def classifica_amostras(self):
        for bairro in self.banco.bairros:
            menor_distancia = sys.maxsize
            for centroide in self.centroides:
                distancia_atual = math.sqrt((self.banco.bairros[bairro]['coordenadas'][0] - centroide.posicao[0]) ** 2 + (self.banco.bairros[bairro]['coordenadas'][1] - centroide.posicao[1]) ** 2)
                if distancia_atual <= menor_distancia:
                    menor_distancia = distancia_atual
                    self.banco.bairros[bairro]['centroide'] = centroide.nome

            for centroide in range(self.numero_centroides):
                if self.banco.bairros[bairro]['centroide'] == centroide:
                    self.centroides[centroide].bairros.append(bairro)
                    self.centroides[centroide].num_bairros += 1

    def move_centroides(self):
        for centroide in range(self.numero_centroides):
            if not self.centroides[centroide].fixo:
                nova_posicao = np.zeros(self.banco.dimensoes)
                numero_bairros = self.centroides[centroide].num_bairros
                for bairro in self.centroides[centroide].bairros:
                    for componente in range(self.banco.dimensoes):
                        nova_posicao[componente] += self.banco.bairros[bairro]['coordenadas'][componente]
                for componente in range(self.banco.dimensoes):
                    self.centroides[centroide].posicao[componente] = np.copy(nova_posicao[componente]/numero_bairros)

    def plota_mapa(self):
        x0 = []
        y0 = []
        x1 = []
        y1 = []
        x2 = []
        y2 = []
        x3 = []
        y3 = []
        xcentroide = []
        ycentroide = []

        for centroide in range(self.numero_centroides):
            xcentroide.append(self.centroides[centroide].posicao[1])
            ycentroide.append(self.centroides[centroide].posicao[0])

        for bairro in self.banco.bairros:
            if self.banco.bairros[bairro]['centroide'] == 0:
                x0.append(self.banco.bairros[bairro]['coordenadas'][1])
                y0.append(self.banco.bairros[bairro]['coordenadas'][0])
            elif self.banco.bairros[bairro]['centroide'] == 1:
                x1.append(self.banco.bairros[bairro]['coordenadas'][1])
                y1.append(self.banco.bairros[bairro]['coordenadas'][0])
            elif self.banco.bairros[bairro]['centroide'] == 2:
                x2.append(self.banco.bairros[bairro]['coordenadas'][1])
                y2.append(self.banco.bairros[bairro]['coordenadas'][0])
            elif self.banco.bairros[bairro]['centroide'] == 3:
                x3.append(self.banco.bairros[bairro]['coordenadas'][1])
                y3.append(self.banco.bairros[bairro]['coordenadas'][0])

        plt.plot(xcentroide[0], ycentroide[0], 'go', xcentroide[1], ycentroide[1], 'bo', xcentroide[2], ycentroide[2],
                 'yo', xcentroide[3], ycentroide[3], 'ro', x0, y0, 'g^', x1, y1, 'b^', x2, y2, 'y^', x3, y3, 'r^')
        plt.show()
