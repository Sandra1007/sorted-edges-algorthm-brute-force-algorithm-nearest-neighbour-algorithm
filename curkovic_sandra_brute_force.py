import csv
import numpy as np
import itertools

#brute force prolazi kroz sve i trai najbolju opciju
def CitajDatoteku():
    with open('bruteforce_sortededges.csv',"r") as f:
        lines=[]
        reader=csv.reader(f,delimiter=",")
        for x in reader:
            lines.append(x)
        
        
        for x in lines[1:]: #preskacen prvu listu jer su u njoj samo imena gradova
            for y in range(0,5): #preskacen prvi element liste u listi jer je u njoj ime grada
                if(x[y]=='-'):
                    x[y]=0
                else:
                    x[y]=int(x[y])
    
    return lines

def NapraviMatricu(lines):
    brojac=0
    for x in lines[1:]:
        brojac=brojac+1 #koliko redova ima
    print(brojac)
    s=(brojac,brojac)
    matrica=np.zeros(s) #popuni matricu za pocetak nulama


    for x in lines[1:]:
        for y in range(1,brojac+1): #4 su reda, ali brojac+1 jer je 5 elemenata u jednom redu
            matrica[x[0],y-1]=x[y]

    return matrica
  
def Brute_force(matrica):
    print(matrica)
    kombinacije=[0,1,2,3]   # 4 su broja u matrici pa 4 kombinacije pocevsi od 0
    sve_kombinacije=list(itertools.permutations(kombinacije)) #sve kombinacije od 4 broja
    print(sve_kombinacije)
    zbroj=0
    lista_zbrojeva=[]
    for x in sve_kombinacije:
        for y in range(0,4):#jer su 4 elementa
            zbroj=zbroj+matrica[x[y],y] #prva.komb. 0 1 2 3,npr. 0 i indeks 0 ->matrica[0][0](vrijednost)
        lista_zbrojeva.append(zbroj) #stavi sve u listu da se kasnje pronade koji je najmanji
        zbroj=0 #resetiraj zbroj inace bi zbrajalo taj zbroj plus novo
    #print(lista_zbrojeva)
    #print(lista_zbrojeva)
    return lista_zbrojeva
     
def PronadiNajmanji(lista_zbrojeva):
    najmanja_udaljenost=min(lista_zbrojeva[1:]) # #kreni od drugog jer je prvi zbroj 0 kako su se zbarajle udaljenost od istog grada do drugog istog 0+0+0+0=0
    print("Najmanja udaljenost je: " +str(najmanja_udaljenost))


    
lines=CitajDatoteku()
matrica=NapraviMatricu(lines)
lista_zbrojeva=Brute_force(matrica)
PronadiNajmanji(lista_zbrojeva)
