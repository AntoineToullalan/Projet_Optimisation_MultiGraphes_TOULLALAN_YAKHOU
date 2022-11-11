#!/usr/bin/python

# Copyright 2013, Gurobi Optimization, Inc.

from lectureGraphe import lectureGrapheTOuF
from grapheChemins import newGraphe,departArrivee,TransfoChemin
from gurobipy import *

INF=10**6

def matriceContraintes(liste_sommets,liste_aretes,depart):
    nbcont=len(liste_aretes)+1
    nbvar=len(liste_sommets)
    
    res=[[0 for _ in range(nbvar)] for _ in range(nbcont)]
    b=[0 for _ in range(nbcont)]
    if(depart in liste_sommets):
        res[0][liste_sommets.index(depart)]=1
        b[0]=0
    
    i=1
    for s in liste_aretes:
        u,v,t=s
        res[i][liste_sommets.index(v)]=1
        res[i][liste_sommets.index(u)]=-1
        b[i]=t
        i+=1       
    return (res,b)

def cheminIV_Gurobi(graphe,x,y,td,tf):
    sommets,aretes=newGraphe(graphe)
    depart,arrivee=departArrivee(sommets,x,y)
    liste_sommets=list(sommets)
    liste_aretes=list(aretes)
    
    nbcont=len(aretes)+1
    nbvar=len(sommets)

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    # Matrice des contraintes
    a,b = matriceContraintes(liste_sommets,liste_aretes,depart)
    
    # Coefficients de la fonction objectif
    c = [1 for _ in range(nbvar)]
    
    m = Model("mogplex")     
            
    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.CONTINUOUS,lb=0, ub=tf+1,name=str(liste_sommets[i])))
    
    # maj du modele pour integrer les nouvelles variables
    m.update()
    
    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += c[j] * x[j]
            
    # definition de l'objectif
    m.setObjective(obj,GRB.MAXIMIZE)
    
    # Definition des contraintes
    for i in lignes:
        m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) <= b[i], "Contrainte%d" % i)
    
    # Resolution
    m.optimize()
    
    sol=[]
    for j in colonnes:
        sol.append(x[j].x)
    return gurobiAChemin(sol,liste_aretes,liste_sommets,arrivee,tf)

def ensembleVoisins(liste_aretes,s):
    res=[]
    for a in liste_aretes:
        u,v,l=a
        if(v==s):
            res.append(u)
    return res
    
def gurobiAChemin(sol,liste_aretes,liste_sommets,arrivee,tf):
    chemin=[]
    if(arrivee in liste_sommets):
        i=liste_sommets.index(arrivee)
    else:
        return []
    
    s=arrivee
    while(sol[i]>0 and sol[i]<=tf):
        chemin=[s]+chemin
        voisins=ensembleVoisins(liste_aretes,s)
        index_voisins=[liste_sommets.index(v) for v in voisins]
        minimum=INF
        
        for iv in index_voisins:
            if(liste_sommets[iv][0]!=s[0]):
                #si le voisin est un nouveau sommet, on fait un voyage->cout de 1 car 1 trajet
                if(minimum>sol[iv]+1):
                    i=iv
                    minimum=sol[iv]+1
                    stemp=liste_sommets[iv]
            else:
                if(minimum>sol[iv]):
                    #si le voisin est n'est pas nouveau sommet, il n'y a pas voyage->cout de 0 car 0 trajets
                    i=iv
                    minimum=sol[iv]
                    stemp=liste_sommets[iv]
        s=stemp
    if(sol[i]==0):
        chemin=[s]+chemin
    return TransfoChemin(chemin)

                
        

#############TEST##############
#graphe=lectureGrapheTOuF()
#graphe=({'c', 'd', 'e', 'g', 'a', 'b', 'f'}, {('f', 'g', 5, 1), ('d', 'f', 4, 1), ('a', 'c', 2, 1), ('a', 'c', 1, 1), ('e', 'g', 5, 1), ('e', 'g', 6, 1), ('c', 'e', 3, 1), ('c', 'f', 3, 1), ('b', 'c', 1, 1), ('c', 'f', 4, 1)})
#print(cheminIV_Gurobi(graphe,'a','g',1,20))   
