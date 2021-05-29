import csv

#algoritam najblizeg susjeda

def CitajDatoteku():
    with open('distance.csv',"r") as f:
        lines=[]
        reader=csv.reader(f,delimiter=",")
        for x in reader:
            lines.append(x)
        
        
        for x in lines[1:]: #preskacen prvu listu jer su u njoj samo imena gradova
            for y in range(1,38): #preskacen prvi element liste u listi jer je u njoj ime grada
                if(x[y]=='-'):
                    x[y]=0
                else:
                    x[y]=int(x[y])
    
    return lines

def GradoviuDrugiNiz(lines):
    niz=[]
    for x in lines[0:1]: #da mi procita samo prvu liniju gdje su samo gradovi 
        for y in range(1,37):
            niz.append(x[y])
        
    return niz

def traziSusjede(lines, niz_gradova):
    gradovi_koji_su_bili=['Amsterdam']
    grad='Amsterdam'
    lista_indexa_minimuma=[0]
    brojac_x=0
    preskoci=True
    brojac_jesu_li_svi_iskoristeni=1 #stavljeno da se vidi ako su svi gradovi iskoristeni da se nadoda prvi 
    while(preskoci):
        
        for x in lines[1:]: #preskoci prvu liniju di su samo  gradovi    
            min=10000 #resetiraj min svaki put kad se trazi novi minimum
            brojac_x=brojac_x+1 #broji jesmo li dosli do kraja vanjske petlje, i ako jesmo, resetiraj je
            if(grad==x[0]): #ako smo nasli grad koji trazimo (prethodni ga je izabrao ko najmanju udaljenost)
                preskoci=False
                for y in range(1,38): #citaj od 1 jer je prvi opet grad, trebaju se usporedivati brojevi
                    if(x[y]==0): #ako je 0, tj. ako grad usporeduje samo sa sobon, preskoci
                        continue

                    elif(x[y]<min and (y-2 not in lista_indexa_minimuma)): 
                        min=x[y] # y-1 jer prvi red ima element vise neg donji pa da se zna koji index se vec koristio, tj. koji grad
                        index=x.index(min) #zapamti se index od minumuma
        

                gradovi_koji_su_bili.append(niz_gradova[index-1]) #da se zna koji su gradovi bili, tj iskoristeni
                grad=niz_gradova[index-1] #prva linija ima element manje neg ostale, jer je svaki grad naveden opet u liniji ispod
                lista_indexa_minimuma.append(index-1) #zapamti na kojem su indexu koristeni gradovi tako da se taj index preskoci
                brojac_jesu_li_svi_iskoristeni=brojac_jesu_li_svi_iskoristeni+1
                
                if(brojac_jesu_li_svi_iskoristeni==37):
                    gradovi_koji_su_bili.append('Amsterdam')
                    break
            
        
        if(brojac_x==37): #ako smo dosli do kraja for vanjske, resetiraj je
            brojac_x=0
            preskoci=True
            
            

    print(gradovi_koji_su_bili)
          



lines=CitajDatoteku()
niz_gradova=GradoviuDrugiNiz(lines)
traziSusjede(lines,niz_gradova)
