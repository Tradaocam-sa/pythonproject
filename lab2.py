import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import ttkbootstrap as ttk

root = tk.Tk()
root.title("Transcript")

connection = sqlite3.connect('transcript.db')

TBL_NAME = "transcriptInfo_table"
ID = "student_id"
NAME = "std_name"
DOB = "std_dob"
ADDRESS = "std_address"
PHONE = "std_phone"
GENDER = "std_gender"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TBL_NAME + " ( " + ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, "+ 
                   NAME + " TEXT, " + DOB 
                   +" TEXT, " + ADDRESS + "  TEXT ," +
                   PHONE + " INTEGER,"
                   + GENDER + " TEXT); ")

                   
appLabel = ttk.Label(root, text = "Transcript information of student", foreground="#568DE5", width= 40)
appLabel.config(font=("Inria Sans Bold Italic",30) )
appLabel.grid(row= 0, columnspan=2, padx= (10,10), pady = (30,0))

class Student:
    studentName = ""
    studentDoB = ""
    studentAddress = ""
    studentPhone = 0
    studentGender = ""

    def __init__(self, studentName, studentDoB, studentAddress, studentPhone, studentGender):
        self.studentName = studentName
        self.studentDoB = studentDoB
        self.studentAddress = studentAddress
        self.studentPhone = studentPhone
        self.studentGender = studentGender

nameLabel = ttk.Label(root, text = "Enter student's name", width=40, anchor='w',font=("Inria Sans Bold Italic",14)).grid(row=1,column=0,padx=(10,0),pady=(30,0))
                                                                                                
dobLabel = ttk.Label(root, text = "Enter student's DoB", width=40, anchor='w',font=("Inria Sans Bold Italic",14)).grid(row=2,column=0,padx=(10,0) )
addressLabel = ttk.Label(root, text = "Enter student's address", width=40, anchor='w',font=("Inria Sans Bold Italic",14)).grid(row=3,column=0,padx=(10,0) )
phoneLabel = ttk.Label(root, text = "Enter student's phone number", width=40, anchor='w',font=("Inria Sans Bold Italic",14)).grid(row=4, column=0,padx=(10,0))                                                                                      
genderLabel = ttk.Label(root, text = "Gender", width=40, anchor='w',font=("Inria Sans Bold Italic", 14)).grid(row=5,column=0,padx=(10,0))                                                                                                


nameEntry = ttk.Entry(root, width= 30)
dobEntry = ttk.Entry(root, width=30)
addressEntry = ttk.Entry(root,width=30)
phoneEntry = ttk.Entry(root, width=30)                                                                                  
genderEntry = ttk.Entry(root, width=30)


nameEntry.grid(row=1, column= 1, padx=(0,10), pady=(30,20))
dobEntry.grid(row=2, column=1, padx=(0,10), pady=(20))
addressEntry.grid(row=3, column= 1, padx=(0,10),  pady=20)
phoneEntry.grid(row=4, column=1, padx=(0,10), pady=20)
genderEntry.grid(row=5, column=1, padx=(0,10), pady=20)


def information_input():
    global nameEntry, dobEntry, addressEntry, phoneEntry, genderEntry
    global list
    global TBL_NAME, NAME, DOB, ADDRESS, PHONE, GENDER
    stdName = nameEntry.get()
    nameEntry.delete(0,ttk.END)
    dob = dobEntry.get()
    dobEntry.delete(0,ttk.END)
    address = addressEntry.get()
    addressEntry.delete(0,ttk.END)
    phone = phoneEntry.get()
    phoneEntry.delete(0, ttk.END)
    gender = genderEntry.get()
    genderEntry.delete(0, ttk.END)

    connection.execute("INSERT INTO " + TBL_NAME + " ( " + NAME + ", " +
                       DOB + ", " + ADDRESS + ", " + PHONE + ", "
                       + GENDER + " ) VALUES ( '"
                       + stdName + "', '" + dob + "','" + address + "', " + str(phone)
                       + ", '" + gender + "' ); ")
    
    connection.commit()
    messagebox.showinfo("Student's information saved")

    
def hideWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display information")

    tabLabel = ttk.Label(secondWindow, text = "Transcirpt information management", foreground='#568DE5', width= 50)
    tabLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="DoB")
    tree.heading("three", text="Address")
    tree.heading("four", text= "Phone number")
    tree.heading("five", text= "Gender")


    cursor =  connection.execute("SELECT * FROM "+ TBL_NAME + " ;")
    i = 0
    
    for row in cursor:
        tree.insert('', i , text = "Student " + str(row[0]),
                    values=(row[1], row[2], 
                            row[3], row[4], 
                            row[5]))
        i = i + 1
    
    tree.pack()
    secondWindow.mainloop()
    

# def deleteInfo():
#     root.destroy

    
        
                                                                                        
button = ttk.Button(root, text= "Add student", command= lambda: information_input())                                                                        
button.grid(row= 6, column= 0, pady=30)

displayButton = ttk.Button(root, text= "Show list", command=lambda:  hideWindow())
displayButton.grid(row=6, column=1)





                                                                                      
                                                                                               
                                                                                                

                                                                                     
                                                                                                
                                                                                                

root.mainloop()
