import random, math

class Dice_rolls():
    def D8(self):
        dice6 = (random.randint(1, 8))
        return dice6
    def D12(self):
        dice12 = (random.randint(1,12))
        return dice12


class Dawn_Winters():

   def savage_mastery(self):
    damage_roll = Dice_rolls.D12("Roll")
    damage_modifier = 5
    damageA = damage_roll + damage_modifier
    damageG1 = Dice_rolls.D8("Roll")  # weapon allows player Roll 2 dice-8's for Burn damage
    damageG2 = Dice_rolls.D8("Roll")  # this is the 2nd dice-8 roll
    damageB = damageG1 + damageG2
    print(f"Attack roll: {damage_roll} + {damage_modifier} = {damageA}\nGlaive damage: {damageG1} + {damageG2} = {damageB}\nMastery: 10\nRage: 2")
    total = damageA + damageB + 10 + 2
    print(f"Total Damage: {total}")
    input("\n*** Press Enter for Next Damage Roll ***\n")
    Dawn_Winters.savage_mastery("roll")





Dawn_Winters.savage_mastery("roll")