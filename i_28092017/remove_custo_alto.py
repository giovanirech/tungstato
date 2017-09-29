# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

f = open('lista_id_custo.txt','r')
linhas = f.readlines()
f.close()
id_pot = []
custo = []
for l in linhas:
    id_pot.append(l.split('\t')[0])
    custo.append(float(l.split('\t')[1].strip('\n')))

os.chdir('tmp')
N = len(id_pot)
for i in range(len(id_pot)):
    if custo[i] >= 100:
        if os.path.exists(id_pot[i]):
            os.system('rm -r -f '+id_pot[i])
            print 'Directory removed: '+id_pot[i]
    print '%.2f%%'%(100*float(i)/float(N))
os.chdir('..')