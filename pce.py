#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 19:47:16 2022

@author: davideteixeira
"""
from analise import Analise
from rse import RSE

class PCE(RSE):
    
    def __init__ (self, numutente, nome, medfamilia):
        super().__init__(numutente, nome)
        self.medfamilia = medfamilia
        self.analises = dict()
    
    def adicionar(self, analise, medico):
        self.analises[analise] = medico
    
    def eliminar(self, data, tipo, valor):
        k = Analise(data, tipo, valor)
        if k in self.analises:
            self.analises.pop(k)
        else:
            print('Impossível')
    
    def mediaanalise(self, k):
        a = list(self.analises.keys())
        soma = 0
        i = 0
        if k == 1:
            for i in range(len(a)):
                temporario = a[i]
                if temporario._tipo == 'Sangue':
                    soma += temporario._valor
                    i = i + 1
                else:
                    continue
            media = soma / i
            return media
        elif k == 0:
            matriz = []
            tipos = []
            for i in range(len(a)):
                tipos.append(a[i].tipo)
            temp = set(tipos)
            tipos = list(temp)
            for i in range(len(tipos)):
                soma = 0
                k = 0
                temp1 = tipos[i]
                for i in range(len(a)):
                    if a[i].tipo == temp1:
                        soma += a[i].valor
                        k += 1
                    else:
                        continue
                media = soma / k
                temp2 = [temp1,media]
                matriz.append(temp2)
            return matriz