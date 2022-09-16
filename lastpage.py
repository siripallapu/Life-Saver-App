from tkinter import *

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Booked")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_text(20, 30, anchor=W, font="Purisa",
            text="  Your appointment is successfully booked! ")
        canvas.create_text(20, 60, anchor=W, font="Purisa",
            text="       Thankyou for using Lifesaver app")
        canvas.create_text(20, 130, anchor=W, font="Purisa",
            text="__________SUCCESSFUL_________")
        canvas.create_text(20, 160, anchor=W, font="Purisa",
            text="")
        canvas.create_text(20, 190, anchor=W, font="Purisa",
            text="Please send your feedback to")
        canvas.create_text(20, 220, anchor=W, font="Purisa",
            text="lifesaver2020@gmail.com")
        canvas.create_text(20, 240, anchor=W, font="Purisa",
            text= "https://forms.gle/5TcxSX1AzTNDw1ff7")
        canvas.pack(fill=BOTH, expand=1)


def main():

    root = Tk()
    ex = Example()
    root.geometry("420x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()


from openpyxl import *
from tkinter import *
wb = load_workbook('C:\\Users\\USER\\Desktop\\lifesaver database.xlsx')
sheet = wb.active

hos= sheet.cell(row= 1, column=8).value

def hello():
    if hos== "hospital 1":
        import mysql_conection.py
        exec("C:\\Users\\USER\\Desktop\\siri\\computer_project_completed_files\\mysql_connection.py")

    elif hos== "hospital 2":
        import mysqlconnectiona.py
        exec("C:\\Users\\USER\\Desktop\\siri\\computer_project_completed_files\\mysqlconnectiona.py")
        
    elif hos== "hospital 3":
        import mysqlconnectionb.py
        exec("C:\\Users\\USER\\Desktop\\siri\\computer_project_completed_files\\mysqlconnectionb.py")

hello()        
    

