# Name: Cayub
# Date: 1/31/19

import sys
import time
import random
from typing import *


# Player setup
class Player:
    def __init__(self):
        self.name = ""
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.strength = 0
        self.defense = 0
        self.fireball = 0
        self.iceshard = 0
        self.heal = 0
        self.holysmite = 0
        self.status_effects = []
        self.location = "a1"
        self.inventory = {}
        self.store_inventory = {"Steel Sword": 20, "Electrum Wand": 20, "Tower Shield": 10, "Mana Drank": 5,
                                "Health Drank": 10}
        self.gold = 20
        self.game_over = False

    def attack(self, myEnemy):
        if myPlayer.job.lower() == "warrior":
            actual_battle_warrior(myEnemy)

        elif myPlayer.job == "mage":
            actual_battle_mage(myEnemy)


myPlayer = Player()


class Enemy:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.strength = 0
        self.defense = 0
        self.lightning = 0
        self.magicmissle = 0

    def attack(self, myPlayer):
        attack = random.randint(0, myEnemy.strength)
        defense = random.randint(0, myPlayer.defense)
        actual_attack = int(attack - defense)
        if actual_attack <= 0:
            print("the enemy stumbled...")
        else:
            myPlayer.hp -= actual_attack
            if myPlayer.hp > 0:
                print("The " + myEnemy.name + " damaged you for " + str(actual_attack) + "! You have " + str(myPlayer.hp) + " left.")
            else:
                print("##############################")
                print("###### You have deaded #######")
                print("##############################")
                print(myEnemy.name + " has killed you.")
                game_over()


myEnemy = Enemy()


# Title screen
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]:
        title_screen()


def title_screen():
    print("###########################")
    print("# Welcome to the Text Rpg #")
    print("###########################")
    print("          -Play-           ")
    print("          -Help-           ")
    print("          -Quit-           ")
    print("###########################")
    title_screen_selections()


def help_menu():
    print("###########################")
    print("# Welcome to the Text Rpg #")
    print("###########################")
    print("Use up, down, left, right to move")
    print("Type commands to do them ")
    print(" Use look to inspect something")
    print("###########################")
    title_screen_selections()


# Map
ZONE_NAME = ""
DESCRIPTION = "description"
EXAMINATION = "examine"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"

solved_places = {"a1": False, "a2": False, "a3": False, "a4": False,
                 "b1": False, "b2": False, "b3": False, "b4": False,
                 "c1": False, "c2": False, "c3": False, "c4": False,
                 "d1": False, "d2": False, "d3": False, "d4": False
                 }

