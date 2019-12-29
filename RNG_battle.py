import random
import math


class Monster(object):
    def __init__(medusa, name, health, attack, defence):
        medusa.name = name
        medusa.health = health
        medusa.attack = attack
        medusa.defence = defence


class Hero(object):
    def __init__(hero, name, health, attack, defence):
        hero.name = name
        hero.health = health
        hero.attack = attack
        hero.defence = defence


def medusa_turn(medusa, hero):
    x = input("Medusa's Turn press enter to continue...\n")
    def battlelogic():
        if total_dmg == 0:
            print("The defence is too high!"
                  "\n0 Damage was inflicted.")
        elif total_dmg > 0:
            print(f'Medusa inflicted {total_dmg} Damage.')
        else:
            print("error has occurred")

    for x in range(1):
        print(f'Perseus\'s health is {hero.health}')
        AP = (random.randint(1, medusa.attack))
        DP = (random.randint(1, hero.defence))
        print(f'Medusa\'s Attack Power is {AP} and Perseus\'s Defence Power is {DP}')
        total_dmg = max(0, (AP - math.ceil(DP / 2)))
        battlelogic()
        hero.health -= total_dmg
        print(f'{hero.name}\'s current health is {hero.health}')
    if hero.health > 0:
        hero_turn(hero, medusa)

    else:
        print("Perseus has fallen.")


def hero_turn(hero, medusa):
    x = input("press enter key to attack...\n")

    def battlelogic():
        if total_dmg == 0:
            print("The defence is too high!"
                  "\n0 Damage was inflicted.")
        elif total_dmg > 0:
            print(f'Perseus inflicted {total_dmg} Damage.')
        else:
            print("error has occurred")
    for x in range(1):
        print(f'Medusa\'s health is at {medusa.health}')
        AP = (random.randint(1, hero.attack))
        DP = (random.randint(1, medusa.defence))
        print(f'Perseus\'s Attack Power is {AP} and Medusa\'s Defence Power is {DP}')
        total_dmg = max(0,(AP - math.ceil(DP / 2)))
        battlelogic()
        medusa.health -= total_dmg
        print(f'{medusa.name}\'s current health is {medusa.health}')
    if medusa.health > 0:
        medusa_turn(medusa, hero)
    else:
        print("Medusa has fallen")

hero = Hero("Perseus", 50, 15, 10)
medusa = Monster("Medusa", 30, 25, 20)
hero_turn(hero,medusa)