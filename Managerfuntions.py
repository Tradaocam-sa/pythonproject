import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


class Management(tk.Tk):
    def __init__(self, title, size, minsize):
            super().__init__()
        #SETUP
            self.title(title)
            self.geometry(f'{size[0]}x{size[1]}')
            self.minsize(minsize[0],minsize[1])

        #widget
            self.left = leftBackground(self)
            self.right = rightBackground(self)
        #RUN

            self.mainloop()

            
class leftBackground(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background='#A4C2F1').pack(expand = True, fill='both')
        self.place(x = 0, y = 0, relwidth= 0.3, relheight=1)

        #Button one
        frame1 = ttk.Frame(self)
        show_std_info_buton = ttk.Button(frame1, text = 'Show students', width=30)

        show_std_info_buton.pack(expand= True, fill='both',  padx=0, pady = 0)
        
        frame1.place(relx=0.15, rely= 0.05, )
        
        
        #Button two
        frame2 = ttk.Frame(self)
        show_info_course = ttk.Button(frame2, text = 'Show courses', width = 30 )
        
        show_info_course.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame2.place(relx=0.15, rely= 0.1 )
        
        #Button 3
        frame3 = ttk.Frame(self)
        Add_student = ttk.Button(frame3, text = 'Add student', width = 30 )
        
        Add_student.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame3.place(relx=0.15, rely= 0.15 )
        
        #Button 4
        frame4 = ttk.Frame(self)
        Add_mark = ttk.Button(frame4, text = 'Add mark', width = 30 )
        
        Add_mark.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame4.place(relx=0.15, rely= 0.2 )
        
        #Button 5
        frame5 = ttk.Frame(self)
        Add_course = ttk.Button(frame5, text = 'Add course', width = 30 )
        
        Add_course.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame5.place(relx=0.15, rely= 0.25 )
        
        
        #Button 6
        frame6 = ttk.Frame(self)
        Edit_info_course = ttk.Button(frame6, text = 'Edit information of course', width = 30 )
        
        Edit_info_course.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame6.place(relx=0.15, rely= 0.3 )
        
        #Button 7
        frame7 = ttk.Frame(self)
        edit_student_info = ttk.Button(frame7, text = 'Edit infomation of student', width = 30 )
        
        edit_student_info.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame7.place(relx=0.15, rely= 0.35 )
        
        #Button 8
        frame8 = ttk.Frame(self)
        Edit_mark = ttk.Button(frame8, text = 'Edit mark', width = 30 )
        
        Edit_mark.pack(expand= True, fill='both',  padx=0, pady = 0)
        frame8.place(relx=0.15, rely= 0.4 )
        
        
        

class rightBackground(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self,background='#CBDCF7').pack(expand = True, fill='both')
        self.place(relx= 0.3, y = 0, relwidth= 0.7, relheight=1)
        
        
        #Title
        frame1 = ttk.Frame(self)
        title = ttk.Label(frame1, text='TRANSCRIPT INFORMATION MANAGEMENT SYSTEM', font = ('Inria' , 20, 'bold' ), background='#CBDCF7', foreground='#568DE5' )
        
        title.pack(expand=True, fill= 'both', padx = 0, pady= 0) 
        frame1.place(relx=0.15, y=0, relwidth= 1, relheight= 0.05)
        
   
class widgets(ttk.TK_WIDGETS):
    def __init__(self):
         super().__init__()
         self.
        

Management('Transcript', '1540x700+0+0',(1540,700))
        
    