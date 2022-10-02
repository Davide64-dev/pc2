#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:27:45 2022

@author: davideteixeira
"""
import datetime as dt

class Analise:
    
    def __init__(self, data, tipo, valor):
        self._data = dt.date(int(data[0:4]), int(data[5:7]), int(data[8:9]))
        self._tipo = str(tipo)
        self._valor = float(valor)
    
    @property
    def data(self):
        return self._data
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def valor(self):
        return self._valor
    
    