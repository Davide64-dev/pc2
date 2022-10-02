#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:24:52 2022

@author: davideteixeira
"""
from documento import Documento

class Documentoaval(Documento):
    
    def __init__(self, codigo, dataderececao):
        super().__init__(codigo, dataderececao)
        self.aval = []
    
    def avaliar(self, nota):
        self.aval.append(nota)
    
    def avaliacao(self):
        avaliacao = 0
        for k in self.aval:
            avaliacao += k
        if avaliacao > 9.5:
            return 'Aprovado'
        else:
            return 'Reprovado'
    
    def retirar(self, nome):
        a = self.workflow.index(nome)
        self.workflow.remove(nome)
        removido = self.aval[a]
        self.aval.remove(removido)

    def __str__(self):
        return f'\nCódigo: {self._codigo}\nData de Receção: {self._dataderececao}\nWorkflow: {self.workflow}\nAvaliações: {self.aval}\n'