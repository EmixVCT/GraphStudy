#coding : UTF-8
class GraphNo:
    """graphe code par liste d'adjacence. Les sommets
    devront etre numerotes 0, 1, 2, ..., n-1"""
   
    def __init__(self, l_adj):
        """initialise un graphe d'apres la liste d'adjacence
        l_adj et son orddre n"""
       
        self.ordre = len(l_adj)    #attribut ordre = nb de sommet
        self.adj = l_adj        #attribut liste adjacence
       
    def affiche(self):
        return "ordre : " +  str(self.ordre) + ", liste d'adjacence : "+ str(self.adj)
       
    def degre(self,sommet):
        return len(self.adj[sommet])
       
       
    def taille(self):
        taille = 0
        for i in range(self.ordre):
            taille += len(self.adj[i])
           
        return taille/2
   
    def composanteConnexe(self,i):
        connu = [False]*self.ordre
        connu[i] = True #considere le sommet de depart connu
        file_attente = [] #manipuler avec append et pop
        file_attente.append(i) #ajoute le sommet de depart dans la file
       
        while file_attente:
            courant = file_attente.pop(0)
            for sommet in self.adj[courant]:
                if not connu[sommet]:
                    file_attente.append(sommet)
                    connu[sommet] = True

        sommet_connexe = []
        for c in range(len(connu)):
            if connu[c]:
                sommet_connexe.append(c)
               
        return sommet_connexe
       
    def nbComposantesConnexes(self):
        n = 0
        connu = [False]*self.ordre
        for sommet in range(self.ordre):
            if not connu[sommet]:
                liste = self.composanteConnexe(sommet)
                for som in liste:
                    connu[som] = True
                n = n+1
               
        return n
       

'''
liste = [[1,2],[0,3],[0,3],[1,2]]
graph_test = GraphNo(liste)
print graph_test.affiche()
print graph_test.degre(0)
print graph_test.taille()
'''

def graphComplet(n):
    list_adj = []
    for sommet in range(n):
        adjacence = []
        for arete in range(n):
            if sommet != arete:
                adjacence.append(arete)
        list_adj.append(adjacence)
       
    return GraphNo(list_adj)
   
"""
graph_test = graphComplet(5)
print graph_test.affiche()
"""

def cycle(n):
    list_adj = []
    for sommet in range(n):
        adjacence = []
        for arete in range(sommet,sommet+1):
            if sommet == 0:
                adjacence.append(arete+1)
                adjacence.append(n-1)
            elif sommet == n-1:
                adjacence.append(0)
                adjacence.append(arete-1)
            else:
                adjacence.append(arete-1)
                adjacence.append(arete+1)
        list_adj.append(adjacence)
    return GraphNo(list_adj)
"""
graph_test = cycle(5)
print graph_test.affiche()
"""

def aretes_vers_liste_adj(list_art,n):
    list_adj = [[] for i in range(n)]
   
    for arete in range(len(list_art)):
        list_adj[list_art[arete][0]].append(list_art[arete][1])
        list_adj[list_art[arete][1]].append(list_art[arete][0])
       
    return GraphNo(list_adj)
   
'''
graph_test = aretes_vers_liste_adj([[1,4],[0,3],[4,3],[1,2],[0,2]],5)
print graph_test.affiche()
'''

def lireAretesEtOrdre(nomdufichier):
    """lit le fichier et renvoie la liste des aretes qui s'y trouvent
    ainsi que l'ordre"""
    f = file(nomdufichier, 'r')
    lignes = f.readlines()
    #on extrait les lignes qui commencent par 'E'
    #si c'est bon on cree une nouvelle arete
    aretes = []
    ordre = 0
    for l in lignes:
        mots = l.split()
        if len(mots) >= 3 and mots[0]=='E':
            aretes.append([int(mots[1]), int(mots[2])])  #ATTENTION ne pas oublier la conversion str en int
        if len(mots) > 0 and mots[0]=="ordre":
            ordre = int(mots[1])
    return aretes, ordre


def lireGraphNO(nomDuFichier):
    arete,ordre = lireAretesEtOrdre(nomDuFichier)
    list_adj = aretes_vers_liste_adj(arete,ordre)
    return list_adj
   
   
"""print lireGraphNO("metro.txt").taille()"""


liste = [[1,2],[0,4,5],[0,3],[2,4],[1,3],[1],[7],[6]]
graph = GraphNo(liste)
print (graph.composanteConnexe(2))

"""
print (len(lireGraphNO("composantes7.txt").composanteConnexe(333)))

print ("NbComposanteConnexes : ")
print ("composantes0.text : " + str(lireGraphNO("composantes0.txt").nbComposantesConnexes()))
print ("composantes1.text : " + str(lireGraphNO("composantes1.txt").nbComposantesConnexes()))
print ("composantes2.text : " + str(lireGraphNO("composantes2.txt").nbComposantesConnexes()))
"""
