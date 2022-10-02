#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:32:48 2022

@author: davideteixeira
"""

class lote:
    lotes = []
    def __init__(self, codigo, morada, area, valorpatrimonial):
        self._codigo = codigo
        self._morada = morada
        self._area = area
        self.valorpatrimonial = str(valorpatrimonial)
        self.confrontacoes = []
        lote.lotes.append(self)
        
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def morada(self):
        return self._morada
    
    @property
    def area(self):
        return self._area
    
    @property
    def valorpatrimonial(self):
        return self._valorpatrimonial
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
    
    @morada.setter
    def morada(self, morada):
        self._morada = morada
    
    @area.setter
    def area(self, area):
        self._area = area
    
    @valorpatrimonial.setter
    def valorpatrimonial(self, valorpatrimonial):
        self._valorpatrimonial = valorpatrimonial
    
    def __str__(self):
        return f'{self._codigo} {self._morada} {self._area} {self.valorpatrimonial}'
    
    def imi(self):
        imi = self.valorpatrimonial * (0.003)
        return imi
    
    def adicionar(self, lote):
        self.confrontacoes.append(lote)
    
    def eliminar(self, codigo):
        for lote in self.confrontacoes:
            if lote.codigo == codigo:
                objeto = lote
                break
        self.confrontacoes.remove(objeto)
    
    def fusao(self, lote):
        if lote in self.confrontacoes:
            codigo = self.codigo
            morada = self.morada
            valorpatrimonial = self.valorpatrimonial
            area = self.area + lote.area
        novolote = lote(codigo, morada, area, valorpatrimonial)
        return novolote