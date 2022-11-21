class DataSheet():
    """This is a data sheet"""

    def __init__(self, courses=[]):
        self.courses = courses

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)
        return grades

    def __repr__(self):
        return 'DataSheet(%r)' % (self.courses)
