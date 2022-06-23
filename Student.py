''' This program is for creating students into an object orientated way'''

#classes should have a capital first letter
class Student:
    '''This holds all the student objects'''
    def __init__(self, name, age, phonenumber, enrollment, classes):
        '''The init function is called when a new object is instantiated'''
        #sets name
        self._name = name
        #sets age
        self._age = age
        #sets phonenumber
        self._phonenumber = phonenumber
        #sets enrollment
        self._enrollment = enrollment
        if enrollment == True:
            #sets classes the student is in
            self._classes = classes
        else:
            self._classes = "Student has no classes"
        student_list.append(self)

    def get_name(self):
        ''' THis function returns the name of the student object'''
        return self._name

    def get_age(self):
        '''This is a getter function that returns the age of the student object'''
        return self._age

    def get_phonenumber(self):
        '''This is a getter function that returns the phonenumber of the student object'''
        return self._phonenumber

    def get_enrollment(self):
        '''This is a getter function that returns the enrollment of the student object'''
        return self._enrollment

    def get_classes(self):
        '''This is a getter function that returns the classes of the student object'''
        return self._classes

def display_students():
    '''This function loops through enemy_list and displays their name and health'''
    for student in student_list:
        print(f"Name: {student.get_name()}")
    print("")

def display_student(name):
    '''This function loops through enemy_list and displays their name and health'''
    for student in student_list:
        if name in student.get_name():
            print("="*30)
            print(f"Name: {student.get_name()}\nAge: {student.get_age()}\nPhone Number: {student.get_phonenumber()}\nEnrollment status: {student.get_enrollment()}\nClasses: {student.get_classes()}")
            print("="*30)
            print("")

def generate_students():
    '''Import students from a csv file'''
    #import the scv package to enable the program to work with a csv
    import csv
    #open the csv file, call is csvfile
    with open("myRandomStudents.csv", newline='') as csvfile:
        #use the reader() function and put the results intp a vairable called filereader
        filereader = csv.reader(csvfile)
        #loop through the csv, one row at a time
        for line in filereader:
            #for each row, we grab the classes in columns D-H and put them into a list
            #the classes can be found in line[3] to line[7]
            classes = []
            i=3
            while i in range(3,8):
                classes.append(line[i])
                i += 1
                #create a new student object
            Student(line[0],int(line[1]),line[2],True,classes)

student_list = []

generate_students()
display_students()

name = input("Enter name of student:\n")
display_student(name)

