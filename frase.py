#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:54:30 2022

@author: davideteixeira
"""

class Frase:
    
    def __init__(self, frase):
        self._frase = frase
    
    @classmethod
    def from_string(cls, string):
        a = string.split()
        return cls(a)
    
    @property
    def escreve(self):
        string = ''
        for palavra in self._frase:
            string = string + palavra + ' '
        string = string[0:len(string)-1]
        print(string)
    
    def numero(self):
        n = len(self._frase)
        return n
    
    def qualpalavra(self, arg):
        a = self._frase[arg-1]
        return a
    
    def substitui(self, palavravelha, palavranova):
        if palavravelha in self._frase:
            indice = self._frase.index(palavravelha)
            self._frase[indice] = palavranova
        else:
            print('Não é possível substituir porque a palavra a ser substituida não se encontra na frase')
    
    def concatenacao(self, outra):
        nova = self._frase + outra._frase
        return Frase(nova)

    def __str__(self):
        string = ''
        for palavra in self._frase:
            string = string + palavra + ' '
        return string