class Person:
    def __init__(self, gender, name, lastname):
        self._gender = gender.lower()
        self._name = name.title()
        self._lastname = lastname.capitalize()
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        self._name = newName.title()
    
    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, newLastName):
        self._lastname = newLastName.capitalize()

    def getFullName(self):
        if self._gender == 'f':
            return f"Ms. {self._lastname} {self._name}"
        else:
            return f"Mr. {self._lastname} {self._name}"
    
    def getInitials(self):
        names = self._name.split(' ')

        initials =""
        for x in names:
            initials += x[0] + ". "

        return f"{initials}{self.lastname}"

    def __str__(self):
        return f"Name: {self._lastname} {self._name}, Gender: {self._gender.upper()}"

if __name__ == "__main__":

    p1 = Person('M', 'ah seng', 'tan')
    p2 = Person('F', 'betty mary', 'lee')

    
#     It has the following methods:
# - getFullName() returns the full name with a salutation “Mr.“ or “Ms.”,
# depending on the person’s gender (m or f). The name is given in this order:
# the last name, name followed by the middle name, e.g., “Mr. Ong Ah Seng”

    print(p1.getFullName())
    print(p2.getFullName())



# - getInitials() returns the first letter of the name separated by blanks, followed
# by the lastname. E.g. it may return “A. Ong”.

    print(p1.getInitials())
    print(p2.getInitials())



# - __str__() method that returns a string representation of a Person object as in:
# Name: Ong Ah Seng Gender : Male

    print(p1)
    print(p2)

    print() 