zone_map = {
    "a1": {ZONE_NAME: "Your Humble Abode",
           DESCRIPTION: "This is where you live",
           EXAMINATION: "Everything is where you left it",
           SOLVED: False,
           UP: "",
           DOWN: "b1",
           LEFT: "",
           RIGHT: "a2",
           },
    "a2": {ZONE_NAME: "Northern Cross Roads",
           DESCRIPTION: "A Sign reads\n ~West~\n Town Merogifly\n ~South~",
           EXAMINATION: "examine",
           SOLVED: False,
           UP: "",
           DOWN: "b2",
           LEFT: "a1",
           RIGHT: "a3",
           },
    "a3": {ZONE_NAME: "The Town of Merogifly",
           DESCRIPTION: "The town has a market containing a blacksmith ",
           EXAMINATION: "prompt the user with dialogue from the blacksmith to buy some weapons** fix later",
           SOLVED: False,
           UP: "",
           DOWN: "",
           LEFT: "a2",
           RIGHT: "a4",
           },
    "a4": {ZONE_NAME: "Castle of the Family of Vagrants",
           DESCRIPTION: "The castle is on top of a miniature mountain with jagged edges. Attacking the castle would be"
                        "suicide due to the single entry point facing the town.",
           EXAMINATION: "upon entry paladin dan says you arent supposed to be here and attacks you** fix later",
           SOLVED: False,
           UP: "",
           DOWN: "",
           LEFT: "a3",
           RIGHT: "",
           },
    "b1": {ZONE_NAME: "Dead End",
           DESCRIPTION: "The hallway ends rather abruptly. As if the people designing the dungeon"
                        "had major limitations",
           EXAMINATION: "put map in this zone** fix later",
           SOLVED: False,
           UP: "",
           DOWN: "",
           LEFT: "",
           RIGHT: "b2",
           },
    "b2": {ZONE_NAME: "Hallway",
           DESCRIPTION: "There is an opening to left and a wall to the right."
                        "The hallway seems to continue forward as well. ",
           EXAMINATION: "Enemy spawn here.",
           SOLVED: False,
           UP: "a2",
           DOWN: "c2",
           LEFT: "b1",
           RIGHT: "",
           },
    "b3": {ZONE_NAME: "Torture Chamber",
           DESCRIPTION: "The Chamber is full of cages hanging from the ceiling,"
                        "and skeletons cuffed to the walls. There appears to be a door to the right.",
           EXAMINATION: "advanced monster spawn",
           SOLVED: False,
           UP: "",
           DOWN: "c3",
           LEFT: "",
           RIGHT: "b4",
           },
    "b4": {ZONE_NAME: "Portal room",
           DESCRIPTION: "A large circular room. To the south in the center there is a portal.",
           EXAMINATION: "advanced monster spawn",
           SOLVED: False,
           UP: "",
           DOWN: "c4",
           LEFT: "b3",
           RIGHT: "",
           },
    "c1": {ZONE_NAME: "Treasure room",
           DESCRIPTION: "The room seems to have nothing more than a single chest"
                        "at the end of the room.",
           EXAMINATION: "class based weapon",
           SOLVED: False,
           UP: "",
           DOWN: "d1",
           LEFT: "",
           RIGHT: "",
           },
    "c2": {ZONE_NAME: "Hallway Intersection",
           DESCRIPTION: "The hallway breaks off to the right as well as continuing forward.",
           EXAMINATION: "Basic enemy spawn",
           SOLVED: False,
           UP: "b2",
           DOWN: "d2",
           LEFT: "",
           RIGHT: "c3",
           },
    "c3": {ZONE_NAME: "Torture room entrance",
           DESCRIPTION: "The room is littered with bones and bloodied walls. ",
           EXAMINATION: "Basic enemy spawn",
           SOLVED: False,
           UP: "b3",
           DOWN: "",
           LEFT: "c2",
           RIGHT: "",
           },
    "c4": {ZONE_NAME: "Entry way to Lair",
           DESCRIPTION: "The room is a square shaped room exiting to south"
                        "to a large circular chamber",
           EXAMINATION: "advanced enemy spawn",
           SOLVED: False,
           UP: "b4",
           DOWN: "d4",
           LEFT: "",
           RIGHT: "",
           },
    "d1": {ZONE_NAME: "Corner room",
           DESCRIPTION: "The room has two doors, one to the right, and one to the north.",
           EXAMINATION: "basic enemy spawn",
           SOLVED: False,
           UP: "c1",
           DOWN: "",
           LEFT: "",
           RIGHT: "d2",
           },
    "d2": {ZONE_NAME: "Hallway end",
           DESCRIPTION: "The hallway ends directly south. To the left and right there "
                        "are door ways. ",
           EXAMINATION: "basic enemy spawn",
           SOLVED: False,
           UP: "c2",
           DOWN: "",
           LEFT: "d1",
           RIGHT: "d3",
           },
    "d3": {ZONE_NAME: "Treasure room",
           DESCRIPTION: "The room is closet sized with a simple chest laying on the"
                        "floor half opened.",
           EXAMINATION: "Class armor",
           SOLVED: False,
           UP: "",
           DOWN: "",
           LEFT: "d2",
           RIGHT: "",
           },
    "d4": {ZONE_NAME: "Boss Lair",
           DESCRIPTION: "The room is a circular stone room. The floor is cold to the "
                        "touch.",
           EXAMINATION: "Final boss spawn",
           SOLVED: False,
           UP: "c4",
           DOWN: "",
           LEFT: "",
           RIGHT: "",
           }

}

# Game Interactivity


def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zone_map[myPlayer.location][ZONE_NAME] + ' #')
    print('# ' + zone_map[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))


