#Dictionary to hold each students information

grade_book = {}

#ARGS AND KWARGSS
# WE MUST HAVE STUDENT NAME AND DEPARTMENT -
# KWARGS WOULD BE SUBJECT AND GRADE

def add_student(name, department, **kwargs):
    """
    adds a student to the grade_book

    param
    name (str): name of student to be added
    department (str): department of the student
    kwargs: a dict for more information on the student

    return:
    none
    """

    #create a new dictionary in the grade_book to hold the student's information using their name as key
    grade_book[name] = {'department': department}

    # We get the students dictionary from grade_book using their name as key
    student_dict = grade_book.get(name)

    #Create a subjects dictionary to hold all subjects in the students dictionary
    student_dict['subjects'] = {}

    #We get the students subjects dictionary
    subjects = student_dict.get('subjects')

    for key, value in kwargs.items():
        #We add the subject and scores
        subjects[key] = value


#Add or Upgrade Grades
def add_update_grade(name, department,**kwargs):
    """
        adds a new student to the grade_book
        updates the score of a student in the grade_book

        param
        name (str): name of student to be added or name of student whose score is to be updated
        department (str): department of the student
        kwargs: a dict for more information on the student

        return:
        none
        """

    #check if the person is a student we can look through
    student = grade_book.get(name)
    if student is None:
        print("This student does not exist. Inputting grades")
        add_student(name, department, **kwargs)
    else:
        subjects = student.get("subjects")
        for subject, score in kwargs.items():
            #Check if we have the subject
            curr_subject = subjects.get(subject)
            if curr_subject is None:
                subjects.setdefault(subject, score)
                print(f"We just added a new subject : {subject} - {score}")
            else:
                subjects[subject] = score

#Calculate the Average Grade per student
def average_student_grade(name):
    """
        calculates the average score of a student in the grade_book

        param:
        name (str) of the student

        return:
        the average score of a student (int)
        none, if student's name is not in the grade_book
        """
    student = grade_book.get(name)
    if student is None:
        print(f"Cannot Find student: {name}")
    else:
        #Average = sum of items / no. of items
        subjects = student.get("subjects")
        sum_of_items = 0
        no_of_items = 0

        for score in subjects.values():
            sum_of_items = sum_of_items + score
            no_of_items = no_of_items + 1
        average = sum_of_items / no_of_items
        print(name)
        print(student)
        print(average)
        return average



add_student("Mahmud", "Computer Science", DSA=70, Applied_Math = 60)
add_student("Aisha", "Medicine", Anatomy=90, Zoology=75, Botany=67)
add_update_grade("Aisha", "Medicine", Psychology=70, Botany=77)
add_update_grade("Seyi", "Economics", Statistics=80, Marketing=76)
# print(grade_book)
average_student_grade("Mahmud")
average_student_grade("Olamide")