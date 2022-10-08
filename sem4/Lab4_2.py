class InvalidAssessmentException(Exception):
    '''Invalid Assessment Exception'''

# b. The Assessment class models an assessment for a student. Write the class
# with the following:

#  Id and mark are instance variables for this class.
#  It has a class variable _max which is the maximum mark that can be
# achieved for this assessment. Set this to _max = 100.

class Assessment:

    _max = 100
    def __init__(self, id, mark):
        self._id = id
        self._mark = mark
    
#  Write a class method for getMaxMark that returns the class variable
# _max.

    @classmethod
    def getMaxMark(cls):
        return cls._max

#  Write a class method for setMaxmark that sets the class variable _max
# to the mark provided in the parameter.

    @classmethod
    def setMaxmark(cls, newMax):
        cls._max = newMax

#  Write the getter for id and mark.

    @property
    def id(self):
        return self._id

    @property
    def mark(self):
        return self._mark

#  Write a setter for mark. A mark can only be between 0 and _max,
# otherwise raise an InvalidAssessmentException with the message
# ‘Mark can only be between 0 and ?’ where ? is _max.

    @mark.setter
    def mark(self, newMark):
        if newMark < 0 or newMark > type(self)._max:
            raise InvalidAssessmentException(f"Mark can only be between 0 and {type(self)._max}")
        self._mark = newMark

#  __str__ to return the id and mark

    def __str__(self):
        return f'Id: {self.id}, Mark: {self.mark}'

# . TutorialGroup class. The class models a tutorial group with a name and a
# dictionary of assessments. Write the class with the following:
#  Instance variable name to represent the tutorial group name.
#  An empty dictionary _assessments = { } in the constructor.

class TutorialGroup:
    def __init__(self, name):
        self._name = name
        self._assessments = {}

#  addAssessment(id, mark) method. Adds an assessment to the
# dictionary. If the id is already in the dictionary, then raise an
# InvalidAssessmentException with a message ‘Assessment for ?
# already added!’ where ? is the id.

    def addAssessment(self, id, mark):
        a = Assessment(id, mark)
        if id in self._assessments:
            raise InvalidAssessmentException(f'Assessment for {id} already added')
        self._assessments[id] = a

#  removeAssessment(id) method. Removes an assessment from the
# dictionary. Raise the following exceptions:
# i. If the id is not found, raise an InvalidAssessmentException with a
# message ‘Assessment for ? not found!’.
# ii. An assessment mark must be 0 before it can be removed. If the
# mark is not 0, raise an InvalidAssessmentException with a
# message ‘Cannot remove if assessment mark is not 0’.

    def removeAssessment(self, id):
        if id not in self._assessments:
            raise InvalidAssessmentException(f'Assessment for {id} not found')
        if self._assessments[id].mark != 0:
            raise InvalidAssessmentException(f'Cannot remove if assessment mark is not 0')
        self._assessments.pop(id)

#  adjustAssessment(id, mark) method. Mark is the mark to adjust to.
# Before adjusting, check and raise the following exceptions:
# i. If the id is not found, raise an InvalidAssessmentException with a
# message ‘Assessment for ? not found!’.
# ii. If the mark to adjust to is the same as the current mark, raise an
# InvalidAssessmentException with a message ‘Mark to adjust is the
# same as existing mark!’.

    def adjustAssessment(self, id, newMark):
        if id not in self._assessments:
            raise InvalidAssessmentException("Assessment for {id} not found!")
        if self._assessments[id].mark == newMark:
            raise InvalidAssessmentException("Mark to adjust is the # same as existing mark!")
        self._assessments[id].mark = newMark

#  __str__ method. Returns a string of all the assessment marks, one per
# line.

    #https://www.w3schools.com/python/ref_string_join.asp 
    def __str__(self): # using list/tupple constructor
        assessmentStr = '\n'.join(str(a) for a in self._assessments.values())
        if assessmentStr == "":
            assessmentStr = "No assessment currently"
        return f'{self._name}\n{assessmentStr}'

def getInt(message, menu=None):
    while True:
        try:
            return int(input(f'{menu if menu else ""}Enter {message}: '))
        except ValueError as e:
            print(f'''The input {str(e).split("'")[1]} is not a whole number''')

def addAssessment(tg):
    studentId = input('Enter studentId: ')
    mark = getInt('mark')
    try:
        tg.addAssessment(studentId, mark)
        print('Added!')
    except InvalidAssessmentException as e:
        print(e)

def main():
    tg = TutorialGroup('T01')
    while True:
        option = getInt('option', '''Menu
1.  Add assessment
2.  Remove assessment
3.  Adjust assessment
4.  List all assessment 
5.  Quit.
''')
        if option == 1:
            addAssessment(tg)
        elif option == 2:
            # removeAssessment(tg)
            pass
        elif option == 3:
            # adjustAssessment(tg)
            pass
        elif option == 4:
            print(tg)
        elif option == 5:
            break
        else:
            print('Invalid menu option')
        print(tg)
        print()
      
if __name__ == "__main__":

    main()
       # try:
    #     as1 = Assessment("S1", 100)
    #     # as1.mark = 101
    #     tg1 = TutorialGroup('T1')
    #     tg1.addAssessment("S2", 70)
    #     # tg1.addAssessment("S2", 71)
    #     # tg1.removeAssessment('S2')
    #     tg1.addAssessment("S1", 0)
    #     tg1.removeAssessment("S1")
    #     # tg1.removeAssessment("S1")
    #     print(tg1)
    # except InvalidAssessmentException as e:
    #     print(e)

