#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:08:46 2022

@author: davideteixeira
"""

class transporte:
    def __init__(self, codigo, capacidade, numparagens, paragens):
        self._codigo = int(codigo)
        self._capacidade = int(capacidade)
        self._numparagens = int(numparagens)
        self._paragens = paragens
        
    distancias = []
    
    def distancias(self, distancias):
        transporte.distancias = distancias
    
    def distancia(self, i, j):
        distancia = int(self.distancias[i][j])
        return distancia

    def associar(self, transporte2):
        if self.paragens[self.numparagens-1] == transporte2.paragens[0]:
            codigo = self._codigo + transporte2._codigo
            capacidade = self._capacidade
            numparagens = self.numparagens + transporte2.numparagens - 1
            paragens = self.paragens + transporte2.paragens[1:]
            transporte3 = transporte(codigo, capacidade, numparagens, paragens)
            return transporte3
        else:
            pass
    
    def tempo(self, i, j):
        distancia = self.distancia(i, j)
        tempo = distancia / 40
        return tempo
    
    def __str__(self):
        return f'\nCódigo: {self._codigo}\nCapacidade: {self._capacidade}\nNúmero de Paragens: {self.numparagens}\nParagens: {self.paragens}\n'