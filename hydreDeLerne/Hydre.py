from Tree import Tree #import de la classe Tree
import random
import pygame

class Hydre(Tree):
    """
    Hercule à du affronter lors du deuxieme de ses douzes travaux l'Hydre de Lerne. 
    Cette hydre, à vous de l'affronter aujourd'hui !
    Pour la tuer il ne doit rester aucune tête, en êtes vous capables?
    Vous disposez de plusieurs méthodes pour tuer l'hydre:
        - Couper une tête : couper(tete)
        - Etat de l'hydre : etat 
        - Pour visualiser l'hydre : print()
        
    """
    
    def __init__(self, racine = None,  *children):
        Tree.__init__(self, racine, *children)
        self.etat = "alive"
        self.nombreTetes = self.getFeuilles()
        self.role = 0
        self.nombreCoups = 0
        self.surface = None
        self.allocateSpace = None
        self.coordOnScreen = None

    def __repr__(self):
        return f"<Hydre object root = {self.racine()}>"
    def getSurf(self):
        """ Renvoie l'attribut surface de l'Hydre """
        return self.surface
    
    def setSurf(self, surface:pygame.Surface):
        """ Change l'attribut surface de l'hydre
            Entrée : objet pygame.Surface
            --> void
        """
        assert type(surface) == pygame.Surface; 'Vous devez entrer un objet pygame Surface'
        self.surface = surface
    def area(self):
        """ renvoie l'espace occupé par le noeud de l'hydre sur l'ecran sous forme de :  coordX -> (x1, x2), coordy -> (y1, y2)"""
        return((self.coordOnScreen[0], self.coordOnScreen[0] + self.allocateSpace[0]), (self.coordOnScreen[1], self.coordOnScreen[1] + self.allocateSpace[1]))
    def getAllocateSpace(self) -> tuple:
        """ renvoie l'allocate space de l'hydre """
        return self.allocateSpace
    
    def setAllocateSpace(self):
        """ Change automatiquement des enfants l'allocatespace de l'hydre """
        if self.estFeuille():
            return None
        else:
            for enfant in self.getChildren():
                enfant.allocateSpace = (self.getAllocateSpace()[0] // len(self.getChildren()), self.getAllocateSpace()[1])
                enfant.setAllocateSpace()
        
    def changeEtat(self):
        """  Change l'etat de l'hydre -> si il lui reste des têtes : 'alive' sinon : 'dead' """ 
        if False in [elt.estVide() for elt in self.getChildren()] or self.nombreTetes > 1:
            self.etat = 'alive'
        else:
            self.etat = 'dead'

    def testVictoire(self):
        """ Renvoie True si l'hydre n'a plus de têtes (si elle morte ...) """
        return self.etat == "dead"
    
    def victoire(self):
        """ Renvoie un message de victoire """
        return f" Bravo vous avez battu l'Hydre en {self.nombreCoups} coups !!"
    
    def defaite(self):
        """ Renvoie un message de défaite """
        return "Vous avez perdu, retentez une prochaine fois !"
            
    def couper(self, tete):
        """ Action de couper une tête de l'Hydre (void) """
        if not self.nodeInTree(tete):
            listeCorps = ["à la tête",
                          "au pied",
                          "à la cheville",
                          "au talon, Vous avez de la chance que je ne sois pas Achille",
                          "à la jambe",
                          "au bras",
                          "au torse"]
            
            endroit = random.choice(listeCorps)
            print(f"Vous devez couper un membre de l'Hydre, vous venez de me faire mal {endroit} !!")
            return None
        

        #si le joueur est hercule il n'a pas besoin de faire d'effort et gagne directement
        if self.estHercule(): # Si le role du joueur est hercule
            return None
        

        if not tete.estFeuille():
            print("Vous devez couper une tête !!!")
            return None
        

        # Si la tete est la racine de l'arbre -> on ne peut pas la couper
        if tete.racine() == self.racine():
            print("Vous ne pouvez pas couper le corps de l'hydre")
            return None
        

        # Si la tete est rattaché au corps, alors elle est coupée définitivement
        if self.parent(tete).racine() == self.racine():
            self.parent(tete).delChild(tete)
            self.nombreCoups += 1


        ## Si la tete n'est pas directement relié au corps il en repousse plusieurs
        else:

            #COUPE 
            tempHydre = self.parent(tete)
            tempHydre.delChild(tete) 
            self.nombreCoups += 1
            #REPOUSSE
            tempHydre = self.parent(tempHydre)
            for i in range(self.nombreCoups):
                tempHydre.addChild(Hydre('nouveau'))
        self.nombreTetes = self.getFeuilles()    
        self.rename()
        
    def rename(self):
        """ Renommage de l'hydre """
        index = 1
        indexCou = 0
        pile = []
        pile.append(self)
        while len(pile) != 0:
            if pile[-1].estFeuille(): #si c'est une feuille on renomme avec le numéro de tête
                pile[-1].setRacine(f"Tête {index}") 
                index += 1
            else:
                pile[-1].setRacine(f"cou {indexCou}") #si c'est autre chose qu'une feuille, c'est un cou ou la racine -> on etudiera le dernier cas + tard
                indexCou += 1
            for enfant in pile.pop().getChildren(): #parcours dfs
                if not enfant.estVide():
                    pile.append(enfant)
        self.setRacine("corps") #on gére le cas de la racine, cette derniere prendra la valeur 'cou' or c'est le corps de l'hydre
    
    def estHercule(self):
        return self.role == 1
    
    def devenirHercule(self):
        self.role = 1
        self.etat = "dead"
        self.nombreTetes = 0
        print("Vous avez reçu un arc et une massue.")
        return None
    

hydre = Hydre(1,
              Hydre(2, Hydre(3), Hydre(4), Hydre(5), Hydre(6), Hydre(7)),
              Hydre(8, Hydre(9), Hydre(10)),
              Hydre(11, Hydre(12, Hydre(13), Hydre(14, Hydre(15))), Hydre(16)),
              Hydre(17))


