from Students import Student
from Courses import Course


student_list = []
course_list = []
while True:
    print(f'''
    0. Exit.
    1. Add new student.     
    2. Edit student's informations.      
    3. Delete student.
    4. Show all in formation of all students.
    5. Show information of choosen student.
    6. Add new course.
    7. Edit course's name.
    8. Add student's attendance.
    9. Add student's mid term mark.
    10. Add student's final mark.
    11. Edit student's attendance.
    12. Edit student's mid-term mark.
    13. Edit  student's final mark.
    14. Show all information of all courses.
    15. Show all grade of a student in a course.
    
    
    ''')
    
    select = input("Pick a fuction: ")
    
    if str(select).isdigit():
        select = int(select)
        if select == 1:
            id = input("Enter student's id: ")
            for i in student_list:
                while i.get_id() == id:
                    print("The ID has assigned to other student")
                    id = input("Enter another ID: ")
            name = input("Enter student's name: ")
            dob = input("Enter student's department: ")
            email = input("Enter student's email: ")
            phoneNumber = input("Enter student's telephone number: ")
            birth = input("Enter student's birth: ")
            student = Student(id, name, dob, email, phoneNumber, birth)
            student.standardizing()
            student_list.append(student)
        
        
                    
        elif select == 2:
            id = input("Enter ID of student that you want to change information: ")
            for i in student_list:
                if i.get_id() == id:
                    print(f'''
                      a. Change name.
                      b. Change dob.
                      c. Change email.
                      d. Change phone number.
                      e. Change birth.
                      
                      ''')
                    choose = input("Choose a function you want: ")
                    if choose == 'a':
                        i.set_name(input("Change name of student to: "))
                    elif choose == 'b':
                        i.set_dob(input("Change DoB to: "))
                    elif choose == 'c':
                        i.set_email(input("Change email to: "))
                    elif choose == 'd':
                        i.set_phoneNumber(input("Change telephone number to: ")) 
                    elif choose == 'e':
                        i.set_birth(input("Change email to: "))
            i.standardizing()
                        
        elif select == 3:
            id = input("Enter ID of student that you want to remove from the list:")
            for i in student_list:
                if i.get_id() == id:
                    student_list.remove(i)
                    print("You deleted")
                    
        elif select == 4:
            if len(student_list) != 0:
                for i in range(len(student_list)):
                    print(student_list[i].get_student())
            else:
                print("There is no student, you need to add student to the list.")
                
                  
        elif select == 5:
            id = input("Enter ID of student that you want to see informations: ")
            for i in student_list:
                if i.get_id() == id:
                    print(i.get_student())
                    
        elif select == 6:
            course_id = input("Enter course's id: ")
            for i in course_list:
                while i.get_course_id() == course_id:
                    print("The ID has assigned to other course")
                    course_id = input("Enter another ID: ")
            course_name = input("Enter course's name: ")
            course = Course(course_id, course_name)
            course_list.append(course)
            
        elif select == 14:
            for i in course_list:
                print(i.get_course())
            
        elif select == 7:
            course_id = input("Enter ID of the course you want to change name: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    i.set_course_name(input("Change name of course to: "))
        
        elif select == 8:
            course_id = input("Enter ID of course you want add attendance grade for student: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id = input("Enter ID of student you want to add attentance mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            i.set_attendance(input("Attendance mark: "), j.get_id())
        
        elif select == 9:
            course_id = input("Enter ID of course you want add mid-term grade for student: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id = input("Enter ID of student you want to add mid-term mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            i.set_midTerm(input("Mid-term mark: "), j.get_id())
                        
        elif select == 10:
            course_id = input("Enter ID of course you want add final grade for student: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id = input("Enter ID of student you want to add final mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            i.set_final(input("Final mark: "), j.get_id())
        
        
        elif select == 11:
            course_id = input("Enter ID of course you want to edit attendance grade for student: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id = input("Enter ID of student you want to edit attendance mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            i.set_attendance(input("Attendance mark change to : "), j.get_id())
                            
        elif select == 12:
            course_id = input("Enter ID of course you want to edit mid-term grade for student: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id = input("Enter ID of student you want to edit mid-term mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            i.set_midTerm(input("Mid-term mark change to: "), j.get_id())

        elif select == 13:
            course_id = input("Enter ID of course you want to edit final grade for student: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id = input("Enter ID of student you want to edit final mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            i.set_midTerm(input("Final mark change to: "), j.get_id())
                            
        elif select == 15:
            course_id = input("Enter ID of course that you want to show student's grade: ")
            for i in course_list:
                if i.get_course_id() == course_id:
                    id == input("Enter ID of student you want to show mark: ")
                    for j in student_list:
                        if j.get_id() == id:
                            print(f'Student ID: {j.get_id()}, Student Name: {j.get_name()}, Attendance in {i.get_course_name()}: {i.get_attendance(j.get_id())}, Mid-term: {i.get_midTerm(j.get_id())}, Final: {i.get_final(j.get_id())}') 
                            
        
    else:
        print("\n You have to input a number !!!")