def prompt():
    print('\n' + "===================")
    print("What would you like to do?")
    action = input("> ")
    acceptable_actions = ("move", "go", "travel", "walk", "quit", "examine", "inspect", "interact", "look",)
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again.\n")
        action = input("> ")
    if action.lower() == "quit":
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action.lower())
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine(action.lower())
    elif action.lower() in ["help"]:
        help_menu()


def player_move(myAction):
    ask = "Where would you like to go?\n> "
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zone_map[myPlayer.location][UP]
        if destination == "":
            print("You have ran into a wall. Please try doing something else.")
            prompt()
        else:
            movement_handler(destination)
    elif dest in ["left", "west"]:
        destination = zone_map[myPlayer.location][LEFT]
        if destination == "":
            print("You have ran into a wall. Please try doing something else.")
            prompt()
        else:
            movement_handler(destination)
    elif dest in ["right", "east"]:
        destination = zone_map[myPlayer.location][RIGHT]
        if destination == "":
            print("You have ran into a wall. Please try doing something else.")
            prompt()
        else:
            movement_handler(destination)
    elif dest in ["down", "south"]:
        destination = zone_map[myPlayer.location][DOWN]
        if destination == "":
            print("You have ran into a wall. Please try doing something else.")
            prompt()
        else:
            movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zone_map[myPlayer.location][SOLVED]:
        print("You have already exhausted the zone")
        return
    elif myPlayer.location == "a3":
        store()
    elif myPlayer.location not in ["b2", "c2", "c3", "d1", "d2", "b3", "b4", "c4", "d4"]:
        print("There is nothing out of the ordinary here")
    else:
        battle_loop()


# Game Functionality
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
        # handle if puzzles have been solved, boss defeated, explored everything, etc...


def setup_game():
    question1 = "Hello, what's your name? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    question2 = "Hello, " + player_name + " what's your Job? ~Warrior~ ~Mage~ \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("> ")
    valid_jobs = ["warrior", "mage"]
    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print("You are now a " + player_job + "!\n")
    while player_job.lower() not in valid_jobs:
        player_job = input("> ")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("You are now a " + player_job + "!\n")
    # player stats
    if myPlayer.job == "warrior":
        myPlayer.hp = 80
        myPlayer.mp = 20
        myPlayer.strength = 30
        myPlayer.defense = 10
    elif myPlayer.job == "mage":
        myPlayer.hp = 40
        myPlayer.mp = 120
        myPlayer.strength = 10
        myPlayer.defense = 3
        myPlayer.fireball = 50
        myPlayer.iceshard = 60

    # Introduction
    question3 = "Welcome, " + player_name + " the " + player_job + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    speech1 = "Welcome to the game made by professionals!\n"
    speech2 = "If you ever want to quit simply type -quit-\n"
    speech3 = "This is the map. You begin in your home in a1.\n"
    speech4 = """
    [a1],[a2],[a3],[a4]
    [b1],[b2],[b3],[b4]
    [c1],[c2],[c3],[c4]
    [d1],[d2],[d3],[d4]
            """
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)

    print("####################")
    print("    Let us begin    ")
    print("####################")
    main_game_loop()


def basic_enemies():
    enemies = ["Snake", "Wolf", "Skeleton", "Giant Rat", "Possessed Sword"]
    enemyChosen = random.choice(enemies)
    if enemyChosen == "Snake":
        myEnemy.name = "Snake"
        myEnemy.hp = 20
        myEnemy.mp = 0
        myEnemy.strength = 5
        myEnemy.defense = 0
    elif enemyChosen == "Wolf":
        myEnemy.name = "Wolf"
        myEnemy.hp = 25
        myEnemy.mp = 0
        myEnemy.strength = 5
        myEnemy.defense = 5
    elif enemyChosen == "Skeleton":
        myEnemy.name = "Skeleton"
        myEnemy.hp = 30
        myEnemy.mp = 0
        myEnemy.strength = 10
        myEnemy.defense = 5
    elif enemyChosen == "Giant Rat":
        myEnemy.name = "Giant Rat"
        myEnemy.hp = 45
        myEnemy.mp = 0
        myEnemy.strength = 10
        myEnemy.defense = 10
    elif enemyChosen == "Possessed Sword":
        myEnemy.name = "Possessed Sword"
        myEnemy.hp = 25
        myEnemy.mp = 0
        myEnemy.strength = 25
        myEnemy.defense = 0


