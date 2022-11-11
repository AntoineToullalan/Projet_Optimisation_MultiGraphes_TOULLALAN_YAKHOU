from lectureGraphe import lectureGrapheTOuF

INF=10**6
    
def djikstraMain(graphe,x,y):
    #on transforme notre graphe dans un format utilisable par
    #la fonction djikstra
    sommets,aretes=graphe
    graphe_input={}
    for s in sommets:
        graphe_input[s]={}
    for a in aretes:
        u,v,l=a
        graphe_input[u][v]=l
                          
    res={}
    for k,_ in graphe_input.items():
        res[k]=[INF,'']
    if(not x in res.keys()):
        return []
    res[x][0]=0
    liste_a_etendre=[]
    for elem in sommets:
        liste_a_etendre.append(elem)
    res=djikstra(graphe_input,x,res,0,liste_a_etendre)

    chemin=[y]
    noeud=y
    while(noeud!='' and noeud!=x) and noeud in res.keys():
        _,noeud=res[noeud]
        chemin=[noeud]+chemin
    if(noeud==''):
        return []
    return [x]+chemin

def djikstra(graphe_input,node,res,distance_sommet,liste_a_etendre):
    voisins=graphe_input[node]
    for noeud_v,dist in voisins.items():
        if(distance_sommet+dist<res[noeud_v][0]):
            res[noeud_v][0]=distance_sommet+dist
            res[noeud_v][1]=node
    liste_a_etendre.remove(node)
    minimum=INF
    choix=0
    for elem in liste_a_etendre:
        if(minimum>res[elem][0]):
            minimum=res[elem][0]
            choix=elem
    if(choix!=0):
        res=djikstra(graphe_input,choix,res,res[choix][0],liste_a_etendre)
    return res
        
def newGraphe(graphe):
    sommets1,aretes1=graphe
    sommets2=set()
    aretes2=set()
    dic={u:[] for u in sommets1}
    for a1 in aretes1:
        u,v,t,l=a1
        sommets2.add((u,t))
        if(not t in dic[u]):
            dic[u].append(t)
        sommets2.add((v,t+l))
        if(not t+l in dic[v]):
            dic[v].append(t+l)
        aretes2.add(((u,t),(v,t+l),l))
    for s in sommets1:
        liste_t=dic[s]
        liste_t.sort()
        for i in range(len(liste_t)-1):
            aretes2.add(((s,liste_t[i]),(s,liste_t[i+1]),0))
    return (sommets2,aretes2)
        

def chemins(graphe,x,y,td,tf):
    #graphe=lectureGrapheTOuF()
    new_graphe=newGraphe(graphe)
    sommets,aretes=new_graphe
    
    a_eliminerS=[]
    a_eliminerA=[]
    for s in sommets:
        u,t=s
        if(t>tf or t<td):
            a_eliminerS.append(s)
    for a in aretes:
        s1,s2,l=a
        if(s1 in a_eliminerS or s2 in a_eliminerS):
            a_eliminerA.append(a)
            
    for el in a_eliminerS:
        sommets.remove(el)
    for el in a_eliminerA:
        aretes.remove(el)
        
    new_graphe=sommets,aretes  
    
    print("Chemin I : ")
    print(cheminI(new_graphe,x,y))

    print("Chemin II : ")
    print(cheminII(new_graphe,x,y))
    
    print("Chemin III : ")
    print(cheminIII(new_graphe,x,y))
    
    print("Chemin IV : ")
    print(cheminIV(new_graphe,x,y))

def cheminI(graphe,x,y):
    sommets,aretes=graphe
    new_aretes=set()
    a_modifie=[]
    for a in aretes:
        u,v,l=a
        u1,t1=u
        v2,t2=v
        if(l==0 and not (u1==y and v2==y)):
            a_modifie.append(a)
        else:
            new_aretes.add(a)
    for a in a_modifie:
        u,v,l=a
        u1,t1=u
        v2,t2=v
        new_aretes.add((u,v,(t2-t1)))
    depart,arrivee=departArrivee(sommets,x,y)
    new_graphe=sommets,new_aretes
    chemin=djikstraMain(new_graphe,depart,arrivee)
    return TransfoChemin(chemin)
    
def cheminII(graphe,x,y):
    sommets,aretes=graphe
    new_aretes=set()
    a_modifie=[]
    for a in aretes:
        u,v,l=a
        u1,t1=u
        v2,t2=v
        if(l==0 and not (u1==x and v2==x)):
            a_modifie.append(a)
        else:
            new_aretes.add(a)
    for a in a_modifie:
        u,v,l=a
        u1,t1=u
        v2,t2=v
        new_aretes.add((u,v,(t2-t1)))
    depart,arrivee=departArrivee(sommets,x,y)
    new_graphe=sommets,new_aretes
    chemin=djikstraMain(new_graphe,depart,arrivee)
    return TransfoChemin(chemin)

def cheminIII(graphe,x,y):
    sommets,aretes=graphe
    new_aretes=set()
    a_modifie=[]
    for a in aretes:
        u,v,l=a
        u1,t1=u
        v2,t2=v
        if(l==0 and not (u1==y and v2==y) and not(u1==x and v2==x)):
            a_modifie.append(a)
        else:
            new_aretes.add(a)
    for a in a_modifie:
        u,v,l=a
        u1,t1=u
        v2,t2=v
        new_aretes.add((u,v,(t2-t1)))
    depart,arrivee=departArrivee(sommets,x,y)
    new_graphe=sommets,new_aretes
    chemin=djikstraMain(new_graphe,depart,arrivee)
    return TransfoChemin(chemin)

def cheminIV(graphe,x,y):
    sommets,aretes=graphe
    depart,arrivee=departArrivee(sommets,x,y)
    chemin=djikstraMain(graphe,depart,arrivee)
    return TransfoChemin(chemin)

def departArrivee(sommets,x,y):
    depart=(x,INF)
    arrivee=(y,0)
    for s in sommets:
        u,t=s
        if(u==y and t>arrivee[1]):
            arrivee=s
        if(u==x and t<depart[1]):
            depart=s
    return (depart,arrivee)

def TransfoChemin(chemin):
    #on renvoie la liste des sommets visités dans G sommet_chemin et les arêtes 
    #empruntées aretes_chemin. Ainsi l'arête entre sommet_chemin[i] et sommet_chemin[i+1] est aretes_chemin[i]
    sommet_chemin=[]
    aretes_chemin=[]
    if(chemin!=[]):
        u,t=chemin[0]
        sommet_chemin.append(u)
    for i in range(len(chemin)-1):
        u,t=chemin[i]
        u2,t2=chemin[i+1]
        if(u!=u2):
            sommet_chemin.append(u2)
            aretes_chemin.append((u,u2,t))
    return (sommet_chemin,aretes_chemin)

    
##############TEST############
#chemins('a','l',1,20)



