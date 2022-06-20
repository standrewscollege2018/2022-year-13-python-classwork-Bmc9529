'''This program demonstrates how classes and object orientation work'''

class Enemy:
    '''The enemy objects are what the player fights in the game'''
    #set initial health value use _ to indicate private object
    _health = 3
    def get_health(self):
        '''This is a getter function that returns the health of the enemy'''
        return self._health

# create a new enemy object
enemy1 = Enemy()
print(f"Enemy has {enemy1.get_health()} health left")