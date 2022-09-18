class ToDo:
    def __init__(self, event):
        self._event = event
        self._actions = []
    
    @property
    def event(self):
        return self._event
    
    def addToDo(self, action):
        self._actions.append(action)
    
    def removeToDoItem(self, index):
        if 1 <= index <= len(self._actions):
            self._actions.pop(index-1)
            return True
        else:
            return False

    def __str__(self):  
        listStr = ""
        for i, action in enumerate(self._actions):
            listStr += str(i+1) + '. ' + action + '\n' 
        return f"Event: {self._event}\n{listStr}"
    

if __name__ == "__main__":
    
    td = ToDo('Orientation camp')

    print()

# The class has 2 instance parameters. They are:
#  the event (string)
#  a list collection to store the to-do actions

# The constructor that has an event as parameter. The constructor initializes an
# empty collection.

# It has the following methods:
#  A getter property for the event name.
#  A addToDo( toDo) method that adds the toDo (string) action to the
# collection.

    td.addToDo("Bring passport")
    td.addToDo('Change money')
    td.addToDo('Bring medicine')

    print()

#  A removeToDoItem(index) method that removes a to-do item using the
# index position of the todo item. Return True if successful and False
# otherwise.

    td.removeToDoItem(1)

    print()

#  __str__() method that returns a string of all the toDo action items in the
# following format:

    print(td)
    
    print()

# Test the ToDo class, with the following:
# i. Create a ToDo object for an “Orientation camp” event.
# ii. Add a few to do actions to the object.
# iii. Display the to do list.
# iv. Remove a to do action and display the outcome of the removal