def advanced_enemies():
    enemies = ["Paladin Dan"]
    enemyChosen = random.choice(enemies)
    if enemyChosen == "Paladin Dan":
        myEnemy.name = "Paladin Dan"
        myEnemy.hp = 400
        myEnemy.mp = 400
        myEnemy.strength = 400
        myEnemy.defense = 400
        myEnemy.lightning = 400
        myEnemy.magicmissle = 400


def boss_enemy():
    enemies = ["Lord of Containment"]
    enemyChosen = random.choice(enemies)
    if enemyChosen == "Lord of Containment":
        myEnemy.name = "Lord of Containment"
        myEnemy.hp = 400
        myEnemy.mp = 400
        myEnemy.strength = 400
        myEnemy.defense = 400
        myEnemy.lightning = 400
        myEnemy.magicmissle = 400


def battle_loop():
    if myPlayer.location in ["b2", "c2", "c3", "d1", "d2"]:
        basic_enemies()
        print('A ' + str(myEnemy.name) + ' has appeared')
    elif myPlayer.location in ["a4", "b3", "b4", "c4"]:
        advanced_enemies()
        print('A ' + str(myEnemy.name) + ' has appeared')
    elif myPlayer.location in ["d4"]:
        boss_enemy()
        print('The final boss ' + str(myEnemy.name) + ' has appeared')
    while myEnemy.hp != 0:
        if myEnemy.hp > 0:
            print("The enemy moves in for it's attack.")
            myEnemy.attack(myPlayer)
            myPlayer.attack(myEnemy)
        elif myPlayer.location in ["d4"] and myEnemy.hp <= 0:
            print("Congratulations!!!!\n You have beaten this very long and immersive game!!!")
            game_over()
        else:
            myEnemy.name = ""
            myEnemy.hp = 0
            myEnemy.mp = 0
            myEnemy.strength = 0
            myEnemy.defense = 0
            zone_map[myPlayer.location][SOLVED] = True
            gold_prize = random.randint(0, 5)
            print('You earned ' + str(gold_prize) + ' Gold.')
            print("You now have " + str(myPlayer.gold) + ".")
            return
    while myEnemy.hp <= 0:
        if myEnemy.name not in [""]:
            myEnemy.name = ""
            myEnemy.hp = 0
            myEnemy.mp = 0
            myEnemy.strength = 0
            myEnemy.defense = 0
            zone_map[myPlayer.location][SOLVED] = True
            gold_prize = random.randint(0, 5)
            print('You earned ' + str(gold_prize) + ' Gold.')
            return


def actual_battle_mage(myEnemy):
    answer = input("What would you like to do? [Attack, Magic, Run away]\n> ")

    if answer.lower() == "attack":
        attack = random.randint(0, myPlayer.strength)
        defense = random.randint(0, myEnemy.defense)
        actual_attack = int(attack - defense)
        if actual_attack <= 0:
            print("you stumbled...")
        else:
            myEnemy.hp = myEnemy.hp - actual_attack
            if myEnemy.hp < 0:
                print("You hit " + myEnemy.name + " for " + str(actual_attack))
                print('The enemy has been slayed')
            else:
                print("You hit " + myEnemy.name + " for " + str(actual_attack) + "! " + myEnemy.name +
                      " now has " + str(myEnemy.hp) + " health left.")

    elif answer.lower() == "magic":
        if myPlayer.mp <= 0:
            print("You do not have enough magic points")
            actual_battle_mage(myEnemy)
        else:
            spell = input("What spell would you like to cast? [Fireball, Ice Shard]\n> ")
            if spell.lower() == "fireball":
                print(str(myPlayer.mp))
                spell_attack = random.randint(0, myPlayer.fireball)
                myPlayer.mp -= 20
                defense = random.randint(0, myEnemy.defense)
                actual_spell_attack = int(spell_attack - defense)
                print(str(myPlayer.mp))
                if actual_spell_attack <= 0:
                    print("Your fireball sailed past the enemy.")
                else:
                    time.sleep(0.05)
                    myEnemy.hp -= actual_spell_attack
                    if myEnemy.hp < 0:
                        print("You hit " + myEnemy.name + " for " + str(actual_spell_attack))
                        print('The enemy has been slayed')
                    else:
                        print("You hit " + myEnemy.name + " for " + str(actual_spell_attack) + "! " + myEnemy.name +
                              " now has " + str(myEnemy.hp) + " health left.")
                        print(str(myPlayer.mp))

            elif spell.lower() == "ice shard":
                spell_attack = random.randint(0, myPlayer.fireball)
                myPlayer.mp -= 30
                defense = random.randint(0, myEnemy.defense)
                actual_spell_attack = int(spell_attack - defense)
                if actual_spell_attack == 0:
                    print("Your ice shard missed")
                else:
                    myEnemy.hp -= actual_spell_attack
                    print("You hit " + myEnemy.name + " for " + str(actual_spell_attack) + "! " +
                          myEnemy.name + " now has " + str(myEnemy.hp) + " health left.")
    elif answer.lower() == "run away":
        luck = random.randint(0, 1)
        if luck == 1:
            print("You have run away.")
            prompt()
        else:
            print("You failed to run away.")


