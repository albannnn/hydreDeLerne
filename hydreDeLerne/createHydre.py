from Hydre import Hydre
def createHydre(difficulte):
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
                      Hydre(3),
                      Hydre(4,
                            Hydre(5)),
                      Hydre(9, 
                            Hydre(10, 
                              Hydre(11))),
                     Hydre(6,
                            Hydre(7),
                            Hydre(8)),
                     Hydre(2))
        hydre.rename()
        return hydre
    
hydre = createHydre('difficile')
print(hydre.hauteur())
print(hydre)
