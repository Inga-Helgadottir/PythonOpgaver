class Student():
    def __init__(self, name, gender, image_url, grades=[], data_sheet=[]):
        self.name = name
        self.gender = gender
        self.image_url = image_url
        self.grades = grades
        self.data_sheet = data_sheet

    def __repr__(self):
        return 'Student(%r, %r, %r, %r, %r)' % (self.name, self.gender, self.image_url, self.grades, self.data_sheet)
    

    def get_avg_grade(self):
        if len(self.grades) >= 1:
            return sum(self.grades) / len(self.grades)
        else:
            return self.grades
        
class DataSheet():
    def __init__(self, name, courses=[]):
        self.name = name
        self.courses = courses

    def get_grades_as_list():
        return "Reminder make this function later"
        

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        if grade != None:
            self.grade = grade

# Create a function that can generate n number of students with random: 
# name, gender, courses (from a fixed list of course names), grades, img_url
from random import random
def generateRandomStudents(nbrOfStudents):
    c1 = Course(names[1], "classroom1", names[2], "ETCS")
    c2 = Course(names[3], "classroom2", names[1], "ETCS2", grades[2])
    c3 = Course(names[5], "classroom4", names[0], "ETCS2")
    c4 = Course(names[2], "classroom3", names[5], "ETCS2", grades[4])
    names = ["name1", "name2", "name3", "name4", "name5", "name6", "name7"]
    genders = ["male", "female"]
    courses = [c1, c2, c3, c4]
    grades = [-3, 0, 2, 4, 7, 10, 12]
    image_url = ["imageUrl1", "imageUrl2", "imageUrl3", "imageUrl4", "imageUrl5"]
    d1 = DataSheet(names[5], genders[0], courses[0])
    d2 = DataSheet(names[6], genders[1], courses[1])
    d3 = DataSheet(names[3], genders[1], courses[2])
    d4 = DataSheet(names[1], genders[0], courses[3])
    dataSheets = [d1, d2, d3, d4]
    listOfStudents = []
    for i in range(nbrOfStudents):
        s = Student(names[random], genders[i], image_url[i], grades=[], data_sheet=[])
        listOfStudents.append(s)