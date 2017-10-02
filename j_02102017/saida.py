#!/usr/bin/python

import sys, definicoes
#--------------------------------------------------------
def le_linhas_arquivo_saida (arquivo):
    f = open(arquivo,"r")
    linhas = f.readlines()
    f.close()
    return linhas

#--------------------------------------------------------
def verifica_final_execucao(arquivo):
    
    arquivo_saida = arquivo

    linhas_arquivo_saida_gulp = le_linhas_arquivo_saida(arquivo_saida)

    for num,l in enumerate(linhas_arquivo_saida_gulp,0):

        if "error opening file " in l:
            return False

        if l.find("ERROR") != -1:
            return False

        if l.find("Conditions for a minimum have not been satisfied") != -1:
            return False
        
        if l.find("**** Too many reciprocal lattice vectors needed ****") != -1:
            return False

        if l.find("ERROR : Largest core-shell distance exceeds cutoff of cuts") != -1:
            return False
        
        if l.find("ERROR : Cell parameter has fallen below allowed limit") != -1:
            return False

        if l.find("Maximum number of function calls has been reached") != -1:
            return False

        if l.find("**** CPU limit has been exceeded - restart optimisation ****") != -1:
            return False
        
        if 'Elastic Constant Matrix' in l:
            if '*' in linhas_arquivo_saida_gulp[num+5]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+6]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+7]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+8]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+9]:
                return False
            if '*' in linhas_arquivo_saida_gulp[num+10]:
                return False

    return True

#--------------------------------------------------------
def busca_parametros_de_rede(linhas_arquivo_saida_gulp):
    parametro_rede_a = 0
    fim_config_7 = len(linhas_arquivo_saida_gulp)-1
    for num, linha in enumerate(linhas_arquivo_saida_gulp, 0):
        if 'Output for configuration   1' in linha:
            inicio_config_1 = num
        if 'Output for configuration   2' in linha:
            inicio_config_2 = num
            fim_config_1 = num-1
        if 'Output for configuration   3' in linha:
            inicio_config_3 = num
            fim_config_2 = num-1
        if 'Output for configuration   4' in linha:
            inicio_config_4 = num
            fim_config_3 = num-1
        if 'Output for configuration   5' in linha:
            inicio_config_5 = num
            fim_config_4 = num-1
        if 'Output for configuration   6' in linha:
            inicio_config_6 = num
            fim_config_5 = num-1
        if 'Output for configuration   7' in linha:
            inicio_config_7 = num
            fim_config_6 = num-1
            
    #### parametro a 2K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_1:fim_config_1]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_2K = float(l.split()[1])
            
    #### parametro a 50K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_2:fim_config_2]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_50K = float(l.split()[1])
            
    #### parametro a 100K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_3:fim_config_3]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_100K = float(l.split()[1])
            
    #### parametro a 150K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_4:fim_config_4]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_150K = float(l.split()[1])
            
    #### parametro a 200K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_5:fim_config_5]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_200K = float(l.split()[1])
            
    #### parametro a 250K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_6:fim_config_6]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_250K = float(l.split()[1])

    #### parametro a 293K #########    
    for l in linhas_arquivo_saida_gulp[inicio_config_7:fim_config_7]:
        if l.find("       a") != -1 and l.find("Angstrom     dE/de1(xx)") != -1:
            parametro_rede_a_293K = float(l.split()[1])
            
    return parametro_rede_a_2K, parametro_rede_a_50K, parametro_rede_a_100K, parametro_rede_a_150K, parametro_rede_a_200K, parametro_rede_a_250K, parametro_rede_a_293K
