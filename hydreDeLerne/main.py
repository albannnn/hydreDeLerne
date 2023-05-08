from Hydre import Hydre
from Tree import Tree
import random
""" 
    Programme pour jouer au jeu dans la console
"""
def beforeStart(difficulte):
    """ Renvoie une hydre de la difficulté donnée """
    if difficulte == "facile":
        hydre = Hydre(1, 
                      Hydre(2), 
                      Hydre(3), 
                      Hydre(4), 
                      Hydre(5, 
                            Hydre(6)))
        hydre.rename()
        return hydre
    if difficulte == "moyen":
        hydre = Hydre(1, 
                      Hydre(2), 
                      Hydre(3), 
                      Hydre(4, 
                            Hydre(5)), 
                      Hydre(6, 
                            Hydre(7),
                            Hydre(8)))
        hydre.rename()
        return hydre
    if difficulte == 'difficile':
        hydre = Hydre(1,
                      Hydre(2),
                      Hydre(3),
                      Hydre(4,
                            Hydre(5)),
                      Hydre(6,
                            Hydre(7),
                            Hydre(8)),
                      Hydre(9, 
                            Hydre(10, 
                                Hydre(11))))
        hydre.rename()
        return hydre
    else:
        return beforeStart(input("Choisissez la difficulté entre facile/moyen/difficile : "))
  
def main(hydre):
    print("Bienvenue dans le jeu. Vous devez battre l'Hydre de Lerne.\n Pour ce faire, vous pouvez couper une de ses têtes à chaque tour. Mais attention, plus vous couper de têtes, plus nombreuses elles repoussent ! \n Bonne chance !! ")
    running = hydre.etat == 'alive'
    while running:
        print(hydre)
        
        toCut = input("Quelle tête voulez vous couper ? (Vous pouvez aussi abandonner en écrivant 'abandonner'):")
        if toCut == 'Devenir Hercule':
            hydre.devenirHercule()
            
            

        elif toCut == 'abandonner':
            running = False
            break
        else:
            hydre.couper(Hydre(toCut))
            hydre.changeEtat()
            hydre.testVictoire()
            running = hydre.etat == 'alive'

def afterGame(hydre):
    if hydre.etat != 'dead':
        print(hydre.defaite())
    else:
        print(hydre.victoire())


hydre = beforeStart(input("Choisissez la difficulté entre facile/moyen/difficile : "))
print("Voici l'Hydre que vous devez vaincre", '\n' , hydre)
main(hydre)
afterGame(hydre)

