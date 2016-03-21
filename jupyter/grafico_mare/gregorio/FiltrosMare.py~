#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-
#
# ----------------------------------------------
# Autor:SC/CC Oc.Gregório Luiz Galvão Teixeira -
# Rede de Modelagem Oceanográfica	       -
# Centro de Hidrografia da Marinha, Edificio 8 -
# Rua Barão de Jaceguay, S/N - Ponta da Areia  -
# 24048-900, Niterói - RJ, Brasil	       -
# Tel: + 55 21 2189-3610		       -
# Cel: + 55 21 8040-4243		       -
#					       -
# Situação: Em Construção		       -
# ----------------------------------------------
#
"""
Created on Thu Nov 09 11:08:27 2012
@author: gregorio
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math

#scipy
import scipy as sp
from scipy.io import netcdf
#pylab
from pylab import *
#numpy
import numpy
import numpy as np
import numpy.ma
from numpy import ma
#sistema operacional
import os
import sys
#matplotlib

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.dates import date2num
import re
import time
import datetime as DT
from datetime import datetime
from datetime import date, datetime, timedelta
import matplotlib.dates as mdates

os.system("clear")

# Lendo o arquivo de saida em .txt padrão do HYDRAS3.
caminho_dadosB = "/home/gregorio/Documentos/PYTHON/teste/FISCAL_01012013_31122013.txt"
print caminho_dadosB
f = open(caminho_dadosB)

# Questionando a estação
y = raw_input('Qual a estação que será analisada?Ex.: "ILHA DA MARAMBAIA"')
nomest = y

#r = raw_input('Qual o nome do eixo Y?Ex.: "eixo Y"')
nomeY = "Altura"

#v = raw_input('Qual o nome do eixo X?Ex.: "eixo X"')
nomeX = "Dias"

# Questionando o fator de escala ---------- O FATOR DE ESCALA SERÁ CONSIDERADO FIXO DE 1.
#z = raw_input('Qual o fator de escala para os dados de altura(cm)?Ex.: 1 ')
#fatesc = z
#print fatesc
fatesc = 1

# Verificando o numero de dados
linhas = f.readlines()
shape = np.shape(linhas)
numdados = shape[0]
print numdados

# Questionando o dia inicial e final de interesse.
#diai,mesi,anoi = raw_input('Insira o dia inicial da série de maré. Ex.: 21 1 2014').split()
#diaf,mesf,anof = raw_input('Insira o dia final da série de maré. Ex.: 21 1 2014').split()
#diai = '{0:02.0f}'.format(float(diai))
#mesi = '{0:02.0f}'.format(float(mesi))
#anoi = '{0:04.0f}'.format(float(anoi))
#diaf = '{0:02.0f}'.format(float(diaf))
#mesf = '{0:02.0f}'.format(float(mesf))
#anof = '{0:04.0f}'.format(float(anof))

################################################################################################
vecAB = np.zeros(numdados,)
vecHB = ["" for x in range(numdados)]
vecDB = ["" for x in range(numdados)]



#Deve ser somado um dia a mais ja que o metodo "diff" não inclui a ultima data de interesse no vetor.




# Lendo todas as linhas do arquivo e separando as colunas em ";".
#-----SEPARANDO DADOS DO RESTO, ENTRE OS DADOS E O RESTO DEVE HAVER DOIS ESPAÇOS --------------------------------
a = 0
for l in linhas:
	linhas2=l.strip().split("  ")
	vecAB[a] = linhas2[1]
	a = a+1

c = 0
for l in linhas:
	linhas2=l.strip().split("  ")
	vecDB[c] = linhas2[0]
	c = c+1

di = vecDB[0]
df = vecDB[(numdados-1)]
#----------------------------------------------------------------------------------------------------------------

d1 = di.strip().split(" ")
d1D = d1[0]
shaped1 = np.shape(d1)
if shaped1[0] <= 1:
	houri = 0
	minutei = 0
else:
	d1H = d1[1]
	d1HS=d1H.strip().split(":")
	houri = d1HS[0]
	minutei = d1HS[1]


d2 = df.strip().split(" ")
d2D = d2[0]
shaped2 = np.shape(d2)

if shaped2[0] <= 1:
	hourf = 0
	minutef = 0
else:
	d2H = d2[1]
	d2HS=d2H.strip().split(":")
	hourf = d2HS[0]
	minutef = d2HS[1]


d1DS=d1D.strip().split("/")
diai = d1DS[0]
mesi = d1DS[1]
anoi = d1DS[2]

#print anoi,mesi,diai,houri,minutei

d2DS=d2D.strip().split("/")
diaf = d2DS[0]
mesf = d2DS[1]
anof = d2DS[2]

#print anof,mesf,diaf,hourf,minutef

#escrevendo os vetores de dias
delta = 60
v = raw_input('A taxa de amostragem destes dados estão configuradas em 10 minutos. É a variável "delta" na linha 159 do programa. CLIQUE ENTER PARA CONTINUAR...')


d1 = DT.datetime(int(anoi),int(mesi),int(diai),int(houri),int(minutei))
d2 = DT.datetime(int(anof),int(mesf),int(diaf),int(hourf),int(minutef))
def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta
b = 0
for result in perdelta(d1, d2+timedelta(minutes=delta), timedelta(minutes=delta)):
	vecHB[b] = result
	b = b+1


fig = plt.figure(figsize=(18, 8))
plt.plot_date(x=vecHB, y=vecAB, fmt="r-",linewidth=2)
plt.title(nomest+" "+str(di)+" "+"a"+" "+str(df),fontsize = 24)
plt.ylabel(nomeY,fontsize = 18)
plt.xlabel(nomeX,fontsize = 18)
plt.grid(True,linewidth=2)
plt.show()

#Filtrando os dados por sucessivas medias moveis

def movingaverage(interval, window_size):
    window= numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')


yB_av = movingaverage(vecAB, 25)
yB_av_av = movingaverage(yB_av, 24)
yB_av_av_av = movingaverage(yB_av_av, 25)
plt.plot_date(x=vecHB[35:-35], y=vecAB[35:-35], fmt="r-",linewidth=2)
plt.plot_date(x=vecHB[35:-35], y=yB_av_av_av[35:-35], fmt="k-",linewidth=2)
plt.title("NMDmedmov"+' '+nomest+" "+str(di)+" "+"a"+" "+str(df),fontsize = 24)
plt.ylabel(nomeY,fontsize = 18)
plt.xlabel(nomeX,fontsize = 18)
plt.grid(True,linewidth=2)
plt.show()






#Extraindo apenas mare da elevacao do nivel do mar por GODIN
MareAstro = vecAB[35:-35]-yB_av_av_av[35:-35]
plt.plot_date(x=vecHB[35:-35], y=MareAstro, fmt="r-",linewidth=2)
plt.title("MareAstro -"+' '+nomest+" "+str(di)+" "+"a"+" "+str(df),fontsize = 24)
plt.ylabel(nomeY,fontsize = 18)
plt.xlabel(nomeX,fontsize = 18)
plt.grid(True,linewidth=2)
plt.show()



# Exportando o NMDmedmov
nomesaidaMedMov = nomest+"_"+str(diai).zfill(2)+str(mesi).zfill(2)+str(anoi).zfill(4)+"_"+str(diaf).zfill(2)+str(mesf).zfill(2)+str(anof).zfill(4)+"_nmdMedMov"+".txt"
numpy.savetxt(nomesaidaMedMov, (yB_av_av_av[35:-35]),fmt='%3.1i')

# Exportando o MAREastro
nomesaidaMareastro = nomest+"_"+str(diai).zfill(2)+str(mesi).zfill(2)+str(anoi).zfill(4)+"_"+str(diaf).zfill(2)+str(mesf).zfill(2)+str(anof).zfill(4)+"_Mareastro"+".txt"
numpy.savetxt(nomesaidaMareastro, (MareAstro),fmt='%3.1i')