#--------------------------------------------------------
def busca_posicoes_atomicas (linhas_arquivo_saida_gulp):
    
    fim_config_7 = len(linhas_arquivo_saida_gulp)-1
    for num, linha in enumerate(linhas_arquivo_saida_gulp, 0):
        if 'Output for configuration   1' in linha:
            inicio_config_1 = num
        if 'Output for configuration   2' in linha:
            inicio_config_2 = num
            fim_config_1 = num-1
        if 'Output for configuration   3' in linha:
            inicio_config_3 = num
            fim_config_2 = num-1
        if 'Output for configuration   4' in linha:
            inicio_config_4 = num
            fim_config_3 = num-1
        if 'Output for configuration   5' in linha:
            inicio_config_5 = num
            fim_config_4 = num-1
        if 'Output for configuration   6' in linha:
            inicio_config_6 = num
            fim_config_5 = num-1
        if 'Output for configuration   7' in linha:
            inicio_config_7 = num
            fim_config_6 = num-1
            
    #### posicoes a 2K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_1:fim_config_1]:
        if l.find("     1  Zr    c") != -1:
            zr_x_2K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_2K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_2K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_2K = float(l.split()[3])
            o1_y_2K = float(l.split()[4])
            o1_z_2K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_2K = float(l.split()[3])
            o2_y_2K = float(l.split()[4])
            o2_z_2K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_2K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_2K = float(l.split()[3])
            
    #### posicoes a 50K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_2:fim_config_2]:
        if l.find("     1  Zr    c") != -1:
            zr_x_50K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_50K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_50K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_50K = float(l.split()[3])
            o1_y_50K = float(l.split()[4])
            o1_z_50K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_50K = float(l.split()[3])
            o2_y_50K = float(l.split()[4])
            o2_z_50K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_50K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_50K = float(l.split()[3])            

    #### posicoes a 100K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_3:fim_config_3]:
        if l.find("     1  Zr    c") != -1:
            zr_x_100K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_100K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_100K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_100K = float(l.split()[3])
            o1_y_100K = float(l.split()[4])
            o1_z_100K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_100K = float(l.split()[3])
            o2_y_100K = float(l.split()[4])
            o2_z_100K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_100K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_100K = float(l.split()[3])
            
    #### posicoes a 150K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_4:fim_config_4]:
        if l.find("     1  Zr    c") != -1:
            zr_x_150K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_150K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_150K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_150K = float(l.split()[3])
            o1_y_150K = float(l.split()[4])
            o1_z_150K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_150K = float(l.split()[3])
            o2_y_150K = float(l.split()[4])
            o2_z_150K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_150K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_150K = float(l.split()[3])    
            
            
    #### posicoes a 200K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_5:fim_config_5]:
        if l.find("     1  Zr    c") != -1:
            zr_x_200K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_200K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_200K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_200K = float(l.split()[3])
            o1_y_200K = float(l.split()[4])
            o1_z_200K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_200K = float(l.split()[3])
            o2_y_200K = float(l.split()[4])
            o2_z_200K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_200K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_200K = float(l.split()[3])     
            
    #### posicoes a 250K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_6:fim_config_6]:
        if l.find("     1  Zr    c") != -1:
            zr_x_250K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_250K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_250K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_250K = float(l.split()[3])
            o1_y_250K = float(l.split()[4])
            o1_z_250K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_250K = float(l.split()[3])
            o2_y_250K = float(l.split()[4])
            o2_z_250K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_250K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_250K = float(l.split()[3])
            
    #### posicoes a 293K ########
    for l in linhas_arquivo_saida_gulp[inicio_config_7:fim_config_7]:
        if l.find("     1  Zr    c") != -1:
            zr_x_293K = float(l.split()[3])

        if l.find("     2  W1    c") != -1:
            w1_x_293K = float(l.split()[3])
            
        if l.find("     3  W2    c") != -1:
            w2_x_293K = float(l.split()[3])

        if l.find("     4  O1    c") != -1:
            o1_x_293K = float(l.split()[3])
            o1_y_293K = float(l.split()[4])
            o1_z_293K = float(l.split()[5])

        if l.find("     5  O2    c") != -1:
            o2_x_293K = float(l.split()[3])
            o2_y_293K = float(l.split()[4])
            o2_z_293K = float(l.split()[5])
            
        if l.find("     6  O3    c") != -1:
            o3_x_293K = float(l.split()[3])
            
        if l.find("     7  O4    c") != -1:
            o4_x_293K = float(l.split()[3])
            
    return(zr_x_2K, w1_x_2K, w2_x_2K,o1_x_2K, o1_y_2K, o1_z_2K, o2_x_2K, o2_y_2K, o2_z_2K, o3_x_2K, o4_x_2K,
           zr_x_50K, w1_x_50K, w2_x_50K, o1_x_50K, o1_y_50K, o1_z_50K, o2_x_50K, o2_y_50K, o2_z_50K, o3_x_50K, o4_x_50K,
           zr_x_100K, w1_x_100K, w2_x_100K, o1_x_100K, o1_y_100K, o1_z_100K, o2_x_100K, o2_y_100K, o2_z_100K, o3_x_100K, o4_x_100K,
           zr_x_150K, w1_x_150K, w2_x_150K, o1_x_150K, o1_y_150K, o1_z_150K, o2_x_150K, o2_y_150K, o2_z_150K, o3_x_150K, o4_x_150K,
           zr_x_200K, w1_x_200K, w2_x_200K, o1_x_200K, o1_y_200K, o1_z_200K, o2_x_200K, o2_y_200K, o2_z_200K, o3_x_200K, o4_x_200K,
           zr_x_250K, w1_x_250K, w2_x_250K, o1_x_250K, o1_y_250K, o1_z_250K, o2_x_250K, o2_y_250K, o2_z_250K, o3_x_250K, o4_x_250K,
           zr_x_293K, w1_x_293K, w2_x_293K, o1_x_293K, o1_y_293K, o1_z_293K, o2_x_293K, o2_y_293K, o2_z_293K, o3_x_293K, o4_x_293K)

