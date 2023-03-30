import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Transcritp information")
        self.window.geometry("1140x700")
        
        self.detail_frame = tk.Frame(
            self.window,
            bg='#CBDCF7',
            relief=ttk.GROOVE
        )
        self.detail_frame.place(width=260, height=700)
        
        
        


if __name__ == "__main__":
    root = tk.Tk()
    obj = Management(root)
    root.mainloop()
        
    