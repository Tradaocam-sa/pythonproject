class Course:
    def __init__(self, course_id, course_name):
        
        self.__course_attendance = {}
        self.__course_mid_term ={}
        self.__course_final = {}
        self.__course_id = course_id
        self.__course_name = course_name
    def get_course_id(self):
        return self.__course_id
    def get_course_name(self):
        return self.__course_name
    
    def set_course_name(self, course_name):
        self.__course_name = course_name
    def get_course(self):
        return f'ID: {self.__course_id } Name: {self.__course_name}'
    
    def set_attendance(self, course_attendance, id):   #Attendance of student in each course
        self.__course_attendance[id] = course_attendance
    def get_attendance(self, student_id):
        return self.__course_attendance[student_id]
    
    def set_midTerm(self, course_mid_term, id):  #Midterm of student in each course
        self.__course_mid_term[id] = course_mid_term
    def get_midTerm(self, student_id):
        return self.__course_mid_term[student_id]
    
    def set_final(self, course_final, id):  #Midterm of student in each course
        self.__course_final[id] = course_final
    def get_final(self, student_id):
        return self.__course_mid_term[student_id]
    