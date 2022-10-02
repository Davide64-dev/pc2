#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:31:21 2022

@author: davideteixeira
"""
from analise import Analise

class RSE (Analise):
    
    def __init__(self, numutente, nome):
        self._numutente = numutente
        self._nome = nome
        self.analises = []
    
    @property
    def numutente(self):
        return self._numutente
    
    @property
    def nome(self):
        return self._numutente
    
    def adicionar(self, analise):
        self.analises.append(analise)
    
    def eliminar(self, data, tipo, valor):
        k = Analise(data, tipo, valor)
        if k in self.analises:
            self.analises.remove(k)
        else:
            print('Impossível')
    
    @property
    def mediaanalise(self):
        soma = 0
        for i in range(len(self.analises)):
            soma += self.analises[i].valor
        media = soma / len(self.analises)
        return media