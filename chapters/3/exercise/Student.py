class Student():
    """ This is a student"""

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        all_grades = self.data_sheet.get_grades_as_list()
        grade_sum = 0
        amount_of_courses = len(self.data_sheet.courses)

        # if student has been registered to one or more courses
        if amount_of_courses > 0:
            for grade in all_grades:
                # if the student has not registered a grade for the course,
                # this grade will not count in the amount of courses with a grade for calculating the avg grade
                if grade == 'None':
                    amount_of_courses -= 1
                else:
                    grade_sum += float(grade)

            # if the student has courses but no grades registered yet
            if amount_of_courses == 0:
                return 0
            else:
                avg = grade_sum / amount_of_courses #calculating the avg
                return avg
        else:
            return 0 #if no grades are registered yet


    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def __str__(self):
        return '{name}, {gender}, {img}'.format(
            name=self.name, gender=self.gender, imp=self.image_url
        )
