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

combatstyle = Paladin
SpecificlvlUp(combatstyle, 'health')

