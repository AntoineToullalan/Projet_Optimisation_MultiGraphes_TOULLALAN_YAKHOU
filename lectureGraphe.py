import os
from math import sqrt
import random
from tkinter import *

"""Un graphe sera représenté par le tuple (set(int),set(int*int*int*int)) où set(int)
est l'ensemble des sommets et set(int*int*int) est l'ensemble des arêtes pondérées"""


def lectureGrapheTOuF():
    choix = input("Taper 't' pour entrer le graphe sur le terminal,\n 'f' pour lire le graphe sur un fichier \n")
    while(choix!='t' and choix!='f'):
        print("Choix Invalide")
        choix = input("Taper 't' pour entrer le graphe sur le terminal,\n 'f' pour lire le graphe sur un fichier \n")
    if(choix=='t'):
        graphe=entreeTerminal()
    else:
        graphe=entreeFichier()
    return graphe

def entreeTerminal():
    sommets=set()
    aretes=set()
        
    n_str=input("nombre de sommets : ")
    m_str=input("nombre d'arêtes : ")
    print("Entrez les "+n_str+" sommets")
    for i in range(int(n_str)):
        s=input("sommet n°"+str(i+1)+" : ")
        sommets.add(s)
    print("Entrez les "+m_str+" arêtes sous forme (u,v,t,lambda)")
    for i in range(int(m_str)):
        a=input("arête n°"+str(i+1)+" : ")
        a=a[1:-1] #on enleve les parenthèses
        liste_a=a.split(',') #on extrait les 4 valeurs
        if(len(liste_a)!=4 or not liste_a[0] in sommets or not liste_a[1] in sommets):
            print("Saisie Invalide")
            return 
        aretes.add((liste_a[0],liste_a[1],int(liste_a[2]),int(liste_a[3])))
    return (sommets,aretes)

def entreeFichier():
    sommets=set()
    aretes=set()
    
    nom_fichier=input("Entrez le nom du fichier : \n")
    graphText=open(nom_fichier,"r")
    lignes=graphText.readlines()
    n=int(lignes[0].replace('\n',''))
    m=int(lignes[1].replace('\n',''))
    for i in range(2,n+2):
        sommets.add(lignes[i].replace('\n',''))
    for i in range(n+2,m+n+2):
        a=lignes[i].replace('\n','')
        a=a[1:-1]
        liste_a=a.split(',')
        aretes.add((liste_a[0],liste_a[1],int(liste_a[2]),int(liste_a[3])))
    return (sommets,aretes)

def generateurMultiGraphe(n,p,tdebut,tfin):
    #Pour éviter les cycles, on divise les sommets en niveaux, les arêtes ne se font 
    #que d'un niveau i à un niveau i+1
    
    listes_sommet=[chr(i+ord('a')) for i in range(n)]
    listes_aretes=[]
    niveaux=[listes_sommet[i:i+int(sqrt(n))] for i in range(0,n,int(sqrt(n)))]
    for i in range(len(niveaux)-1):
        for sommet1 in niveaux[i]:
            for sommet2 in niveaux[i+1]:
                if(random.random()<p):
                    #on lie les sommet1 et sommet2 par un nombre arbitraire d'arêtes (entre 1 et 3)
                    for _ in range(random.randrange(1,4)):
                        listes_aretes.append((sommet1,sommet2,random.randrange(tdebut,tfin),1))

    return(set(listes_sommet),set(listes_aretes)) 

#######################TEST####################
#print(generateurMultiGraphe(5,0.5,2,9))






