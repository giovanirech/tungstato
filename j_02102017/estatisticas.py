#!/usr/bin/python
import saida, custo, sys, entrada 
import definicoes
import os
import glob

#-----------------------------------------------------------------------#
def informacoes (diretorio, arquivo_saida):
 

    try:

	#sys.stdout = open(os.devnull, "w")
	valor_custo = custo.calcula_custo(arquivo_saida[0])
	sys.stdout = sys.__stdout__

    	#print '####################### ID %s #####################'% diretorio
    	#print '###################################################'
    	#print '   charge O_core: %s'%P[0]
    	#print '   charge O_shell: %s'%(-P[0]-2)
    	#print '   buck Zr-O: A=%s, rho=%s'%(P[1], P[2])
    	#print '   buck W-O:  A=%s, rho=%s'%(P[3], P[4])
    	#print '   buck O-O:  A=%s, rho=%s, C=%s'%(P[5], P[6], P[7])
    	#print '   spring O: K= %s'%P[8]
    	#print '   covexp W-O: D= %s, a= %s, r0= %s'%(P[9], P[10], P[11])
    	#print 'Custo: %s'%valor_custo
    	#print '###########################################################'
	

    except:

	valor_custo = definicoes.penalidade

	#print 'Custo: %s'% definicoes.penalidade
        #print '###########################################################'
 
    return valor_custo

#------------------------------------------------------------------------#
def le_informacoes_arquivos(diretorios):

	dados = []

	for d in diretorios:
		os.chdir(d)
	
		arquivo_saida = glob.glob('*.gout')

		valor_custo = informacoes(d, arquivo_saida)
		dados.append((d,valor_custo))
		os.chdir('..')

	dados.sort(key=lambda x: x[1])
	
	return dados 

#-------------------------------------------------------------------------#
def escreve_dados(dados):
	for d in dados:
		print 'Diretorio: %s  |  Custo: %s' % (d[0], d[1])
		
#======================================================================================

os.chdir('./tmp')

diretorios =  os.listdir('.')   

dados = le_informacoes_arquivos(diretorios)

escreve_dados(dados)


os.chdir('..')
