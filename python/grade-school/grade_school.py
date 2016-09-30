# create a Grade school class that stores a school name, grades 1-9, and the students in each grade

class School:
    def __init__(self,name):
        self.name = name
        self.grades = {n: [] for n in range(1,10)}

    def grade(self,grade):
        return sorted(self.grades[grade])

    def add(self, student, grade):
        self.grades[grade].append(student)

    def sort(self):
        return [(n, tuple(self.grade(n))) for n in range(1,10) if self.grade(n)]
