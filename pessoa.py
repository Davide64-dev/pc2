#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:14:43 2022

@author: davideteixeira
"""
import datetime as dt

class Pessoa:
    def __init__ (self, nome, datadenascimento):
        self._nome = nome
        self._datadenascimento = dt.date.fromisoformat(datadenascimento)
    
    @property
    def idade (self):
        today = dt.date.today()
        if (today.month, today.day) > (self._datadenascimento.month, self._datadenascimento.day):
            idade = today.year - (self._datadenascimento).year
        else:
            idade = today.year - self._datadenascimento.year - 1
        return idade
    
    @property
    def apelido (self):
        a = self._nome.split()
        apelido = a[len(a)-1]
        return apelido
    
    @property
    def nomeproprio (self):
        a = self._nome.split()
        nomeproprio = a[0]
        return nomeproprio
    
    def __str__(self):
        return f'{self.nomeproprio}, {self.apelido}, {self.idade}'