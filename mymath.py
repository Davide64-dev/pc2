#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 18:04:33 2022

@author: davideteixeira
"""
import math

class myMath:
    
    @staticmethod
    def fatorial(n):
        temp = 1
        for i in range(1, n+1):
            temp *= i
        return temp
    
    
    @staticmethod
    def exp(x):
        temp = 0
        for n in range(1000):
            temp += x**n / myMath.fatorial(n)
        return temp
    
    # Método que condensa uma matriz pelo método da eliminação de gauss
    @staticmethod
    def gauss(a,b):
        n = len(b)
        
        #para cada coluna
        for k in range(0,n-1):
            temp = list()
            
            #procura pelo maior valor absoluto da coluna a partir do pivô
            for i in range(k,n):
                temp.append(abs(a[i][k]))
            m = max(temp)
            p = temp.index(m)
            p = p + k
            
            #Troca de linha, caso se arranje um número maior, para ficar com o maior pivô
            # possível
            if p != k:
                for j in range(k,n):
                    aux = a[k][j]
                    a[k][j] = a[p][j]
                    a[p][j] = aux
                aux = b[k]
                b[k] = b[p]
                b[p] = aux
            
            # Multiplicação e adição de linhas para condensar toda a coluna abaixo do pivô
            for i in range(k+1, n):
                mult = a[i][k] / a[k][k]
                a[i][k] = 0
                for j in range(k+1, n):
                    a[i][j] = a[i][j] - mult * a[k][j]
                b[i] = b[i] - mult*b[k]
                
        return a,b
    
    # Método que dados um vetor e uma matriz condensados, soluciona para X um problema AX = B
    @staticmethod
    def subst_inv(a,b):
        # Criação do Vetor e do seu último elemento
        n = len(b)
        x = [0] * n
        x[n-1] = b[n-1] / a[n-1][n-1]
        # Para cada elemento
        for i in range(n-2,-1,-1):
            produto = 0
            # Criação do vetor
            for j in range(i, n):
                produto = produto + x[j] * a[i][j]
            x[i] = (b[i] - produto) / a[i][i]
            
        return x
    
    # Soluciona um problema AX = B, invocando os métodos "gauss" e "subst_inv"
    @staticmethod
    def AXB(a,b):
        a,b = myMath.gauss(a,b)
        x = myMath.subst_inv(a,b)
        
        return x
    
    # Calcula o determinante de uma matriz qualquer
    @staticmethod
    def determinante(a):
        m = len(a)
        b = [0]* m
        
        # Condensar a matriz
        a,b = myMath.gauss(a,b)
        produto = 1
        
        # Produto dos pivôs da diagonal principal da matriz condensada = determinante
        for i in range(m):
            produto = produto * a[i][i]
            
        return produto
    
    # Resolve uma equação não linear, utilizando o método da substituição direta
    @staticmethod
    def subst_direta(x0, tol, maxiter):
        k = 0
        erro = tol + 1
        while k < maxiter and erro > tol:
            k = k + 1
            x = myMath.g(x0)
            erro = abs(x-x0)
            x0 = x
        return x, erro
    
    # Resolve uma equação não linear, utilizando o método de newton
    @staticmethod
    def newton(x0, tol, maxiter):
        k = 0
        erro = tol + 1
        while k < maxiter and erro > tol:
            k = k + 1
            x = x0 - (myMath.f(x0) / myMath.flinha(x0))
            erro = abs(x-x0)
            x0 = x
        return (x,erro)
    
    # Constroi uma tabela das diferenças divididas para realizar uma interpolação polinomial
    @staticmethod
    def tabela_DD(x,y):
        m = len(x)
        T = [[0]*m for i in range(m)]
        for i in range(m):
            T[i][0] = y[i]
        for j in range(1,m):
            for i in range(j,m):
                T[i][j] = round((T[i][j-1] - T[i-1][j-1]) / (x[i]-x[i-j]),4)
        return T
    
    # Realiza a interpolação propriamente dita, utilizando o método "tabela_DD"
    @staticmethod
    def interpolacao(x,y,valor):
        m = len(x)
        T = myMath.tabela_DD(x,y)
        soma = T[0][0]
        for i in range(1,m):
            temp = T[i][i]
            for j in range(0,i):
                temp = temp * (valor - x[j])
            soma = soma + temp
        return soma
    
    # Resolve um integral definido utilizando a regra dos trapézios
    @staticmethod
    def trapezios(a,b,n):
        h = (b-a)/n
        soma = 0
        for i in range(1,n-1):
            x = a + i * h
            soma = soma + myMath.f(x)
        trap = (h/2) * (myMath.f(a) + 2 * soma + myMath.f(b))
        return trap
    
    
    # Resolve um integral definido utilizando a regra de simpson
    @staticmethod
    def simpson(a, b, n):
        h = (b-a)/n
        soma_impar = 0
        soma_par = 0
        for i in range(1,n-2,2):
            x = a + h * i
            soma_par = soma_par + myMath.f(x)
        for i in range(1,n-1,2):
            x = a + h* i
            soma_impar = soma_impar + myMath.f(x)
        simp = (h/3)*(myMath.f(a) + 4 * soma_impar + 2 * soma_par + myMath.f(b))
        return simp
    
    ## Funções Auxiliares
    
    # Função g, utilizado em subst_direta
    @staticmethod
    def g(x):
        y = x**2
        return y
    
    # Função f, utilizada nos métodos de integração e no método de Newto
    @staticmethod
    def f(x):
        y = 0
        y = math.sqrt(9-x**2-y**2)
        return y
    
    # Função derivada da função f acima. Utilizada exclusivamente no método de Newton
    @staticmethod
    def flinha(x):
        y = (math.exp(x) - math.exp(-x))/2
        return y