#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 22:06:21 2022

@author: davideteixeira
"""

class Poligono:
    
    def __init__(self, n):
        self.n = n
        self.vertices = dict()
        
    def defcord(self, i, x, y):
        if i <= self.n:
            self.vertices[i] = [x,y]
        else:
            print('O polígono não tem esse número de vértices')
    
    def comprimento(self, i):
        if i != self.n:
            comprimento = ((self.vertices[i][0] - self.vertices[i+1][0])**2 + (self.vertices[i][1] - self.vertices[i+1][1]) **2)**(0.5)
        else:
            comprimento = ((self.vertices[i][0]-self.vertices[1][0])**2+(self.vertices[i][1]-self.vertices[1][1])**2)**(0.5)
        return comprimento
    
    def __str__(self):
        string = ''
        for i in range(1, self.n+1):
            string = string + str(self.vertices[i]) + ', '
        string = string[0:len(string)-2]
        return string