class Character:
    name = input('Enter the hero name: ')
    id = input('Enter the character ID number: ')
    level = int(input('Enter the hero level: '))
    loot = float(input('Enter the hero loot value: '))

    class hero(Character):
        name = "Knight"
        id = 111
        level = 1 
        loot = 50.00



    def __init__(self, name, character, level, loot):
        self.name = name
        self.character = character
        self.level = level
        self.loot = loot
    
        print("names of characters and attributes")
        print(name)
        print(id)
        print(level)
        print(loot)
        print(hero)

class Boss:
    name = (input('Enter the Boss name '))
    character = (input('Enter the character ID number: '))
    level = int(input('Enter the hero level: '))
    hp = int(input('Enter The HP of the character '))
    attack_points = (int(input("Enter The attack points here ")))
    lifespan = (hp / 300)

    class Boss(Ogre):
        name = "ogre"
        character = 333
        level = 2
        hp = 5500
        attack_damage = 99

    def __init__(self, name, character, level, loot, hp, attack_points, lifespan):
        self.name = name
        self.character = character
        self.level = level
        self.loot = loot
        self.hp = hp
        self.attack_points = attack_points
        self.lifespan = lifespan

        print("names of Bosses and attributes")
        print(name)
        print(character)
        print(level)
        print(hp)
        print(attack_points)
        print(lifespan)
        print(Ogre)