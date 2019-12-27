import random


class Monster(object):
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence


def battle(self):
    for x in range (1):
        print(f'intiial health is {self.health}')
        AP = (random.randint(1, self.attack))
        DP = (random.randint(1, self.defence))
        print(f'Attack Power is {AP} and Defence Power {DP}')
        total_dmg = AP - DP
        print(f'Total damage inflicted is {abs(total_dmg)}')
        self.health -= total_dmg
        print(self.health)


battle(Monster("medusa", 30, 14, 16))
