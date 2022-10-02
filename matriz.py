#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 00:08:25 2022

@author: davideteixeira
"""
import numpy

class Matriz:
    
    def __init__(self, matriz):
        self.matriz = list(matriz)
        self.colunas = len(matriz[0])
        self.linhas = len(matriz)
    
    def soma(self, m2):
        if (m2.linhas == self.linhas) and (m2.colunas == self.colunas):
            matrizsoma = [[0] * self.colunas for i in range (self.linhas)]
            for i in range(self.linhas):
                for j in range(self.colunas):
                    matrizsoma[i][j] = self.matriz[i][j] + m2.matriz[i][j]
            return Matriz(matrizsoma)
        else:
            return 'Impossível fazer o cálculo'

    def multiplica(self, matriz):
        linhas = self.linhas
        colunas = matriz.colunas
        matrizproduto = [[0] * colunas for i in range(linhas)]
        if self.colunas == matriz.linhas:
            for n in range(linhas): #Fixada a linha
                v1 = self.matriz[n] #Vetor da 1.ª linha da 1.ª matriz
                for m in range(matriz.colunas):
                    v2 = []
                    for k in range(matriz.linhas):
                        v2.append(matriz.matriz[k][m]) # n constante, varia o k
                    temp = 0
                    for l in range (len(v2)):
                        temp += v1[l] * v2[l]
                    matrizproduto[n][m] = temp
            return Matriz(matrizproduto)
        else:
            return 'Impossível fazer o cálculo'
    
    def transposta(self):
        transposta = [[0] * self.linhas for i in range (self.colunas)]
        for i in range(self.colunas):
            for j in range(self.linhas):
                transposta[i][j] = self.matriz[j][i]
        return Matriz(transposta)
    
    def maximo(self):
        maximo = self.matriz[0][0]
        for i in range(self.linhas):
            for j in range(self.colunas):
                k = self.matriz[i][j]
                if k > maximo:
                    maximo = k
        return maximo
      
    def det(self):
        if self.colunas == self.linhas:
            det = numpy.linalg.det(self.matriz)
            return det
        else:
            return 'Impossível fazer o cálculo'
    
    def inversa(self):
            if self.colunas == self.linhas:
                inv = numpy.linalg.inv(self.matriz)
                return Matriz(inv)
            else:
                return 'Impossível fazer o cálculo'
    
        
    def __str__ (self):
        string = ''
        for k in self.matriz:
            string = string + str(k) + '\n'
        return string