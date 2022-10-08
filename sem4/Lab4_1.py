class BoxException(Exception):
    '''A Box Excpeiont'''

class Box:

# The class consists of:
#  A class variable _maxItems = 10 that specifies the maximum number of
# items the box can hold.

    _maxItems = 10

#  An instance variable numberOfItems, that represents the number of items
# in the box
#  A constructor that will initialise numberOfItems. If this value exceeds the
# max items the box can hold, throw an exception with a message.

    def __init__(self, numberOfItems):
        if numberOfItems > type(self)._maxItems:
            raise BoxException(f'{numberOfItems} cannot fit into a box of {type(self)._maxItems}')
        self._numberOfItems = numberOfItems

#  A method, remove(items), that will remove items from the box. Throw an
# exception if the removal will result in negative number of items.

    def remove(self, itemsToBeRemoved):
        if itemsToBeRemoved > self._numberOfItems:
            raise BoxException(f'{itemsToBeRemoved} cannot be removed as it is more than {self._numberOfItems}')
        self._numberOfItems -= itemsToBeRemoved 

#  A method, add(items), that will add items to the box. Throw an exception if
# the addition will result in more than the max items allowed.

    def add(self, itemsToBeAdded):
        subtotal = itemsToBeAdded + self._numberOfItems
        if subtotal > type(self)._maxItems:
            raise BoxException(f'{itemsToBeAdded} items cannot be added to {self._numberOfItems} as {subtotal} is more than {type(self)._maxItems}')
        self._numberOfItems = subtotal

#  A __str__() method that returns a string “Number of items: X’.

    def __str__(self):
        return f'Number of items {self._numberOfItems}'

# c. Test Box class by create a Box object and testing the add and remove methods.
# Exceptions must be taken care of. Include suitable display of messages
# informing the user what is happening when executing your program.

if __name__ == "__main__":

    try:
        b1 = Box(5)
        # b2 = Box(12)
        b1.add(3)
        # b1.add(3)

        b1.remove(4)
        b1.remove(5)

    except BoxException as e:
        print(e)