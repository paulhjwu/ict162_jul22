from abc import ABC, abstractmethod
class Fruit:
    def __init__(self, size, weight):
        self._size = size
        self._weight = weight
        
    def __str__(self):
        return f'{self._size} {self._weight}'
    
class Apple(Fruit):
    def __str__(self):
        return f'Apple {super().__str__()}'

class Orange(Fruit):
    def __str__(self):
        return f'Orange {super().__str__()}'        
        
class Papaya(Fruit):
    def __str__(self):
        return f'Papaya {super().__str__()}'      

class BasketException(Exception):
    '''Fruit with smaller size should cheaper'''
    
class Basket:
    def __init__(self, recipient, batchLoad, contents = None):
        self._recipient = recipient
        self._fruits = {'Orange': [], 'Apple': [], 'Papaya': []}
        if batchLoad:
            for line in contents.splitlines():
                details = line.split(',')
                if details[0] == 'Orange':
                    f = Orange(details[1], details[2])
                elif details[0] == 'Apple':
                    f = Apple(details[1], details[2])
                else:
                    f = Papaya(details[1], details[2])
                try:
                    self.addFruit(details[0], f)
                except BasketException as e:
                    print(e)
                
    def addFruit(self, fruitType, fruit):
        print(f"Adding {fruit}")
        fruitList = self._fruits.get(fruitType)
        if not fruitList:
            self._fruits[fruitType].append(fruit)
        else:
            found=False
            lastIndex = len(fruitList)-1
            for index, ft in enumerate(fruitList):
                if fruit._size == ft._size:
                    raise BasketException(f"Same fruit cannot have same size '{fruit}'/removed")
                elif ft._size > fruit._size:
                    if ft._weight <= fruit._weight:
                        raise BasketException(f"Price of fruit of smaller size '{fruit}'/removed must be ligher than '{ft}'")
                    elif fruitList[index-1]._weight >= fruit._weight:
                        raise BasketException(f"Price of fruit of larger size '{fruit}'/removed must be heavier than '{fruitList[index-1]}'")
                    else:
                        insertIndex = index
                        found=True
                        break
            if found:
                fruitList.insert(insertIndex,fruit)
            else:
                fruitList.insert(lastIndex+1, fruit)
                        
    def __str__(self):
        fruitStr = ""
        for key, fruitValues in self._fruits.items():
            fruitStr += f"{key}: \n"
            fruitStr += "\n".join(str(f) for f in fruitValues) or 'No fruit'
            fruitStr += "\n"
        return f'{self._recipient}\nFruits:\n{fruitStr}'
        
def main():
    
    inputData = '''Orange,1,3
Apple,2,3
Orange,3,8
Orange,2,3
Apple,1,4
Apple,3,5'''

    b2 = Basket('mary', True, inputData)
    print(b2)
    
main()