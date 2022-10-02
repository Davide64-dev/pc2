#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:10:16 2022

@author: davideteixeira
"""
from transporte import transporte

class Veiculo (transporte):
    
    def __init__(self, codigo, capacidade, numparagens, paragens, funcionalidade, velocidademedia):
        super().__init__(codigo, capacidade, numparagens, paragens)
        self.funcionalidade = funcionalidade
        self._velocidademedia = velocidademedia
    
    def tempo(self, i, j):
        tempo = self.distancia(i,j) / self._velocidademedia
        return tempo
    
    def tempodefinido(self, i, j, velocidade):
        distancia = self.distancia(i, j)
        tempo = distancia / velocidade
        return tempo
    
    def __str__(self):
        return f'Código: {self._codigo}\nCapacidade: {self._capacidade}\nNúmero de Paragens: {self.numparagens}\nParagens: {self.paragens}\nFuncionalidade: {self.funcionalidade}\nVelocidade Média: {self._velocidademedia} km/h\n'