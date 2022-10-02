#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:35:55 2022

@author: davideteixeira
"""

class Conjunto:
    
    def __init__(self, set1):
        self.set = set1
    
    def intercecao(self, outro):
        t = self.set.intersection(outro.set)
        return Conjunto(t)
    
    def reuniao(self, outro):
        t = self.set.union(outro.set)
        return Conjunto(t)

    def __str__(self):
        string = ''
        for i in self.set:
            string = string + f'{i}, '
        string = string[0:len(string)-2]
        return string