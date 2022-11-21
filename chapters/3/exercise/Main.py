import csv
import random
from Student import Student
from DataSheet import DataSheet
from Course import Course
import matplotlib.pyplot as plt

names = ['Hermonie', 'Draco', 'Luna', 'Ron', 'Neville', 'Ginny', 'Harry', 'Fred', 'George', 'Newt']
genders = ['male', 'female']
img_urls = ['img1', 'img2', 'img3']
grades = [None, -3, 0, 2, 4, 7, 10, 12]
courses = [
    Course('Transfiguration', 'Room1', 'Minerva McGonagall', 30, None),
    Course('Potions', 'Room2', 'Severus Snape', 60, None),
    Course('Care of Magical Creatures', 'Room3', 'Hagrid', 30, None),
    Course('Defense Against the Dark Arts', 'Room4', 'Remus', 60, None),
    Course('Charms', 'Room5', 'Filius Flitwick', 30, None)
]


def get_random_name():
    return names[random.randint(0, 9)]


def get_random_gender():
    return genders[random.randint(0, 1)]


def get_random_courses():
    amount_of_course = random.randint(0, 4)
    s_courses = []
    s_course_indexes = set()
    for i in range(amount_of_course):
        s_course_indexes.add(random.randint(0, 4))

    for index in s_course_indexes:
        grade = grades[random.randint(0, 7)]
        s_course = courses[index]
        s_course.grade = grade
        s_courses.append(s_course)

    return s_courses


def get_random_img_url():
    return img_urls[random.randint(0, 2)]


def create_random_student():
    s_name = get_random_name()
    s_gender = get_random_gender()
    s_courses = get_random_courses()
    s_img_url = get_random_img_url()
    return Student(s_name, s_gender, DataSheet(s_courses), s_img_url)


def get_random_students():
    amount_of_students = random.randint(1, 10)
    students = []
    for student in range(amount_of_students):
        students.append(create_random_student())
    return students


def write_students_data():
    with open('students.csv', 'w') as file:
        file.write('id,stud_name,gender,img_url,course_name,classroom,teacher,ects,grade\n')
        students = get_random_students()
        id = 0

        for student in students:
            #Checks if a student has no registered courses
            if student.data_sheet.courses == []:
                print("none")
                file.write(
                    ('{id},{name},{gender},{img_url},{course_name},{classroom},{teacher},{ects},{grade}\n'
                     .format(id=id, name=student.name, gender=student.gender, img_url=student.image_url,
                             course_name=None, classroom=None, teacher=None, ects=None, grade=None)))
            else:
                for course in student.data_sheet.courses:
                    file.write(
                        ('{id},{name},{gender},{img_url},{course_name},{classroom},{teacher},{ects},{grade}\n'
                         .format(id=id, name=student.name, gender=student.gender, img_url=student.image_url,
                                 course_name=course.name,
                                 classroom=course.classroom, teacher=course.teacher, ects=course.ETCS,
                                 grade=course.grade)))
            id += 1


def read_students_data():
    with open('students.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)
        students = []
        for id, stud_name, gender, img_urls, course_name, classroom, teacher, ects, grade in reader:
            id = int(id)
            course = Course(course_name, classroom, teacher, ects, grade)
            courses = [course]
            student = Student(stud_name, gender, DataSheet(courses), img_urls)

            #Checks if student does not exist yet in list (id same as index)
            if len(students) <= id:
                students.append(student)
            else:
                students[id].data_sheet.courses.append(course)

        return students

def print_students_avg(students):
    for student in students:
        # print(student.__repr__())
        print('{name}, {img_url}, {avg_grade}'.format(name=student.name, img_url=student.image_url,
                                                      avg_grade=student.get_avg_grade()))
    return students

def sort_students_by_avg_grade(students):
    return sorted(students, key=lambda student: student.get_avg_grade())

def get_bar_char_students_grade(students):
    sorted_students = sort_students_by_avg_grade(students)
    print_students_avg(sorted_students)

    plt.bar([student.name + str(sorted_students.index(student)) for student in sorted_students], [student.get_avg_grade() for student in sorted_students], align='center')
    plt.show()


if __name__ == '__main__':
    write_students_data()
    students = read_students_data()
    students1 = sort_students_by_avg_grade(students)
    get_bar_char_students_grade(students)