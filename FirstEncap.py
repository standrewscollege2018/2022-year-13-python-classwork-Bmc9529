'''This program demonstrates how classes and object orientation work'''

class Enemy:
    '''The enemy objects are what the player fights in the game'''

    def __init__(self, name, health):
        '''The init function is called when a new object is instantiated'''
        #set name
        self._name = name
        #set initial health value use _ to indicate private object
        self._health = health

        #scare the world with evil laugh
        print(f"mwa ga ga ga, {self._name} has been born")

    def get_name(self):
        ''' THis function returns the name of the enemy object'''
        return self._name

    def get_health(self):
        '''This is a getter function that returns the health of the enemy'''
        return self._health

    def attacked(self, damage):
        '''This function is called when the enemy is attacked. The damage value is deducted from the _health value'''
        self._health -= damage
        if self._health <=0:
            print("*Poof*")
        else:
            print("Ouch")

# create a new enemy object
enemy1 = Enemy("Ethan Adams", 1000)
enemy2 = Enemy("Ryan stewart", 0.01)

attacking = True
print(f"{enemy1.get_name()} has {enemy1.get_health()} health left")
print(f"{enemy2.get_name()} has {enemy2.get_health()} health left")
while attacking == True:
    target = input("\nWho do you want to attack:\n")
    attack = float(input("\nHow much do you want to attack:\n"))
    if target == "Ethan Adams":
        enemy1.attacked(attack)
    elif target == "Ryan Stewart":
        enemy2.attacked(attack)
    else:
        print("\nNo one attacked")
    print(f"{enemy1.get_name()} has {enemy1.get_health()} health left")
    print(f"{enemy2.get_name()} has {enemy2.get_health()} health left")
