#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 21:19:55 2022

@author: davideteixeira
"""

class Atividade:
    
    def __init__(self, descricao, responsavel, duracao):
        self._descricao = str(descricao)
        self._responsavel = str(responsavel)
        self._duracao = int(duracao)
    
    @property
    def descricao(self):
        return self._descricao
    
    @property
    def responsavel(self):
        return self._responsavel
    
    @property
    def duracao(self):
        return self._duracao