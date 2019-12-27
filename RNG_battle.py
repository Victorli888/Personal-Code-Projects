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



def battlelogic():
        if total_dmg == 0:
            print("The defence is too high!"
                  "\n0 Damage was inflicted.")
        elif total_dmg > 0:
            print(f' {total_dmg} Damage inflicted.')
        else:
            print("error has occurred")
def medusa_turn():
    for x in range(1):
        print(f'intiial health is {medusa.health}')
        AP = (random.randint(1, medusa.attack))
        DP = (random.randint(1, medusa.defence))
        print(f'Attack Power is {AP} and Defence Power {DP}')
        total_dmg = max(0,(AP - math.ceil(DP / 2)))
        battlelogic()
        medusa.health -= total_dmg
        print(f'{medusa.name}\'s current health is {medusa.health}')
    if medusa.health > 0:
        hero_turn()
def hero_turn():
    Monster("Medusa", 30, 14, 16)
    Hero("Perseus", 50, 30, 10)
    for x in range(1):
       print(f'Your health is at {hero.health}')
        AP = (random.randint(1, medusa.attack))
        DP = (random.randint(1, medusa.defence))
        print(f'Attack Power is {AP} and Defence Power {DP}')
        total_dmg = max(0,(AP - math.ceil(DP / 2)))
        battlelogic()
        hero.health -= total_dmg
        print(f'{hero.name}\'s current health is {hero.health}')
    if medusa.health > 0:
        medusa_turn()
    hero_turn()
Monster("Medusa", 30, 14, 16)
Hero("Perseus", 50, 30, 10)

