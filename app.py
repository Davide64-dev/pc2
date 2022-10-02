#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:59:56 2022

@author: davideteixeira
"""

from tkinter import *
from lote import lote
import tkinter as tk

def end_app():
    root.destroy()
    
def adicionar():
    codigo = codigo_var.get()
    morada = morada_var.get()
    area = area_var.get()
    valorpatrimonial = valorpatrimonial_var.get()
    temp = lote(codigo, morada, area, valorpatrimonial)
    listalote.insert('end', temp)
    codigo_var.set('')
    morada_var.set('')
    area_var.set('')
    valorpatrimonial_var.set('')
    valorcodigo.focus_set()
    valormorada.focus_set()
    valorarea.focus_set()
    valorvalorpatrimonial.focus_set()
    
def remover():
    codigo = codigo_var.get()
    for k in listalote:
        l = k.split()
        temp = k[0]
        if temp.codigo == codigo:
            listalote.delete(0, k)

root = Tk()
root.geometry('850x550+300+200')
root.title("Form1")

sairlabel = Label(root, text ="Sair")
sairlabel.grid(row=0, column=0, padx=10,pady=10)

codigolabel = Label(root, text = "Código")
codigolabel.grid(row=1, column=1, padx=10, pady=10)

moradalabel = Label(root, text = "Morada")
moradalabel.grid(row=2,column=1,padx=10,pady=10)

arealabel = Label(root, text = "Área")
arealabel.grid(row=3,column=1,padx=10,pady=10)

valorpatrimonial = Label(root, text = "Valor Patrimonial")
valorpatrimonial.grid(row=4, column=1,padx=10,pady=10)

codigo_var = StringVar()
valorcodigo = Entry(root, textvariable = codigo_var)
valorcodigo.grid(row=1, column= 2, padx=10, pady=10)

morada_var = StringVar()
valormorada = Entry(root, textvariable = morada_var)
valormorada.grid(row=2,column=2,padx=10,pady=10)

area_var = StringVar()
valorarea = Entry(root, textvariable = area_var)
valorarea.grid(row=3,column=2,padx=10,pady=10)

valorpatrimonial_var = StringVar()
valorvalorpatrimonial = Entry(root, textvariable = valorpatrimonial_var)
valorvalorpatrimonial.grid(row=4, column=2,padx=10,pady=10)

botaoadicionar = Button(root, text = 'Adicionar Lote', command = adicionar)
botaoadicionar.grid(row=5, column=1,padx=10,pady=10)

botaoremover = Button(root, text = 'Remover Lote', command = remover)
botaoremover.grid(row=5, column=2,padx=10,pady=10)

loteslabel = Label(root, text = "Lotes:")
loteslabel.grid(row=6,column=1,padx=10,pady=10)

#lotes = DoubleVar()
listalote = tk.Listbox(root)
listalote.grid(row = 7, column = 2, sticky = 'W')


##Segunda Parte
confrontacoeslabel = Label(root, text="Ver Confrontações")
confrontacoeslabel.grid(row=0, column=3,padx=10,pady=10)

codigo2label = Label(root, text = "Código")
codigo2label.grid(row=1, column=3, padx=10, pady=10)

codigo2_var = StringVar()
valorcodigo2 = Entry(root, textvariable = codigo2_var)
valorcodigo2.grid(row=1, column= 4, padx=10, pady=10)

botaoconfrontacoes = Button(root, text = 'Ver confrontações', command = remover)
botaoconfrontacoes.grid(row=2, column=4,padx=10,pady=10)

editarconfrontacoeslabel = Label(root, text="Editar Confrontações")
editarconfrontacoeslabel.grid(row=3, column=3,padx=10,pady=10)

codigo3label = Label(root, text = "Código")
codigo3label.grid(row=4, column=3, padx=10, pady=10)

codigo3_var = StringVar()
valorcodigo3 = Entry(root, textvariable = codigo2_var)
valorcodigo3.grid(row=4, column= 4, padx=10, pady=10)

botaoadicionarconfrontacoes = Button(root, text = 'Adicionar confrontação', command = remover)
botaoadicionarconfrontacoes.grid(row=5, column=3,padx=10,pady=10)

botaoremoverconfrontacoes = Button(root, text = 'Remover confrontação', command = remover)
botaoremoverconfrontacoes.grid(row=5, column=4,padx=10,pady=10)

confrontacoes2label = Label(root, text = "Confrontações")
confrontacoes2label.grid(row=6, column=3, padx=10, pady=10)

listaconfrontacoes = tk.Listbox(root)
listaconfrontacoes.grid(row = 7, column = 4, sticky = 'W')






root.mainloop()