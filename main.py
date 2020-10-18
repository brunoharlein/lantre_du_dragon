import random
import time


def displayIntro():
    print('''Tu es dans un pays rempli de dragons. Devant toi, tu vois deux grottes
Dans l'une d'elle, le dragon Thomas est amical et partagera son trésor avec toi.
Dans l'autre grotte, le dragon Yamina est affamé et te dévorera s'il te voit''')
    print()


def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print('Dans quelle grotte vas-tu entrer ? (1 or 2)')
        cave = input()

    return cave


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
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Veux-tu rejouer (oui ou non) ?")
    playAgain = input()
