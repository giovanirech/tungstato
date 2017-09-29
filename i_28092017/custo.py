#!/usr/bin/python

import definicoes, saida

#--------------------------------------------------------------------------------------------------

def funcao_custo(parametro_rede_a_2K, zr_x_2K, w1_x_2K, w2_x_2K,
                 o1_x_2K, o1_y_2K, o1_z_2K, o2_x_2K, o2_y_2K, o2_z_2K, 
                 o3_x_2K, o4_x_2K, c11_2K, c12_2K, c44_2K,#------------------------------------------------
                 parametro_rede_a_50K, zr_x_50K, w1_x_50K, w2_x_50K,
                 o1_x_50K, o1_y_50K, o1_z_50K, o2_x_50K, o2_y_50K, o2_z_50K, 
                 o3_x_50K, o4_x_50K, c11_50K, c12_50K, c44_50K,#-------------------------------------------
                 parametro_rede_a_100K, zr_x_100K, w1_x_100K, w2_x_100K,
                 o1_x_100K, o1_y_100K, o1_z_100K, o2_x_100K, o2_y_100K, o2_z_100K, 
                 o3_x_100K, o4_x_100K, c11_100K, c12_100K, c44_100K,#------------------------------------------------
                 parametro_rede_a_150K, zr_x_150K, w1_x_150K, w2_x_150K,
                 o1_x_150K, o1_y_150K, o1_z_150K, o2_x_150K, o2_y_150K, o2_z_150K, 
                 o3_x_150K, o4_x_150K, c11_150K, c12_150K, c44_150K,#------------------------------------------------
                 parametro_rede_a_200K, zr_x_200K, w1_x_200K, w2_x_200K,
                 o1_x_200K, o1_y_200K, o1_z_200K, o2_x_200K, o2_y_200K, o2_z_200K, 
                 o3_x_200K, o4_x_200K, c11_200K, c12_200K, c44_200K,#------------------------------------------------
                 parametro_rede_a_250K, zr_x_250K, w1_x_250K, w2_x_250K,
                 o1_x_250K, o1_y_250K, o1_z_250K, o2_x_250K, o2_y_250K, o2_z_250K, 
                 o3_x_250K, o4_x_250K, c11_250K, c12_250K, c44_250K,#-------------------------------------------
                 parametro_rede_a_293K, zr_x_293K, w1_x_293K, w2_x_293K,
                 o1_x_293K, o1_y_293K, o1_z_293K, o2_x_293K, o2_y_293K, o2_z_293K, 
                 o3_x_293K, o4_x_293K, c11_293K, c12_293K, c44_293K):

    parametros = definicoes.peso_parametros * (abs(1.0-parametro_rede_a_2K/definicoes.a_2K_experimental) +
                                               abs(1.0-parametro_rede_a_50K/definicoes.a_50K_experimental) +
                                               abs(1.0-parametro_rede_a_100K/definicoes.a_100K_experimental) +
                                               abs(1.0-parametro_rede_a_150K/definicoes.a_150K_experimental) +
                                               abs(1.0-parametro_rede_a_200K/definicoes.a_200K_experimental) +
                                               abs(1.0-parametro_rede_a_250K/definicoes.a_250K_experimental) +
                                               abs(1.0-parametro_rede_a_293K/definicoes.a_293K_experimental))/7.0
    posicoes = definicoes.peso_posicoes * (#abs(1.0-zr_x_2K/definicoes.zr_x_2K_experimental)+ #-------------T=2K
                                          abs(1.0-w1_x_2K/definicoes.w1_x_2K_experimental)+
                                          abs(1.0-w2_x_2K/definicoes.w2_x_2K_experimental)+
                                          abs(1.0-o1_x_2K/definicoes.o1_x_2K_experimental)+
                                          abs(1.0-o1_y_2K/definicoes.o1_y_2K_experimental)+
                                          abs(1.0-o1_z_2K/definicoes.o1_z_2K_experimental)+
                                          abs(1.0-o2_x_2K/definicoes.o2_x_2K_experimental)+
                                          abs(1.0-o2_y_2K/definicoes.o2_y_2K_experimental)+
                                          abs(1.0-o2_z_2K/definicoes.o2_z_2K_experimental)+
                                          abs(1.0-o3_x_2K/definicoes.o3_x_2K_experimental)+
                                          abs(1.0-o4_x_2K/definicoes.o4_x_2K_experimental)+
                                          #abs(1.0-zr_x_50K/definicoes.zr_x_50K_experimental)+ #-------------T=50K
                                          abs(1.0-w1_x_50K/definicoes.w1_x_50K_experimental)+
                                          abs(1.0-w2_x_50K/definicoes.w2_x_50K_experimental)+
                                          abs(1.0-o1_x_50K/definicoes.o1_x_50K_experimental)+
                                          abs(1.0-o1_y_50K/definicoes.o1_y_50K_experimental)+
                                          abs(1.0-o1_z_50K/definicoes.o1_z_50K_experimental)+
                                          abs(1.0-o2_x_50K/definicoes.o2_x_50K_experimental)+
                                          abs(1.0-o2_y_50K/definicoes.o2_y_50K_experimental)+
                                          abs(1.0-o2_z_50K/definicoes.o2_z_50K_experimental)+
                                          abs(1.0-o3_x_50K/definicoes.o3_x_50K_experimental)+
                                          abs(1.0-o4_x_50K/definicoes.o4_x_50K_experimental)+
                                          #abs(1.0-zr_x_100K/definicoes.zr_x_100K_experimental)+ #-------------T=100K
                                          abs(1.0-w1_x_100K/definicoes.w1_x_100K_experimental)+
                                          abs(1.0-w2_x_100K/definicoes.w2_x_100K_experimental)+
                                          abs(1.0-o1_x_100K/definicoes.o1_x_100K_experimental)+
                                          abs(1.0-o1_y_100K/definicoes.o1_y_100K_experimental)+
                                          abs(1.0-o1_z_100K/definicoes.o1_z_100K_experimental)+
                                          abs(1.0-o2_x_100K/definicoes.o2_x_100K_experimental)+
                                          abs(1.0-o2_y_100K/definicoes.o2_y_100K_experimental)+
                                          abs(1.0-o2_z_100K/definicoes.o2_z_100K_experimental)+
                                          abs(1.0-o3_x_100K/definicoes.o3_x_100K_experimental)+
                                          abs(1.0-o4_x_100K/definicoes.o4_x_100K_experimental)+
                                          #abs(1.0-zr_x_150K/definicoes.zr_x_150K_experimental)+ #-------------T=150K
                                          abs(1.0-w1_x_150K/definicoes.w1_x_150K_experimental)+
                                          abs(1.0-w2_x_150K/definicoes.w2_x_150K_experimental)+
                                          abs(1.0-o1_x_150K/definicoes.o1_x_150K_experimental)+
                                          abs(1.0-o1_y_150K/definicoes.o1_y_150K_experimental)+
                                          abs(1.0-o1_z_150K/definicoes.o1_z_150K_experimental)+
                                          abs(1.0-o2_x_150K/definicoes.o2_x_150K_experimental)+
                                          abs(1.0-o2_y_150K/definicoes.o2_y_150K_experimental)+
                                          abs(1.0-o2_z_150K/definicoes.o2_z_150K_experimental)+
                                          abs(1.0-o3_x_150K/definicoes.o3_x_150K_experimental)+
                                          abs(1.0-o4_x_150K/definicoes.o4_x_150K_experimental)+
                                          #abs(1.0-zr_x_200K/definicoes.zr_x_200K_experimental)+ #-------------T=200K
                                          abs(1.0-w1_x_200K/definicoes.w1_x_200K_experimental)+
                                          abs(1.0-w2_x_200K/definicoes.w2_x_200K_experimental)+
                                          abs(1.0-o1_x_200K/definicoes.o1_x_200K_experimental)+
                                          abs(1.0-o1_y_200K/definicoes.o1_y_200K_experimental)+
                                          abs(1.0-o1_z_200K/definicoes.o1_z_200K_experimental)+
                                          abs(1.0-o2_x_200K/definicoes.o2_x_200K_experimental)+
                                          abs(1.0-o2_y_200K/definicoes.o2_y_200K_experimental)+
                                          abs(1.0-o2_z_200K/definicoes.o2_z_200K_experimental)+
                                          abs(1.0-o3_x_200K/definicoes.o3_x_200K_experimental)+
                                          abs(1.0-o4_x_200K/definicoes.o4_x_200K_experimental)+
                                          #abs(1.0-zr_x_250K/definicoes.zr_x_250K_experimental)+ #-------------T=250K
                                          abs(1.0-w1_x_250K/definicoes.w1_x_250K_experimental)+
                                          abs(1.0-w2_x_250K/definicoes.w2_x_250K_experimental)+
                                          abs(1.0-o1_x_250K/definicoes.o1_x_250K_experimental)+
                                          abs(1.0-o1_y_250K/definicoes.o1_y_250K_experimental)+
                                          abs(1.0-o1_z_250K/definicoes.o1_z_250K_experimental)+
                                          abs(1.0-o2_x_250K/definicoes.o2_x_250K_experimental)+
                                          abs(1.0-o2_y_250K/definicoes.o2_y_250K_experimental)+
                                          abs(1.0-o2_z_250K/definicoes.o2_z_250K_experimental)+
                                          abs(1.0-o3_x_250K/definicoes.o3_x_250K_experimental)+
                                          abs(1.0-o4_x_250K/definicoes.o4_x_250K_experimental)+
                                          #abs(1.0-zr_x_293K/definicoes.zr_x_293K_experimental)+ #-------------T=293K
                                          abs(1.0-w1_x_293K/definicoes.w1_x_293K_experimental)+
                                          abs(1.0-w2_x_293K/definicoes.w2_x_293K_experimental)+
                                          abs(1.0-o1_x_293K/definicoes.o1_x_293K_experimental)+
                                          abs(1.0-o1_y_293K/definicoes.o1_y_293K_experimental)+
                                          abs(1.0-o1_z_293K/definicoes.o1_z_293K_experimental)+
                                          abs(1.0-o2_x_293K/definicoes.o2_x_293K_experimental)+
                                          abs(1.0-o2_y_293K/definicoes.o2_y_293K_experimental)+
                                          abs(1.0-o2_z_293K/definicoes.o2_z_293K_experimental)+
                                          abs(1.0-o3_x_293K/definicoes.o3_x_293K_experimental)+
                                          abs(1.0-o4_x_293K/definicoes.o4_x_293K_experimental))/70.0
    constantes = definicoes.peso_constantes* (abs(1.0-c11_2K/definicoes.c11_2K_experimental) + #-----------T=2K
                                              abs(1.0-c12_2K/definicoes.c12_2K_experimental) +
                                              abs(1.0-c44_2K/definicoes.c44_2K_experimental) +
                                              abs(1.0-c11_50K/definicoes.c11_50K_experimental) + #-----------T=50K
                                              abs(1.0-c12_50K/definicoes.c12_50K_experimental) +
                                              abs(1.0-c44_50K/definicoes.c44_50K_experimental) +
                                              abs(1.0-c11_100K/definicoes.c11_100K_experimental) + #-----------T=100K
                                              abs(1.0-c12_100K/definicoes.c12_100K_experimental) +
                                              abs(1.0-c44_100K/definicoes.c44_100K_experimental) +
                                              abs(1.0-c11_150K/definicoes.c11_150K_experimental) + #-----------T=150K
                                              abs(1.0-c12_150K/definicoes.c12_150K_experimental) +
                                              abs(1.0-c44_150K/definicoes.c44_150K_experimental) +
                                              abs(1.0-c11_200K/definicoes.c11_200K_experimental) + #-----------T=200K
                                              abs(1.0-c12_200K/definicoes.c12_200K_experimental) +
                                              abs(1.0-c44_200K/definicoes.c44_200K_experimental) +
                                              abs(1.0-c11_250K/definicoes.c11_250K_experimental) + #-----------T=250K
                                              abs(1.0-c12_250K/definicoes.c12_250K_experimental) +
                                              abs(1.0-c44_250K/definicoes.c44_250K_experimental) +
                                              abs(1.0-c11_293K/definicoes.c11_293K_experimental) + #-----------T=293K
                                              abs(1.0-c12_293K/definicoes.c12_293K_experimental) +
                                              abs(1.0-c44_293K/definicoes.c44_293K_experimental))/21.0
    
    delta_a_calc = parametro_rede_a_293K-parametro_rede_a_2K
    delta_a_exp = definicoes.a_293K_experimental-definicoes.a_2K_experimental
    variacao_parametro_rede = definicoes.peso_variacao_parametro_rede*(abs(1.0-delta_a_calc/delta_a_exp))
    
    delta_c11_calc = c11_293K-c11_2K
    delta_c11_exp = definicoes.c11_293K_experimental-definicoes.c11_2K_experimental
    delta_c12_calc = c12_293K-c12_2K
    delta_c12_exp = definicoes.c12_2K_experimental-definicoes.c12_293K_experimental  
    delta_c44_calc = c44_293K-c44_2K
    delta_c44_exp = definicoes.c44_293K_experimental-definicoes.c44_2K_experimental
    variacao_constantes = definicoes.peso_variacao_constantes*(abs(1.0-delta_c11_calc/delta_c11_exp)+
                                                               abs(1.0-delta_c12_calc/delta_c12_exp)+
                                                               abs(1.0-delta_c44_calc/delta_c44_exp))/3.0                           
    custo_total = parametros + posicoes +  constantes + variacao_parametro_rede+variacao_constantes
    return custo_total, parametros, posicoes, constantes


