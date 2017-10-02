import sys
from glob import glob
import saida

if len(sys.argv)<2:
    print 'Utilize o ID como argumento de entrada'
elif len(sys.argv)>2:
    print 'Somente um argumento deve ser informado'

def get_a(ID):
    arquivo=glob('tmp/%s/*.gout'%ID)[0]
    linhas_arquivo_saida = saida.le_linhas_arquivo_saida(arquivo)
    return saida.busca_parametros_de_rede(linhas_arquivo_saida)

parametros = get_a(sys.argv[1])
print '  T(K)  |  a (A)  '
print '----------------------'
print '    2   |  %s'%parametros[0]
print '   50   |  %s'%parametros[1]
print '  100   |  %s'%parametros[2]
print '  150   |  %s'%parametros[3]
print '  200   |  %s'%parametros[4]
print '  250   |  %s'%parametros[5]
print '  293   |  %s'%parametros[6]