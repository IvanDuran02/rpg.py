import random

def say(name,dialouge):
    return print(f'{name}{dialouge}')
#list of characters below
garen = 'Garen: '
#
say(garen,'hi')

class Monsters:
    def __init__(self,name,hp,dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
#Slime
slime = Monsters('Slime', 15, random.randint(1,3))
slimeStatus = f'{slime.name} - {slime.hp}HP'
#Wolf
wolf = Monsters("Wolf", 25, random.randint(3,5))
wolfStatus = f"{wolf.name} - {wolf.hp}HP"
