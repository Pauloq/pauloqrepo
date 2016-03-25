arquivo = input('Nome do arquivo:')
fiss = open(arquivo, 'r', encoding = "cp860")
results = []
for i in fiss:
    results.append(i)

partenemea = open('NEMEA.txt', 'r')
results2 = []
for n in partenemea:
    results2.append(n)
    

#Lat
alat = results[14]
blat = str(alat)
clat = blat[4:15]
clat

alati = results2[0]
blati = str(alati)
clati = blati[0:17] + ' ' + clat
clati

partenemea = open('NEMEA.txt', 'r')
results2 = []
for n in partenemea:
    results2.append(n)
    
#LAT
alati = results2[0]
blati = str(alati)
clati = blati[0:17] + ' ' + clat
clati

#LON
alon = results[15]
blon = str(alon)
clon = blon[4:16]
clon

aloni = results2[1]
bloni = str(aloni)
cloni = bloni[0:18] + ' ' + clon
cloni

#DATA
import datetime

adat = results[16]
bdat = str(adat)
cdat = bdat[5:15]

ahor = results[16]
bhor = str(ahor)
chor = bhor[16:21]
chor

yearfirst = datetime.datetime.strptime(cdat, "%d/%m/%Y").strftime("%Y-%m-%d")

ina = yearfirst[0:4]
inb = yearfirst[5:7]
inc = yearfirst[8:10]

yyyy = int(ina)
mm = int(inb)
d = int(inc)

#print(yyyy, mm, d)
#print(ina, inb, inc)

month = datetime.date(yyyy, mm, d).strftime('%b')
#month

datared = (month + ' ' + inb + ' ' + ina + ' ' + chor + ':00')
#datared

#data redonda
adati = results2[2]
bdati = str(adati)
cdati = bdati[0:19] + ' ' + datared
cdati

#ULTIMA LINHA
ault = results[15]
bult = str(ault)
cult = bult[4:16]
cult

aulti = results2[1]
bulti = str(aloni)
culti = bulti[0:18] + ' ' + clon
culti

#ARQUIVO DE SAIDA
import sys
sys.stdout = open("baby.cnv","w")
ss = 'AIAIAIAIIAIAIAI'
file = open('semnemea.cnv', 'r', encoding = "cp860")
for line in range(700):
    cc = file.readline()
    ccc = cc.strip()
    print(ccc)
    if ccc.startswith('* System UpLoad Time'):
        print(clati)
        print(cloni)
        print(cdati)
        print(culti)
