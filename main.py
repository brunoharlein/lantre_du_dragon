import random  # import random module
import time  # import time module

#   Les fonctions permettent de répéter l'exécution d'un même code sans devoir copier-coller ce code plusieurs fois.
#   Il suffit de placer les instructions dans une fonction et d'appeler cette dernière dès que nécessaire.
#   Ainsi, s'il y a une erreur dans le code, il n'y a qu'un endroit ou corriger

def displayIntro():
    #   '''you can write on multiple lines'''
    print('''Tu es dans un pays rempli de dragons. Devant toi, tu vois deux grottes
Dans l'une d'elle, le dragon Thomas est amical et partagera son trésor avec toi.
Dans l'autre grotte, le dragon Yamina est affamé et te dévorera s'il te voit''')
    print()     # to skip a line ;-)


def chooseCave():
    # Contrairement à la boucle FOR dont le nombre de répétitions est précisé, une boucle WHILE se répète
    # TANT QU'UNE condition définie est VRAIE (TRUE)
    cave = ""   # variable that expects a value (1 or 2)
    # As long as the user does not type 1 or 2, the computer will ask the question again.
    while cave != "1" and cave != "2":
        print("Dans quelle grotte vas-tu entrer ? (1 or 2)")
        cave = input()  # Un input renvoi toujour une STR

    return cave     # return 1 or 2


def checkCave(chosenCave):
    print("Tu t'approches de la grotte")
    time.sleep(2)
    print("Tout est sombre et effrayant")
    time.sleep(2)
    print("Un énorme dragon saute juste devant toi ! Il ouvre grand ses machoires et ...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Te donne son trésor !")
    else:
        print("T'avale d'un seul coup !")


playAgain = "oui"
while playAgain == "oui" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()   # 1 or 2 (the result of chooseCave)
    checkCave(caveNumber)

    print("Veux-tu rejouer (oui ou non) ?")
    playAgain = input()