#--------------------------------------------------------
def busca_constantes_elasticas (linhas_arquivo_saida_gulp):
    fim_config_7 = len(linhas_arquivo_saida_gulp)-1
    for num, linha in enumerate(linhas_arquivo_saida_gulp, 0):
        if 'Output for configuration   1' in linha:
            inicio_config_1 = num
        if 'Output for configuration   2' in linha:
            inicio_config_2 = num
            fim_config_1 = num-1
        if 'Output for configuration   3' in linha:
            inicio_config_3 = num
            fim_config_2 = num-1
        if 'Output for configuration   4' in linha:
            inicio_config_4 = num
            fim_config_3 = num-1
        if 'Output for configuration   5' in linha:
            inicio_config_5 = num
            fim_config_4 = num-1
        if 'Output for configuration   6' in linha:
            inicio_config_6 = num
            fim_config_5 = num-1
        if 'Output for configuration   7' in linha:
            inicio_config_7 = num
            fim_config_6 = num-1
            
   
    ###### constantes a 2K ########        
    c11_2k = 0
    c12_2k = 0
    c44_2k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_1:fim_config_1], inicio_config_1):
        if 'Elastic Constant Matrix' in linha:
            c11_2K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_2K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_2K = float(linhas_arquivo_saida_gulp[num+8][40:50])
            
    ###### constantes a 50K ########        
    c11_50k = 0
    c12_50k = 0
    c44_50k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_2:fim_config_2], inicio_config_2):
        if 'Elastic Constant Matrix' in linha:
            c11_50K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_50K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_50K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 100K ########        
    c11_100k = 0
    c12_100k = 0
    c44_100k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_3:fim_config_3], inicio_config_3):
        if 'Elastic Constant Matrix' in linha:
            c11_100K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_100K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_100K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 150K ########        
    c11_150k = 0
    c12_150k = 0
    c44_150k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_4:fim_config_4], inicio_config_4):
        if 'Elastic Constant Matrix' in linha:
            c11_150K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_150K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_150K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 200K ########        
    c11_200k = 0
    c12_200k = 0
    c44_200k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_5:fim_config_5], inicio_config_5):
        if 'Elastic Constant Matrix' in linha:
            c11_200K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_200K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_200K = float(linhas_arquivo_saida_gulp[num+8][40:50])
               
    ###### constantes a 2K ########        
    c11_250k = 0
    c12_250k = 0
    c44_250k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_6:fim_config_6], inicio_config_6):
        if 'Elastic Constant Matrix' in linha:
            c11_250K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_250K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_250K = float(linhas_arquivo_saida_gulp[num+8][40:50])
            
    ###### constantes a 293K ########        
    c11_293k = 0
    c12_293k = 0
    c44_293k = 0
    
    for num, linha in enumerate(linhas_arquivo_saida_gulp[inicio_config_7:fim_config_7], inicio_config_7):
        if 'Elastic Constant Matrix' in linha:
            c11_293K = float(linhas_arquivo_saida_gulp[num+5][10:20])
            c12_293K = float(linhas_arquivo_saida_gulp[num+5][20:30])
            c44_293K = float(linhas_arquivo_saida_gulp[num+8][40:50])

    return (c11_2K, c12_2K, c44_2K,
            c11_50K, c12_50K, c44_50K,
            c11_100K, c12_100K, c44_100K,
            c11_150K, c12_150K, c44_150K,
            c11_200K, c12_200K, c44_200K,
            c11_250K, c12_250K, c44_250K,
            c11_293K, c12_293K, c44_293K)

#--------------------------------------------------------

