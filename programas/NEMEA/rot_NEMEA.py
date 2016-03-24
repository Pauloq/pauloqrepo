from pandas import DataFrame, read_csv, datetime, Series, Timestamp
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import numpy as np
from pandas.tseries.offsets import *
import time
import datetime
#%matplotlib inline


local = r'/home/pauloque/programacao/pauloqrepo/jupyter/NEMEA/NEMEA.xlsx'
dfp = pd.read_excel(local)

local2 = r'/home/pauloque/programacao/pauloqrepo/jupyter/NEMEA/cnvs/dMCTV001.xlsx'
dfp2 = pd.read_excel(local2)

cnv = []
for i in dfp2['* Sea-Bird SBE 9 Data File:']:
    cnv.append(i)
    
cnvnemea = []
for k in dfp['Codigo']:
    cnvnemea.append(k)

    
#Dados a serem implemntados no formato nemea

cnvlat = []
for lat in range(len(cnv)):
    if cnv[lat].startswith('**') and cnv[lat].endswith('S'):
        cnvlat.append(cnv[lat])


cnvlon = []
for lon in range(len(cnv)):
    if cnv[lon].startswith('**') and cnv[lon].endswith('W'):
        cnvlon.append(cnv[lon])
 

cnvdat = []
for dat in range(len(cnv)):
    if cnv[dat].startswith('**') and cnv[dat].endswith('Z'):
        cnvdat.append(cnv[dat])

#cnvnemea + latlon         
strlat = str(cnvnemea[0]) + str(cnvlat[0][2:15])

strlon = str(cnvnemea[1]) + str(cnvlon[0][2:16])

        
#ajustando a data para o formato nemea
strdata = str(cnvdat)
datafat = strdata[7:17]
horafat = strdata[18:23]

yearfirst = datetime.datetime.strptime(datafat, "%d/%m/%Y").strftime("%Y-%m-%d")

ina = yearfirst[0:4]
inb = yearfirst[5:7]
inc = yearfirst[8:10]

yyyy = int(ina)
mm = int(inb)
d = int(inc)

#print(yyyy, mm, d)
#print(ina, inb, inc)

month = datetime.date(yyyy, mm, d).strftime('%b')
month

datared = (month + ' ' + inb + ' ' + ina + ' ' + horafat + ':00')
datared

#cnvnemea + data
dataredonda = str(cnvnemea[2]) + ' ' + datared



cnvnemeal = [strlat, strlon, dataredonda, cnvnemea[3]]


#Integrando tudo

cnvredondao = []
for p in cnv:
    cnvredondao.append(p)
    if p == cnv[7]:
        
        for k in range(len(cnvnemeal)):
            cnvredondao.append(cnvnemeal[k])
cnvredondao            
