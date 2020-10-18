import random
import time

    if __name__ == '__main__':
        display_intro()

    def display_intro():
        print("Tu es dans un pays rempli de dragons. Devant toi, tu vois deux grottes. Dans l'une, le dragon Thomas est amical et partagera son trésor avec toi. Dans l'autre, le dragon Yamina est affamé et te dévorera s'il te voit")
        # print()

    def choose_cave():
        cave = ""
        while cave != "1" and cave != "2":
            print("Dans quelle grotte vas-tu entrer (1 ou 2) ? ")
            cave = input()
        return cave

    def check_cave(chosen_cave):
        print("Tu t'approches de la grotte ...")
        time.sleep(2)
        print("Tout est sombre et effrayant ...")
        time.sleep(2)
        print("Un énorme dragon saute juste devant toi ! "
        + " Il ouvre grand ses machoires et ...")
        print()
        time.sleep(2)

        friendly_cave = random.randint(1,2)

        if chosen_cave == str(friendly_cave):
            print("Te donne son trésor !")
        else:
            print("T'avale d'un seul coup !")
        print()

        play_again = "oui"

        while play_again == "oui" or play_again == "o":
            display_intro()
            cave_number = choose_cave()
            check_cave(cave_number)

            print("Veux-tu rejouer (oui ou non) ?")
            play_again = input()
