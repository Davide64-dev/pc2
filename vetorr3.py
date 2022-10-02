#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 16:26:10 2022

@author: davideteixeira
"""

class VetorR3:
    
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    @classmethod
    def from_string(cls, string):
        args_list = string.split(',')
        argx = float(args_list[0])
        argy = float(args_list[1])
        argz = float(args_list[2])
        return cls (argx, argy, argz)
    
    @property
    def norma (self):
        norma = ((self.x) ** 2 + (self.y) ** 2 + (self.z) ** 2) ** 0.5
        return norma
    
    
    def __add__(self, vetor2):
        x = self.x + vetor2.x
        y = self.y + vetor2.y
        z = self.z + vetor2.z
        return VetorR3(x, y,z)

    def __mul__(self, vetor2):
        produtoescalar = self.x * vetor2.x + self.y * vetor2.y + self.z * vetor2.z
        return produtoescalar
    
    def __pow__(self, vetor2):
        x = self.y * vetor2.z - self.z * vetor2.y
        y = self.z * vetor2.x -self.x * vetor2.z 
        z = self.x * vetor2.y - self.y * vetor2.x
        return VetorR3(x,y,z)
    
    def __str__ (self):
        return f'({self.x}, {self.y}, {self.z}) - Norma = {self.norma:.2f}'