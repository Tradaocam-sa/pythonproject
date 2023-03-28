
import numpy as np

class Student:
    def __init__(self,  id, name, dob, email, phoneNumber, birth ):
        self.__gpa = []
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__birth = birth
        
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
    def get_email(self):
        return self.__email
    def get_phoneNumber(self):
        return self.__phoneNumber
    def get_birth(self):
        return self.__birth
    def set_name(self, name):
        self.__name = name
    def set_dob(self, dob):
        self.__dob = dob
    def set_email(self, email):
        self.__email = email
    def set_phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber
    def set_birth(self, birth):
        self.__birth = birth
    def get_student(self):
        return f'ID: {self.__id} , Name: {self.__name} , DoB:{self.__dob} , Email: {self.__email}, Telephone Number: {self.__phoneNumber} , Birth: {self.__birth}'
    def set_gpa(self,  mark):
        self.__gpa.append(mark)
    def get_gpa(self):
        return np.average(self.__gpa)
    
    def standardizing(self):
        if self.__birth[1] == '/':
            self.__birth = '0' + self.__birth
        if self.__birth[4] == '/':
            self.__birth = self.__birth[0 : 3] + '0' + self.__birth[3 : ]
        tmp = self.__name.split()
        res = ' '.join(tmp)
        res = res.title()
        self.__name = res
    

    

        


          
