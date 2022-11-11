from gurobi_cheminIV import cheminIV_Gurobi
from lectureGraphe import generateurMultiGraphe
from grapheChemins import chemins,newGraphe,cheminIV
from math import log
from time import time

tdebut=1
tfin=50
liste_temps1=[]
liste_temps2=[]
p=0.5
liste=[i for i in range(2,250,5)]
nb_repetitions=5
for nb_sommets in liste:
    pt1=0
    pt2=0
    for _ in range(nb_repetitions):
        graphe=generateurMultiGraphe(nb_sommets,p,tdebut,tfin)
        sommets,_=graphe
        x=sommets.pop()
        y=sommets.pop()
        sommets.add(x)
        sommets.add(y)
        t1=time()
        cheminIV_Gurobi(graphe,x,y,1,tfin)
        t2=time()
        
        pt1+=(t2-t1)/nb_repetitions
        
        t1=time()
        new_graphe=newGraphe(graphe)
        cheminIV(new_graphe,x,y)
        t2=time()
        
        pt2+=(t2-t1)/nb_repetitions
    liste_temps1.append(log(pt1))
    liste_temps2.append(log(pt2))
print(liste_temps1)
print(liste_temps2)
print([log(i) for i in liste])

