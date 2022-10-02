#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:44:49 2022

@author: davideteixeira
"""

class Texto:
    
    def __init__(self, n):
        self.n = n
        self.linhas = []
    
    def adicionar(self, texto):
        if len(self.linhas) < self.n:
            self.linhas.append(texto)
        else:
            print('Número insuficiente de linhas')
    
    def retirar(self, indice):
        self.linhas.pop(indice-1)
    
    def escrever(self, texto):
        fileh = open(texto, 'wt')
        for k in self.linhas:
            fileh.write(k+'\n')
        fileh.close()
    
    def ler(self, texto):
        fileh = open(texto, 'rt')
        for line in fileh:
            line = line[0:len(line)-1]
            self.linhas.append(line)
        fileh.close
    
    def procurar(self, palavra):
        i = 0
        for line in self.linhas:
            if palavra in line:
                i +=1
        return i
    
    def __str__(self):
        string = ''
        for i in self.linhas:
            string += i + '\n'
        return string