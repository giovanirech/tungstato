#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
import definicoes

with open('custos_individuais.txt','r') as f:
    linhas = f.readlines()
A=[]
total_minimo = definicoes.penalidade
n=0
parametros_minimo = total_minimo/3.0
posicoes_minimo = total_minimo/3.0
constantes_minimo = total_minimo/3.0
for l in linhas[1:]:
    i, total, parametros, posicoes, constantes = l.rstrip('\n').split('\t')
    if float(total)<total_minimo:
        total_minimo = float(total)
        parametros_minimo = float(parametros)
        posicoes_minimo = float(posicoes)
        constantes_minimo = float(constantes)
    n += 1 
    A.append([n, total_minimo, parametros_minimo, posicoes_minimo, constantes_minimo])
A=np.asarray(A)

fig = plt.figure(figsize=(8,5))
plt.semilogy(A[:,0], A[:,1], lw=2, label='Custo Total')
plt.semilogy(A[:,0], A[:,2], lw=1, label='Parametros')
plt.semilogy(A[:,0], A[:,3], lw=1, label='Posicoes')
plt.semilogy(A[:,0], A[:,4], lw=1, label='Constantes')
plt.xlabel('n')
plt.ylabel(u'Custo mínimo relativo')
plt.grid()
plt.grid(axis='y', which='minor')
plt.legend()
plt.savefig('CustoMinimo.png')