import os
import custo
import saida
import numpy as np

file_list = os.listdir('tmp')
N = np.size(file_list)
Custo_total = []
parametros = []
posicoes = []  
constantes = [] 
ID = []
C11_2K = []
C12_2K = []
C44_2K = []
C11_293K = []
C12_293K = []
C44_293K = []
A_2K = []
A_293K = []
Zr_A = []
Zr_rho = []
W_A = []
W_rho = []
O_A = []
O_rho = []
O_C = []
O_spring = []



def procura_parametros_potencial(linhas_saida):
    for num, linha in enumerate(linhas_saida):
        if 'General interatomic potentials' in linha:
            zr_A = float(linhas_saida[num+6].split()[5])
            zr_rho = float(linhas_saida[num+6].split()[6])
            w_A = float(linhas_saida[num+7].split()[5])
            w_rho = float(linhas_saida[num+7].split()[6])
            o_A = float(linhas_saida[num+8].split()[5])
            o_rho = float(linhas_saida[num+8].split()[6])
            o_C = float(linhas_saida[num+8].split()[7])
            o_spring = float(linhas_saida[num+9].split()[6])
            
    return zr_A, zr_rho, w_A, w_rho, o_A, o_rho, o_C, o_spring

for n in range(N):
    i = file_list[n]
    print i
    arquivo_saida='tmp/%s/20170517_TempInterm_%s.gout'%(i,i)
    linhas_saida = saida.le_linhas_arquivo_saida(arquivo_saida)
    if saida.verifica_final_execucao(arquivo_saida):
        try:
            a_2K, a_50K, a_100K, a_150K, a_200K,a_250K, a_293K = saida.busca_parametros_de_rede(linhas_saida)
            c11_2K, c12_2K, c44_2K, c11_50K, c12_50K, c44_50K, c11_100K, c12_100K, c44_100K, c11_150K, c12_150K, c44_150K, c11_200K, c12_200K, c44_200K, c11_250K, c12_250K, c44_250K, c11_293K, c12_293K, c44_293K = saida.busca_constantes_elasticas(linhas_saida)
            c = custo.calcula_custo(arquivo_saida)
            #if (a_2K-a_293K >= 0.005) and (c11_2K > c11_293K) and (c12_2K > c12_293K) and (c44_2K > c44_293K) :
            if (a_2K-a_293K >= 0.001) and (c<300.0):
                zr_A, zr_rho, w_A, w_rho, o_A, o_rho, o_C, o_spring = procura_parametros_potencial(linhas_saida)
                Custo_total.append(c)
                ID.append(i)
                C11_2K.append(c11_2K)
                C12_2K.append(c12_2K)
                C44_2K.append(c44_2K)
                C11_293K.append(c11_293K)
                C12_293K.append(c12_293K)
                C44_293K.append(c44_293K)
                A_2K.append(a_2K)
                A_293K.append(a_293K)
                Zr_A.append(zr_A)
                Zr_rho.append(zr_rho)
                W_A.append(w_A)
                W_rho.append(w_rho)
                O_A.append(o_A)
                O_rho .append(o_rho)
                O_C.append(o_C)
                O_spring.append(o_spring)
                print '======================== FOUND NTE!!! ========================='
        except UnboundLocalError:
            print 'Error on potential %s'%i
            
    print '%3.2f%%    %s'%(100.0*n/N, c)

M = np.vstack((ID, np.asarray(Custo_total))).transpose()
M_sorted = M[np.asarray([np.float(M[i,1]) for i in range(np.size(ID))]).argsort()]

with open('resumo_20170517_TempInterm.txt', 'w') as f:
    f.write('#ID\tCusto_total\ta_2K\ta_293K\tc11_2K\tc11_293K\tc12_2K\tc12_293K\tc44_2K\tc44_293K\tZr_A\tZr_rho\tW_A\tW_rho\tO_A\tO_rho\tO_C\tO_spring\n')
    for i in range(np.size(ID)):
        f.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(M_sorted[i,0], M_sorted[i,1], A_2K[i],A_293K[i],
                                                            C11_2K[i], C12_2K[i], C44_2K[i],C11_293K[i], C12_293K[i], C44_293K[i],
                                                            Zr_A[i], Zr_rho[i], W_A[i], W_rho[i], 
                                                            O_A[i], O_rho[i], O_C[i], O_spring[i]))
