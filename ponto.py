#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 21:44:39 2022

@author: davideteixeira
"""

class Ponto:
    
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def distancia(self, outro):
        temp = ((self.x-outro.x) ** 2 + (self.y-outro.y) ** 2) ** (0.5)
        return f'\n{temp:.3f}'
    
    def __str__(self):
        return f'\n({self.x},{self.y})'