def busca_valores_arquivo_saida (arquivo) :
    
    arquivo_saida = arquivo
    
    linhas_arquivo_saida_gulp = le_linhas_arquivo_saida(arquivo_saida)
    
    parametro_rede_a_2K, parametro_rede_a_50K, parametro_rede_a_100K, parametro_rede_a_150K, parametro_rede_a_200K, parametro_rede_a_250K, parametro_rede_a_293K = busca_parametros_de_rede(linhas_arquivo_saida_gulp)
    
    (zr_x_2K, w1_x_2K, w2_x_2K,o1_x_2K, o1_y_2K, o1_z_2K, o2_x_2K, o2_y_2K, o2_z_2K, o3_x_2K, o4_x_2K, zr_x_50K, w1_x_50K, w2_x_50K, o1_x_50K, o1_y_50K, o1_z_50K, o2_x_50K, o2_y_50K, o2_z_50K, o3_x_50K, o4_x_50K, zr_x_100K, w1_x_100K, w2_x_100K, o1_x_100K, o1_y_100K, o1_z_100K, o2_x_100K, o2_y_100K, o2_z_100K, o3_x_100K, o4_x_100K, zr_x_150K, w1_x_150K, w2_x_150K, o1_x_150K, o1_y_150K, o1_z_150K, o2_x_150K, o2_y_150K, o2_z_150K, o3_x_150K, o4_x_150K, zr_x_200K, w1_x_200K, w2_x_200K, o1_x_200K, o1_y_200K, o1_z_200K, o2_x_200K, o2_y_200K, o2_z_200K, o3_x_200K, o4_x_200K, zr_x_250K, w1_x_250K, w2_x_250K, o1_x_250K, o1_y_250K, o1_z_250K, o2_x_250K, o2_y_250K, o2_z_250K, o3_x_250K, o4_x_250K, zr_x_293K, w1_x_293K, w2_x_293K, o1_x_293K, o1_y_293K, o1_z_293K, o2_x_293K, o2_y_293K, o2_z_293K, o3_x_293K, o4_x_293K) = busca_posicoes_atomicas(linhas_arquivo_saida_gulp)
    
    c11_2K, c12_2K, c44_2K, c11_50K, c12_50K, c44_50K, c11_100K, c12_100K, c44_100K, c11_150K, c12_150K, c44_150K, c11_200K, c12_200K, c44_200K, c11_250K, c12_250K, c44_250K, c11_293K, c12_293K, c44_293K = busca_constantes_elasticas(linhas_arquivo_saida_gulp)
    
    return parametro_rede_a_2K, zr_x_2K, w1_x_2K, w2_x_2K,o1_x_2K, o1_y_2K, o1_z_2K, o2_x_2K, o2_y_2K, o2_z_2K,o3_x_2K, o4_x_2K, c11_2K, c12_2K, c44_2K, parametro_rede_a_50K, zr_x_50K, w1_x_50K, w2_x_50K, o1_x_50K, o1_y_50K, o1_z_50K, o2_x_50K, o2_y_50K, o2_z_50K, o3_x_50K, o4_x_50K, c11_50K, c12_50K, c44_50K, parametro_rede_a_100K, zr_x_100K, w1_x_100K, w2_x_100K, o1_x_100K, o1_y_100K, o1_z_100K, o2_x_100K, o2_y_100K, o2_z_100K, o3_x_100K, o4_x_100K, c11_100K, c12_100K, c44_100K, parametro_rede_a_150K, zr_x_150K, w1_x_150K, w2_x_150K, o1_x_150K, o1_y_150K, o1_z_150K, o2_x_150K, o2_y_150K, o2_z_150K,o3_x_150K, o4_x_150K, c11_150K, c12_150K, c44_150K, parametro_rede_a_200K, zr_x_200K, w1_x_200K, w2_x_200K, o1_x_200K, o1_y_200K, o1_z_200K, o2_x_200K, o2_y_200K, o2_z_200K, o3_x_200K, o4_x_200K, c11_200K, c12_200K, c44_200K, parametro_rede_a_250K, zr_x_250K, w1_x_250K, w2_x_250K, o1_x_250K, o1_y_250K, o1_z_250K, o2_x_250K, o2_y_250K, o2_z_250K, o3_x_250K, o4_x_250K, c11_250K, c12_250K, c44_250K, parametro_rede_a_293K, zr_x_293K, w1_x_293K, w2_x_293K, o1_x_293K, o1_y_293K, o1_z_293K, o2_x_293K, o2_y_293K, o2_z_293K, o3_x_293K, o4_x_293K, c11_293K, c12_293K, c44_293K

