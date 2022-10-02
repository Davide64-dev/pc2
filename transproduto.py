#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:47:32 2022

@author: davideteixeira
"""
from produto import Produto

class Transproduto(Produto):
    
    def __init__(self, nome, precodecompra, quantidade, precodevenda, cf, cv):
        super().__init__(nome, precodecompra, quantidade, precodevenda)
        self.precodevenda = precodevenda
        self.cf = cf
        self.cv = cv
        self.produtos = []
    
    def lucro(self):
        total = 0
        for key in self.vendidos:
            total += self.vendidos[key]
        lucro = self.precodevenda * total - self._precodecompra * total - self.cf - self.cv * total
        return f'Lucro: {lucro:.2f}€'
    
    def acrescentar(self, produto2):
        self.produtos.append(produto2)
    
    def remover(self, produto2):
        self.produtos.append(produto2)
     
    def arvore(self):
        p = self.produtos
        i = 1
        while p != []:
            i +=1
            p = p[0].produtos
        
        todos = []
        k = self.produtos
        todos = []
        
        for j in range(i-1):
            temp2 = []
            for prod in k:
                temp2.append(prod._nome)
            todos.append(temp2)
            t = len(k)
            l = []
            for m in range(t):
                l = l + k[m].produtos
            k = l
        string = '\n'
        for i in range(i-1):
            temp3 = todos[i]
            temp4 = ''
            for j in range(len (temp3)):
                temp4 += temp3[j] + ', '
            temp4 = temp4[0:len(temp4)-2]
            string = string + str(i+1) + ': '  + temp4 + '\n'
        return string
        
    def __str__(self):
        return f'\nNome: {self._nome}\nPreço de compra: {self._precodecompra:.2f}€\nQuantidade em Armazém: {self.quantidade} uni\nPreço de Venda = {self._precodevenda:.2f}€\nVendas = {self.vendidos}\nComponente Fixa do Custo de Transporte: {self.cf:.2f}€\nComponente Variável do Custo de Trannsporte: {self.cv:.2f}€/uni\n'