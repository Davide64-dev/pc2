#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:47:11 2022

@author: davideteixeira
"""
from lote import lote

class predio(lote):
    
    def __init__(self, codigo, morada, area, valorpatrimonial, areadeimplantacao, npisos):
        super().__init__(codigo, morada, area, valorpatrimonial)
        self._areadeimplantacao = areadeimplantacao
        self._npisos = npisos
        self._anterior = ''
        self._seguinte = ''
    
    .complexo = []
    
    @property
    def area(self):
        return (self._area - self._areadeimplantacao)
    
    @property
    def npisos(self):
        return self._npisos
    
    def imi(self):
        imi = (0.003 * self.valorpatrimonial)* ((self.npisos+1)/ self.npisos)
        return imi
    
    def anterior(self, predio):
        self._anterior = predio
    
    def seguinte(self, predio):
        self._seguinte = predio
    