import sys
from glob import glob
import saida



if len(sys.argv)>1:
    num=sys.argv[1]
else:
    num=15

with open('stdout.txt','r') as f:
    linhas = f.readlines()
    
def get_a(ID):
    arquivo=glob('tmp/%s/*.gout'%ID)[0]
    linhas_arquivo_saida = saida.le_linhas_arquivo_saida(arquivo)
    return saida.busca_parametros_de_rede(linhas_arquivo_saida)    
    
A=[]
for n,l in enumerate(linhas,0):
    if 'Custo' in l:
        c=float(l.split()[1])
        if c < 2000:
            i = linhas[n-10].split()[2]
            date = linhas[n-9].strip('#').rstrip('#\n')
            parametros = get_a(i)
            if parametros[0] > parametros[-1]:
                A.append([i, c, parametros[0], parametros[-1],date])
            
            
def getKey(item):
    return item[1]
Asorted = sorted(A, key=getKey)
for item in Asorted[:num]:
    print item