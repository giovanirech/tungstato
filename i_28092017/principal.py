#!/usr/bin/python
import saida, custo, sys, entrada 
import definicoes
import numpy as np
import random
import sys
import os

from _differentialevolution import differential_evolution 
from joblib import Parallel, delayed, cpu_count
import time
from filelock import FileLock

#-----------------------------------------------------------------------#
nome_arquivo_entrada_gulp = "i_modeloentradagulp.gin"
arquivo_potencial = 'resultados_potencial.txt'
arquivo_propriedades = 'resultados_propriedades.txt'
arquivo_custos_individuais = 'custos_individuais.txt'
i = 0

#-----------------------------------------------------------------------#
def escreve_arquivo_potencial(arquivo_potencial,i_str,valor_custo,P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13):
    with FileLock('lock_potencial'):
        if os.path.exists(arquivo_potencial):
            append_write = 'a' 
        else:
            append_write = 'w' 
        with open(arquivo_potencial, append_write) as f:
            f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(i_str,valor_custo,P0,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10,P11,P12,P13)) 

def escreve_arquivo_propriedades(arquivo_propriedades,i_str,valor_custo,a2,a50,a100,a150,a200,a250,a293,c11_2,c11_50,c11_100,c11_150,c11_200,c11_250,c11_293,c12_2,c12_50,c12_100,c12_150,c12_200,c12_250,c12_293,c44_2,c44_50,c44_100,c44_150,c44_200,c44_250,c44_293):               
    with FileLock('lock_propriedades'):
        if os.path.exists(arquivo_propriedades):
            append_write = 'a' 
        else:
            append_write = 'w'       
        with open(arquivo_propriedades, append_write) as f:
            f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(i_str,valor_custo,
                                 a2,a50,a100,a150,a200,a250,a293,
                                 c11_2,c11_50,c11_100,c11_150,c11_200,c11_250,c11_293, 
                                 c12_2,c12_50,c12_100,c12_150,c12_200,c12_250,c12_293,
                                 c44_2,c44_50,c44_100,c44_150,c44_200,c44_250,c44_293))

def escreve_arquivo_custos(arquivo_custos_individuais,i_str, custo_total, custo_parametros, custo_posicoes, custo_constantes, custo_variacao_rede, custo_variacao_constantes):
    with FileLock('lock_custos'):
        if os.path.exists(arquivo_custos_individuais):
            append_write = 'a' 
        else:
            append_write = 'w' 
        with open(arquivo_custos_individuais, append_write) as f:
            f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(i_str, custo_total, custo_parametros, custo_posicoes, custo_constantes, custo_variacao_rede, custo_variacao_constantes)) 

#-------------------------------------------------------



