'''This program demonstrates how classes and object orientation work'''

class Enemy:
    '''The enemy objects are what the player fights in the game'''

    def __init__(self, name, health):
        '''The init function is called when a new object is instantiated'''
        #set name
        self._name = name
        #set initial health value use _ to indicate private object
        self._health = health

        #append new enemy into the enemy list
        enemy_list.append(self)

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

def display_enemies():
    '''This function loops through enemy_list and displays their name and health'''
    for e in enemy_list:
        print(f"{e.get_name()} has {e.get_health()} health")

#create a list to store all enemy objects
enemy_list = []


# create a new enemy object
Enemy("Ethan Adams", 1000)
Enemy("Ryan stewart", 0.01)

display_enemies()