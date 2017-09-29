from glob import glob
import saida

lista = glob('tmp/*/*.gout')

for arquivo in lista:
    linhas_arquivo_saida = saida.le_linhas_arquivo_saida(arquivo)
    parametros = saida.busca_parametros_de_rede(linhas_arquivo_saida)
    if parametros[0]>parametros[6]:
        print '========================================================================='
        print arquivo
        print parametros
        print '========================================================================='
