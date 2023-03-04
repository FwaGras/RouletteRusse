from random import randint

def revolver()->list:
    """
    Renvoie une liste constitué de cinq 0 et d'un 1 qui est placé dans
    une position aléatoire
    """
    barillet_vide = [0, 0, 0, 0, 0, 0]
    barillet_chargé = []
    
    for _ in range(1):
        barillet_vide.remove(barillet_vide[randint(0, 5)])
        barillet_vide.insert(randint(0, 5), 1)
        barillet_chargé = barillet_vide
        
    return barillet_chargé
    
def tirer(barillet:list)->bool:
    """
    Prend la liste barillet en paramètre.
    Renvoie True si c'est 1 qui se trouve dans le 5ème indice de
    barillet et rapelle la fonction Revolver pour tirer au hasard la nouvelle position de la balle.
    Sinon, renvoie False si c'est 0 et décale les éléments de la liste à gauche.
    """
    return barillet[5] ==  1

def tirer_et_shuffle(barillet):
    fin = False
    while fin == False :
        v = input("Mélange ?")
        if v == "Oui" :
            barillet = revolver()
        if tirer(barillet) == True :
            print("Mort")
            fin == True
            barillet = revolver()
        else :
            barillet = décale_droite(barillet)
            print("C'est ton jour de chance, petit veinard.")

def décale_droite(barillet:list)->list:
    for i in range(5, 0, -1):
        barillet[i] = barillet[i - 1]
    barillet[0] = 0
    return barillet


barillet = revolver()
print(barillet)
tirer(barillet)
tirer_et_shuffle(barillet)
décale_droite(barillet)
