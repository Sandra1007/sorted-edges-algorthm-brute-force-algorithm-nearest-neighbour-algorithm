#algoritam sorted edges

rj={
0:1 ,#koliki je stupanj svakog vrha
1:0,
2:0,
3:0,
}

import csv
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
    print(lines)
        
    return lines

def Sortiraj(lines):
    
    niz1=[]
    niz2=[]
    niz3=[]
    niz4=[]
    for x in lines[1:]:
        for y in range(1,5):
            if(x[y]==0): # 0 0 160 3082 1639 -> 0 ide u 0 za indeks 0, 0->1 za160
                continue
            else:
                niz1.append(x[0])
                niz2.append(y-1)
                niz3.append(x[y])
                niz4=tuple(zip(niz1,niz2,niz3)) #spoji sve
                
    niz4=sorted(niz4, key=lambda x:x[2]) #sortiraj po tezini

    return niz4

def IsIn(prvi, drugi,visited):
    brojac=0
    brojac2=0
    for x in visited: #provjerava se je li nastao trokut i pravokutnik i tako
        if(prvi in x and drugi in x):
            brojac2=2
        elif(drugi in x):
            brojac=brojac+1
        elif(prvi  in x):
            brojac=brojac+1

    if(brojac==2 or brojac2==2):
        vrijednost=True
    else:
        vrijednost=False
    
    return vrijednost #vratite true ako postoji mogucnost trokuta il pravokutnika bez svih vrhova, inace false

def SortedEdges(niz4):
    d=len(niz4)
    brojac=0
    for x in range(0,d): #uzima se zadnji element da se doda
        brojac=brojac+1#dodaje se zadnji(npr.(0,1), (1,3) ako bude (3,0) ni jedan od ta dva broja ne bi triba bit jer bi nasta trokut
        if(brojac==d-1): #a zadnji svakako imaju brojevi u prethodnim pa se doda
            zadnja_vrijednost=niz4[x] #alazi se zadnji element

    visited=[[0,1,160]] #postavlja se da je prvi posjecen
    for x in niz4:
        if(rj[x[0]]>=3): #ako je stupanj veci od 3 prijedi na drugi element
            continue
        elif(rj[x[0]]<3 and not IsIn(x[0],x[1],visited)): #ako je stupanj manji od 3 i od tuplea se brojevi ne ponavljaju u prethodnim
            rj[x[0]]=rj[x[0]]+1 #povecaj stupanj vrha iz kojeg se ide
            visited.append(x) #dodaj u visited
    
    print(visited)
    
    
    visited.append(zadnja_vrijednost)
    print(visited)



lines=CitajDatoteku()
niz4=Sortiraj(lines)
SortedEdges(niz4)