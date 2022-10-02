#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:01:55 2022

@author: davideteixeira
"""

class romano:
    
    def __init__(self, n):
        self._n = int(n)
    
    @classmethod
    def from_string(cls, string):
        l = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
        n = l.index(string)+1
        return cls(n)
    
    def adicionar(self, n2):
        soma = self._n + n2._n
        return romano(soma)
    
    def decimal(self):
        return self._n
    
    def __str__(self):
        l = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
        n = l[self._n-1]
        return n