def actual_battle_warrior(myEnemy):
    answer = input("What would you like to do? [Attack, Run away]\n> ")
    if answer.lower() == "attack":
        attack = random.randint(0, myPlayer.strength)
        defense = random.randint(0, myEnemy.defense)
        actual_attack = int(attack - defense)
        if actual_attack <= 0:
            print("you stumbled...")
        else:
            time.sleep(0.05)
            myEnemy.hp = myEnemy.hp - actual_attack
            if myEnemy.hp < 0:
                print("You hit " + myEnemy.name + " for " + str(actual_attack))
                print('The enemy has been slayed')
            else:
                print("You hit " + myEnemy.name + " for " + str(actual_attack) + "! " + myEnemy.name +
                      " now has " + str(myEnemy.hp) + " health left.")
    elif answer.lower() == "run away":
        luck = random.randint(0, 1)
        if luck == 1:
            print("You have run away.")
            prompt()
        else:
            print("You failed to run away.")


def store():
    n = 0
    print("You have " + str(myPlayer.gold) + " gold.")
    print("Shop Keep ~ I have these items for sale. ~")
    for i in myPlayer.store_inventory:
        print(list((myPlayer.store_inventory.keys()))[n] + ": " + str(myPlayer.store_inventory[i]) + " gold.")
        n += 1
    y = input('Shop Keep ~ What do you want to buy? ~ \n> ')
    buy_store(y.lower())


def buy_store(y):
    if y in ["steel sword", "electrum wand", "tower shield", "mana drank", "health drank"]:
        if y in myPlayer.inventory:
            myPlayer.inventory[y] += 1
        else:
            myPlayer.inventory[y] = 1
        if y == "steel sword":
            myPlayer.strength += 10
            print("You have gained a steel sword. Your Strength is now " + str(myPlayer.strength) + ".")
        elif y == "tower shield":
            myPlayer.defense += 5
            print("You have gained a tower shield. Your Defense is now " + str(myPlayer.defense) + ".")
        elif y == "electrum wand":
            myPlayer.fireball += 10
            myPlayer.iceshard += 10
            print("You have gained an electrum wand. Your spell strength has increase by 10.")
        elif y == "health drank":
            myPlayer.hp += 20
            print("You have drank the health drank. Your HP is now " + str(myPlayer.hp) + ".")
        elif y == "mana drank":
            myPlayer.mp += 20
            print("You have drank the mana drank. Your MP is now " + str(myPlayer.mp) + ".")
    else:
        print("I don't have that item.")
    stay_store()


def stay_store():
    x = input('Would you like to continue shopping? (Yes/No)')
    if x.lower() == 'yes':
        store()
    if x.lower() == 'no':
        return


def game_over():  # code so that it will handle player death and beating the game and exhausting all zones.
    print("==== Game Over ====")
    a: str = str(input("What would you like to do?[Restart / Quit]\n> "))
    if a.lower() in ["restart", "quit"]:
        if a.lower() == "restart":
            title_screen()
        elif a.lower() == "quit":
            sys.exit()
    else:
        print("Please enter a valid command.")
        game_over()


title_screen()