#--------------------------------------------------------------------------------------------------
def calcula_custo (arquivo_saida):
    if ( saida.verifica_final_execucao(arquivo_saida) == True ):
        parametro_rede_a_2K, zr_x_2K, w1_x_2K, w2_x_2K,o1_x_2K, o1_y_2K, o1_z_2K, o2_x_2K, o2_y_2K, o2_z_2K,o3_x_2K, o4_x_2K, c11_2K, c12_2K, c44_2K, parametro_rede_a_50K, zr_x_50K, w1_x_50K, w2_x_50K, o1_x_50K, o1_y_50K, o1_z_50K, o2_x_50K, o2_y_50K, o2_z_50K, o3_x_50K, o4_x_50K, c11_50K, c12_50K, c44_50K, parametro_rede_a_100K, zr_x_100K, w1_x_100K, w2_x_100K, o1_x_100K, o1_y_100K, o1_z_100K, o2_x_100K, o2_y_100K, o2_z_100K, o3_x_100K, o4_x_100K, c11_100K, c12_100K, c44_100K, parametro_rede_a_150K, zr_x_150K, w1_x_150K, w2_x_150K, o1_x_150K, o1_y_150K, o1_z_150K, o2_x_150K, o2_y_150K, o2_z_150K,o3_x_150K, o4_x_150K, c11_150K, c12_150K, c44_150K, parametro_rede_a_200K, zr_x_200K, w1_x_200K, w2_x_200K, o1_x_200K, o1_y_200K, o1_z_200K, o2_x_200K, o2_y_200K, o2_z_200K, o3_x_200K, o4_x_200K, c11_200K, c12_200K, c44_200K, parametro_rede_a_250K, zr_x_250K, w1_x_250K, w2_x_250K, o1_x_250K, o1_y_250K, o1_z_250K, o2_x_250K, o2_y_250K, o2_z_250K, o3_x_250K, o4_x_250K, c11_250K, c12_250K, c44_250K, parametro_rede_a_293K, zr_x_293K, w1_x_293K, w2_x_293K, o1_x_293K, o1_y_293K, o1_z_293K, o2_x_293K, o2_y_293K, o2_z_293K, o3_x_293K, o4_x_293K, c11_293K, c12_293K, c44_293K = saida.busca_valores_arquivo_saida (arquivo_saida)
        
        custo_total, parametros, posicoes, constantes = funcao_custo(parametro_rede_a_2K, zr_x_2K, w1_x_2K, w2_x_2K,
                 o1_x_2K, o1_y_2K, o1_z_2K, o2_x_2K, o2_y_2K, o2_z_2K, 
                 o3_x_2K, o4_x_2K, c11_2K, c12_2K, c44_2K,#------------------------------------------------
                 parametro_rede_a_50K, zr_x_50K, w1_x_50K, w2_x_50K,
                 o1_x_50K, o1_y_50K, o1_z_50K, o2_x_50K, o2_y_50K, o2_z_50K, 
                 o3_x_50K, o4_x_50K, c11_50K, c12_50K, c44_50K,#-------------------------------------------
                 parametro_rede_a_100K, zr_x_100K, w1_x_100K, w2_x_100K,
                 o1_x_100K, o1_y_100K, o1_z_100K, o2_x_100K, o2_y_100K, o2_z_100K, 
                 o3_x_100K, o4_x_100K, c11_100K, c12_100K, c44_100K,#------------------------------------------------
                 parametro_rede_a_150K, zr_x_150K, w1_x_150K, w2_x_150K,
                 o1_x_150K, o1_y_150K, o1_z_150K, o2_x_150K, o2_y_150K, o2_z_150K, 
                 o3_x_150K, o4_x_150K, c11_150K, c12_150K, c44_150K,#------------------------------------------------
                 parametro_rede_a_200K, zr_x_200K, w1_x_200K, w2_x_200K,
                 o1_x_200K, o1_y_200K, o1_z_200K, o2_x_200K, o2_y_200K, o2_z_200K, 
                 o3_x_200K, o4_x_200K, c11_200K, c12_200K, c44_200K,#------------------------------------------------
                 parametro_rede_a_250K, zr_x_250K, w1_x_250K, w2_x_250K,
                 o1_x_250K, o1_y_250K, o1_z_250K, o2_x_250K, o2_y_250K, o2_z_250K, 
                 o3_x_250K, o4_x_250K, c11_250K, c12_250K, c44_250K,#-------------------------------------------
                 parametro_rede_a_293K, zr_x_293K, w1_x_293K, w2_x_293K,
                 o1_x_293K, o1_y_293K, o1_z_293K, o2_x_293K, o2_y_293K, o2_z_293K, 
                 o3_x_293K, o4_x_293K, c11_293K, c12_293K, c44_293K)
    else:
        custo_total = definicoes.penalidade
        parametros = definicoes.penalidade/3
        posicoes = definicoes.penalidade/3
        constantes = definicoes.penalidade/3
    
    return custo_total, parametros, posicoes, constantes

#--------------------------------------------------------------------------------------------------