def funcao (P):

    global nome_arquivo_entrada_gulp
    i = random.getrandbits(64)
    
    linhas_arquivo_entrada_gulp = entrada.le_arquivo_entrada_gulp(nome_arquivo_entrada_gulp)

    potenciais = entrada.cria_dicionario_potenciais(P)

    linhas_arquivo_entrada_gulp_alterado = entrada.altera_arquivo_entrada(linhas_arquivo_entrada_gulp, potenciais)

    i_str = str(i)
    os.chdir('tmp')
    os.mkdir(i_str)
    os.chdir(i_str)

    arquivo_entrada_execucao = nome_arquivo_entrada_gulp[0:nome_arquivo_entrada_gulp.find('.')] + '_'  + i_str + '.gin'

    arquivo_saida_execucao = nome_arquivo_entrada_gulp[0:nome_arquivo_entrada_gulp.find('.')] + '_'  + i_str + '.gout'

    entrada.cria_arquivo_entrada(arquivo_entrada_execucao, linhas_arquivo_entrada_gulp_alterado)
    
    entrada.executa_arquivo_gulp(arquivo_entrada_execucao, arquivo_saida_execucao)

    custo_total, custo_parametros, custo_posicoes, custo_constantes, custo_variacao_rede, custo_variacao_constantes = custo.calcula_custo(arquivo_saida_execucao)

    linhas_arquivo_saida_gulp = saida.le_linhas_arquivo_saida(arquivo_saida_execucao)
    
    if saida.verifica_final_execucao(arquivo_saida_execucao):
        (c11_2, c12_2, c44_2,c11_50, c12_50, c44_50,c11_100, c12_100, c44_100,c11_150, c12_150, c44_150,
         c11_200, c12_200, c44_200, c11_250, c12_250, c44_250, c11_293, c12_293, c44_293) = saida.busca_constantes_elasticas(linhas_arquivo_saida_gulp)
        a2,a50,a100,a150,a200,a250,a293 = saida.busca_parametros_de_rede(linhas_arquivo_saida_gulp)
    else:
        (c11_2, c12_2, c44_2,c11_50, c12_50, c44_50,c11_100, c12_100, c44_100,c11_150, c12_150, c44_150,
         c11_200, c12_200, c44_200, c11_250, c12_250, c44_250, c11_293, c12_293, c44_293) = (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        a2,a50,a100,a150,a200,a250,a293 = (0,0,0,0,0,0,0)
    os.chdir('../..')


    print '####################### ID %s #####################'%i
    print '######################### %s ######################'%time.ctime()
    print '   Charge core O:%s'%(P[0])
    print '   buck Zr-O: A=%s, rho=%s'%(P[1], P[2])
    print '   buck W-O:  A=%s, rho=%s'%(P[3], P[4])
    print '   buck O-O:  A=%s, rho=%s, C=%s'%(P[5], P[6], P[7])
    print '   spring O:  K= %s'%P[8]
    print '   three O-W-O: k = %s'%(P[9])
    print '   three O-Zr-O: k = %s'%(P[10])
    print '   covexp W-O: D= %s, a= %s, r0= %s'%(P[11], P[12], P[13])
    print 'Custo: %s'%custo_total
    print '###########################################################'
    
    if custo_total >= (definicoes.penalidade/10.0):
        os.system('rm -r tmp/%s'%i_str)
    
    #write to file
    escreve_arquivo_potencial(arquivo_potencial,i_str,custo_total,P[0],P[1],P[2],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],P[11],P[12],P[13])
    escreve_arquivo_propriedades(arquivo_propriedades,i_str,custo_total,a2,a50,a100,a150,a200,a250,a293,c11_2,c11_50,c11_100,c11_150,c11_200,c11_250,c11_293,c12_2,c12_50,c12_100,c12_150,c12_200,c12_250,c12_293,c44_2,c44_50,c44_100,c44_150,c44_200,c44_250,c44_293)               
    escreve_arquivo_custos(arquivo_custos_individuais,i_str, custo_total, custo_parametros, custo_posicoes, custo_constantes, custo_variacao_rede, custo_variacao_constantes)
    
    return custo_total

#======================================================================================

def pareval(listcoords):
    listresults = Parallel(n_jobs=cpu_count())(delayed(funcao)(i) for i in listcoords) 
    return listresults

def parallel_run():
    result = differential_evolution(pareval, bounds, parallel=True, polish=False, popsize=5)
    print result.x, result.fun

#======================================================================================
if __name__=='__main__':
    bounds=[(0,1), #charge O_core
            (10, 10000),(0.1, 0.5), #buck Zr-O: A, rho
            (10, 10000), (0.1, 0.5), #buck W-O: A, rho
            (10, 30000), (0.1,0.9), (1,100), #buck O-O: A, rho, C
            (5, 90), #spring O
            (0,5.0), #3-body O-Zr-O
            (0,5.0), #3-body O-W-O
            (1, 10), (10,50), (0.1, 3) #covexp W-O: D, a, r0
           ]
    
    with open(arquivo_potencial, 'w') as f:
        f.write('#ID\tCusto\tchargeO\tbuckZrA\tbuckZrRho\tbuckWA\tbuckWRho\tbuckOA\tbuckORho\tbuckOC\tspringO\t3bOWO\t3bOZrO\tcovexpWD\tcovexpWa\tcovexpWr0\n')
    
    with open(arquivo_propriedades, 'w') as f:
        f.write('#i_str\tcusto\ta2\ta50\ta100\ta150\ta200\ta250\ta293\tc11_2\tc11_50\tc11_100\tc11_150\tc11_200\tc11_250\tc11_293\tc12_2\tc12_50\tc12_100\tc12_150\tc12_200\tc12_250\tc12_293\tc44_2\tc44_50\tc44_100\tc44_150\tc44_200\tc44_250\tc44_293\n')
        
    with open(arquivo_custos_individuais, 'w') as f:
        f.write('#i_str\tcusto_total\tcusto_parametros\tcusto_posicoes\tcusto_constantes\tcusto_delta_a\tcusto_delta_constantes\n')

    if os.path.exists('tmp')==False:
        os.mkdir('tmp')
    start_time = time.time()
    parallel_run()
    print "Parallel run took %s seconds using %s cores" % ((time.time() - start_time), cpu_count())


    
    