#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:50:42 2022

@author: davideteixeira
"""

class Produto:
    
    def __init__(self, nome, precodecompra, quantidade, precodevenda):
        self._nome = nome
        self._precodecompra = precodecompra
        self.quantidade = quantidade
        self._precodevenda = precodevenda
        self.vendidos = dict()
        
    def adicionar(self, quantidade):
        self.quantidade += quantidade
    
    def retirar(self, quantidade, funcionario):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            if funcionario in self.vendidos.keys():
                self.vendidos[funcionario] += quantidade
            else:
                self.vendidos[funcionario] = quantidade
        else:
            print('Quantidade insuficiente')
    
    def lucro(self):
        total = 0
        for key in self.vendidos:
            total += self.vendidos[key]
        lucro = (self._precodevenda - self._precodecompra) * total
        return f'Lucro: {lucro:.2f}€'

    def total(self):
        total = 0
        for key in self.vendidos:
            total += self.vendidos[key]
        return(total)

    def __str__(self):
        return self._nome
        return f'\nNome: {self._nome}\nPreço de compra: {self._precodecompra:.2f}€\nQuantidade em Armazém: {self.quantidade} uni\nPreço de Venda = {self._precodevenda:.2f}€\nVendas = {self.vendidos}\n'