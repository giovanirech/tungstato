#!/usr/bin/python

import saida, custo, sys, os, definicoes

#--------------------------------------------------------------
def le_arquivo_entrada_gulp (arquivo):

    f = open(arquivo,"r")

    linhas = f.readlines()

    f.close()

    return linhas


#--------------------------------------------------------------
def cria_dicionario_potenciais(P):

    i = 0

    potenciais = {}

    for p in P:
        chave = '$' + str(i) + '$'

        potenciais[chave] = P[i]

        i = i + 1

    return potenciais

#--------------------------------------------------------
def altera_arquivo_entrada (linhas_arquivo_entrada_gulp, potenciais):

    linhas_arquivo_entrada_gulp_copia = list(linhas_arquivo_entrada_gulp)        

    chaves = potenciais.keys()

    for c in chaves:

        i = 0

        for l in linhas_arquivo_entrada_gulp_copia:

            if l.find(c) != -1 :
                linhas_arquivo_entrada_gulp_copia[i] = l.replace(c,str(potenciais[c]))
                
            #Altera carga da casca de oxigenio que nao e parametro livre
            if '&0&' in l:
                linhas_arquivo_entrada_gulp_copia[i] = l.replace('&0', str(-potenciais['$0']-2))
                
            if '&1&' in l:
                linhas_arquivo_entrada_gulp_copia[i] = l.replace('&1', str(-potenciais['$1']-2))

            i = i + 1

    return linhas_arquivo_entrada_gulp_copia

#--------------------------------------------------------
def cria_arquivo_entrada(nome_arquivo_entrada_gulp, linhas_arquivo_entrada_gulp_alterado):

    f = open(nome_arquivo_entrada_gulp, 'w')

    for l in linhas_arquivo_entrada_gulp_alterado:

        f.write(l)

    f.close()

#--------------------------------------------------------
def executa_arquivo_gulp( nome_arquivo_entrada_gulp, nome_arquivo_saida_gulp):

    entrada = nome_arquivo_entrada_gulp

    saida = nome_arquivo_saida_gulp

    os.system('timeout 10800 ' +  definicoes.diretorio_gulp +'/gulp < ' + entrada + ' > ' + saida ) 

