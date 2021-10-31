import random
import time

def sleep():
    time.sleep(2)


Paladin = {
  'name': "Paladin",
  'health': 15,
  'strength': 8,
  'dexterity': 10,
  'swordsplay': 5,
  'agility': 3,
}

SwordMaster = {
  'name': 'SwordMaster',
  'health': 12,
  'strength': 6,
  'dexterity': 5,
  'swordsplay': 10,
  'agility': 8
}

Tank = {
  'name': 'Tank',
  'health': 18,
  'strength': 7,
  'dexterity': 11,
  'swordsplay': 3,
  'agility': 1
}

Berserker = {
  'name': 'Berserker',   
  'health': 13,
  'strength': 11,
  'dexterity': 5,
  'swordsplay': 6,
  'agility': 6
}


# level up system

def SpecificlvlUp(combatstyle, skill):
    combatstyle[skill] = combatstyle[skill] + 1 
    return print(f"{[skill]} has leveled up to: {combatstyle[skill]}!")

# combatstyle
# combatstyle = Paladin

def say(name,dialouge):
    return print(f'{name}{dialouge}')
#list of characters below
garen = 'Garen: '
#
#Command - say(garen,'hi')

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

# SpecificlvlUp(combatstyle, 'health')

username = input(f'{garen}Hello adventeror, Im Garen what can i call a young lad like you?\n')
userPrefix = username + ': '
sleep()
print(f'{userPrefix}???')
sleep()
print(f'{garen}*cough* sorry... i was just trying to lighten the mood... you know what never mind -_-')
sleep()
print(f'{garen}[Thats right... the mood here is a bit gloomy, currently you stand in a empty battlefield, you came here to be recruited into a new job... the Adventeror.')
sleep()

while True:
    combatstyle = input(f'{garen}so what kind of combat style do you wish to learn?\n[Tank][Berserker][Paladin][SwordMaster]\n')
    if combatstyle.lower() == 'tank':
        combatstyle = Tank
        break
    elif combatstyle.lower() == 'paladin':
        combatstyle = Paladin
        break
    elif combatstyle.lower() == 'swordmaster':
        combatstyle = SwordMaster
        break
    elif combatstyle.lower() == 'berserker':
        combatstyle = Berserker
        break
    else:
        print(f"[{combatstyle} Is an invalid entry... try again.]")
        sleep()
print(combatstyle)
