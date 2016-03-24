#with open('teste2.cnv') as inputfile:
 #   for line in inputfile:
  #      al = line.strip()

import sys
sys.stdout=open("test.cnv","w")

fi = open('teste3.cnv', 'r')
for l in fi:
    cnvp = l.strip()
    print(cnvp)


