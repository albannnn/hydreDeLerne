# CLASS TREE
# extension de la classe BinTree �tous les types d'arbres
class Tree:
    """
    Classe Tree
    - Attributs :
        root : La racine root de type N (ou None)
        *children : les enfants de l'arbre du type Tree
        Un arbre vide est représenté par un objet dont la racine est None et aucun enfant n'est passé en arguments, c'est à dire qu'il y a au plus 1 argument
      
    - Condition : Un arbre est vide si et seulement si la racine est non définie
    
    - Méthodes(26) : 
        * Constructeur - Tree(racine, *children)
        * estVide()
        * estFeuille()
        * getFeuilles()
        * racine()
        * countOfChildren()
        * getChildren()
        * getChildrenRacines()
        * getChild()
        * setChild()
        * addChild()
        * delChild()
        * setRacine()
        * getEtage()
        * nodeInTree()
        * parent()
        * hauteur()
        * taille()
        * arite()
        * BFS()
        * DFS()
        *__repr__()
        * __str__()
    
    - Surcharge de plusieurs opérateurs :
        * objet(arbre) >= b -> Renvoie taille(a) >= b 
        * objet(arbre) <= b -> Renvoie taille(a) <= b
        * objet(arbre1) == objet(arbre2) -> Renvoie True si tous les noeuds sont les mêmes
        * objet(arbre1) != objet(arbre2) -> Renvoie True si des noeuds sont différents
        

    """

    def __init__(self, root=None, *children):
        """
        CONSTRUCTOR        
        
        Parameters
        ----------
        root : not bool, value of the root. The default is None -> arbre vide.
        *children : children of the root -> instance of tree or None

        Create a Tree object
        -------
        CONSTRUCTOR

        """
        
        # Pré-condition : tous les enfants doivent être des arbres
        #for child in children:
        #   assert (type(child) == type(self) or child ==  None), f"{child} doit être un Tree ou None"
        # Pré-condition : Une valeur ne peut se trouver 2 fois dans l'arbre
        
        
        self.root = root

        if len(children) == 0:
            self.children = []
        else:
            self.children = [child for child in children]

        # Axiome
        assert self.estVide() == (self.root == None), "Un arbre non vide a une racine"

    # Impressions
    def __str__(self, level=0):
        """ Représentation de l'arbre """
        if self.estVide():
            return ''
        result = ''
        result += '  ' * level + '|' + str(self.racine()) + '\n' 
        for child in self.getChildren():
            
            result += child.__str__(level+1)
        return result
    def __repr__(self):
        return f"<objet Tree : racine = {self.racine()} ; enfants = {self.getChildrenRacines()}"
    
    #Ordre de grandeur 
    def __eq__(self, val):
        """ 2 objets arbres sont égaux lorsque ils ont les memes enfant, la meme racine"""
        if type(self) != type(val):
            return False
        
        if (self.racine() != val.racine()) or \
            (len(self.getChildren()) != len(val.getChildren())):
            return False
        if self.estVide() and val.estVide():
            return True
        else:
            if self.racine() == val.racine():
                list = [self.getChildren()[i] == val.getChildren()[i] for i in range(len(self.getChildren()))]
                if False in list:
                    return False
                return True
            
    def __ne__(self, val):
        return not self.__eq__(val)
        
    def __lt__(self, val):
        return self.taille() < val
    def __gt__(self, val):
        return self.taille() > val
    def __le__(self, val):
        return self.taille() <= val
    def __ge__(self, val):
        return self.taille() >= val

    # Méthodes

    def estVide(self):
        """ Renvoie True si l'arbre est vide False sinon"""
        return (self.racine() == None) and (len(self.children) == 0)

    def estFeuille(self):
        """ Renvoie True si l'arbre est une feuille False sinon (un arbre ne contenant qu'un seul noeud est une feuille)"""
        if False in [elt.estVide() for elt in self.getChildren()]:  # un arbre ayant une feuille a au minimum un enfant donc index = 0
            return False 
        else:
            return True
        
    def getFeuilles(self):
        """ Renvoie le nombre de feuilles de l'arbre"""
        if self.estVide():
            return 0
        if self.estFeuille():
            return 1
        else:
            return sum([elt.getFeuilles() for elt in self.getChildren()])
    def racine(self):
        """ Renvoie la valeur de la racine"""
        return self.root

    def countOfChildren(self):
        """ renvoie le nombre d'enfants"""
        return len(self.children)

    def getChildren(self):
        """ Renvoie la liste des enfants si il y en a, un arbre vide sinon"""
        if self.countOfChildren() != 0:
            return self.children
        else:
            return [type(self)()]  # Renvoie une liste avec un arbre vide si pas d'enfants
        
    def getChildrenRacines(self):
        """ Renvoie la racine de chaue enfant """
        return [elt.racine() for elt in self.getChildren()]
    
    def getChild(self, index):
        """ Renvoie le fils à l'indice indiqué """
        if not self.getChildren().estVide():  # Si il a des enfants
            # Si il il y a un enfant à l'endroit indiqué
            if not (self.children[index].estVide()):
                return self.children[index]
            else:
                return None
            
    def getChildIndex(self, child):
        """ Renvoie l'indice de l'enfant donné """
        for i in range(len(children := self.getChildren())):
            if children[i] == child:
                return i

    def setChild(self, value, index = -1):
        """ Ne renvoie rien, change la valeur d'un enfant de l'arbre à l'indiex indiqué"""
        assert type(value) == type(self), 'Vous devez mettre un arbre comme valeur'        
        self.children[index] = value

    def addChild(self, value):
        """ Ajoute un enfant à l'arbre """
        assert type(value) == type(self), 'Vous devez mettre un arbre comme valeur'
        self.children.append(value)

    def delChild(self, delete):
        """ Supprime un enfant de l'arbre passé en args"""
        assert self.nodeInTree(delete), "Pour supprimer un enfant, il doit être dans l'arbre"
        index = 0
        for elt in self.getChildren():
            if elt == delete:
                self.children.pop(index)
            index += 1

    def delChildIndex(self, index):
        try:
            self.children[index] == type(self)()
        except:
            pass
    def setRacine(self, value):
        """ Change la valeur de la racine, Ne renvoie rien"""
        self.root = value

    def getEtage(self, n: int) -> list:
        """ Renvoie une liste des enfants de l'arbre à l'étage donné """
        if n == 0:
            return [self]
        else:
            list = []
            for i in range(len(self.getChildren())):
                if not self.getChildren()[i].estVide():
                    list += self.getChildren()[i].getEtage(n - 1)
            return list
    
    def nodeInTree(self, node):
        """ Renvoie True si `node` est dans l'arbre False sinon
            node -> objet arbre ; composé du noeud de l'arbre et ses enfants
        """
        assert type(node) is type(self) or type(node) is not None, "L'objet en args doit être un arbre"
        if self.estVide():
            return False
        if (self.racine() == node.racine()) and (node.getChildrenRacines() == self.getChildrenRacines()):
            return True
        else:
            return (True in [elt.nodeInTree(node) for elt in self.children])
        
    def parent(self, node):
        """ Renvoie le parent du noeud en args"""
        if self.estVide():
            return False
        if not self.nodeInTree(node):
            return False
        if node in self.getChildren():
            return self
        else:
            for enfant in [elt.parent(node) for elt in self.getChildren()]:
                if enfant is not False:
                    return enfant                   
    # Mesures

    def hauteur(self):
        """ Renvoie la hauteur de l'arbre """
        if self.estVide():
            return -1
        if self.estFeuille():
            return 0
        else:
            ListHauteurs = [elt.hauteur() for elt in self.children]
            return max(ListHauteurs) + 1

    def taille(self):
        """ Renvoie la taille de l'arbre"""
        if self.estVide():
            return 0
        else:
            listeTailles = [elt.taille() for elt in self.getChildren()]
            return 1 + sum(listeTailles)

    def arite(self):
        """ Renvoie l'arité de l'arbre (nbre d'enfants max)"""
        if self.estFeuille():
            return 0
        else:
            # arite de chaque noeuds -> noeud.arite() ;  arite du noeud actuel  -> len(l)
            listArite = [elt.arite() for elt in self.getChildren()]
            return max(max(listArite), len(listArite))
    
    # Parcours
    def DFS(self):
        """ Renvoie une liste du parcours en profondeur de l'arbre : `Depth First Search` """
        listeFinale = []  # Contiendra les valeurs qui montreront la manière dont le parcours est effectué
        pile = []
        pile.append(self)
        while len(pile) != 0:
            temp = pile.pop()
            listeFinale.append(temp)
            for enfant in temp.getChildren():
                if not enfant.estVide():
                    pile.append(enfant)
        return listeFinale

    def BFS(self):
        """ Renvoie une liste du parcours en largeur de l'arbre : `Breadth First Search` """
        listeFinale = []
        fileFIFO = []
        fileFIFO.insert(0, self)
        while len(fileFIFO) != 0:
            temp = fileFIFO.pop()
            listeFinale.append(temp)
            for enfant in temp.getChildren():
                if not enfant.estVide():
                    fileFIFO.insert(0, enfant)
        return listeFinale
tree = Tree(1,
                      Tree(2),
                      Tree(3),
                      Tree(4,
                            Tree(5)),
                      Tree(6,
                            Tree(7),
                            Tree(8)),
                      Tree(9, 
                            Tree(10, 
                                Tree(11))))

