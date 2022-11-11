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
        u,v,t,l=a
        if(not v in list(graphe_input[u].keys())):
            graphe_input[u][v]=[]
        graphe_input[u][v].append((t,l))
                          
    res={}
    for k,_ in graphe_input.items():
        res[k]=[INF,'',INF]
    if(not x in res.keys()):
        return []
    res[x][0]=0
    liste_a_etendre=[]
    for elem in sommets:
        liste_a_etendre.append(elem)
    res=djikstraSUB(graphe_input,x,res,0,liste_a_etendre,1,y)
    
    chemin=[y]
    noeud=y
    while(noeud!='' and noeud!=x) and noeud in res.keys():
        _,noeud,_=res[noeud]
        chemin=[noeud]+chemin
    if(noeud==''):
        return []
    if(y==x):
        return [x]
    return chemin

def djikstraSUB(graphe_input,node,res,distance_sommet,liste_a_etendre,jour,y):
    voisins=graphe_input[node]
    for noeud_v,liste_t in voisins.items():
        for t,l in liste_t:
            if((distance_sommet+1<res[noeud_v][0] and t>=jour) or ):
                res[noeud_v][0]=distance_sommet+1
                res[noeud_v][1]=node
                res[noeud_v][2]=t+l
                
    liste_a_etendre.remove(node)
    minimum=INF
    new_jour=0
    res2=res
    for elem in liste_a_etendre:
        new_jour=res[elem][2]
        res=djikstraSUB(graphe_input,elem,res,res[elem][0],liste_a_etendre,new_jour,y)
        if(res[y][0]<minimum):
            minimum=res[y]
            res2=res
        print(res2)
    return res2

#####################TEST#####################
graphe=lectureGrapheTOuF()

print(djikstraMain(graphe,'a','l'))




