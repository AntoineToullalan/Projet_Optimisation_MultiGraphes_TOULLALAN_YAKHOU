from gurobi_cheminIV import cheminIV_Gurobi
from lectureGraphe import generateurMultiGraphe,lectureGrapheTOuF
from grapheChemins import chemins,newGraphe,cheminIV
INF=10**6

graphe=lectureGrapheTOuF()
x=input("entrez le sommet de départ : ")
y=input("entrez le sommet de d'arrivée' : ")
#On calcul tdebut et tfin car ce sont des arguments de la fonction cheminIV_Gurobi
sommets,aretes=graphe
tdebut=INF
tfin=0
for a in aretes:
    u,v,t,l=a
    if(t<tdebut):
        tdebut=t
    if(t+l>tfin):
        tfin=t+l
print("Le résultat du calcul du chemin 4 avec Gurobi :")        
print(cheminIV_Gurobi(graphe,x,y,tdebut,tfin))
print()
print("Calcul des chemins 1,2,3,et 4 sans gurobi : ")
chemins(graphe,x,y,tdebut,tfin)


