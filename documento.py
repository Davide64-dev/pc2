#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 08:06:16 2022

@author: davideteixeira
"""
import datetime as dt

class Documento:
    
    def __init__(self, codigo, dataderececao):
        self._codigo = codigo
        self._dataderececao = dt.date(int(dataderececao[0:4]), int(dataderececao[5:7]), int(dataderececao[8:10]))
        self.workflow = []
    
    def adicionar(self, nome):
        self.workflow.append(nome)
    
    def retirar(self, nome):
        self.workflow.remove(nome)
    
    def __str__(self):
        return f'\nCódigo: {self._codigo}\nData de Receção: {self._dataderececao}\nWorkflow: {self.workflow}'