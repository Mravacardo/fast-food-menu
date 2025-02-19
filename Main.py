from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Enter Answers")
window.geometry("600x700")
window.config(background="green")

e_mail = Label(window, text="E_mail").place(x=40,y=60)
user_password = Label(window, text="Password").place(x=40, y=120)
e_mail_input_area = Entry(window, width=30).place(x=110, y=60)
user_password_entry_area = Entry(window, show='.', width=30).place(x=110, y=120)

burger_name = Label(window, text="Enter the name of the burger you want and then enter the quantity into the box on the right.").place(x=20,y=180)
burger_name_input_area = Entry(window, width=30).place(x=40, y=220)
burger_amount_input_area = Entry(window, width=10).place(x=380, y=220)

drink_name = Label(window, text="Enter the name of the drink you want and then enter the quantity into the box on the right.").place(x=20,y=280)
drink_name_input_area = Entry(window, width=30).place(x=40, y=320)
drink_amount_input_area = Entry(window, width=10).place(x=380, y=320)

side_name = Label(window, text="Enter the name of the side you want and then enter the quantity into the box on the right.").place(x=20,y=380)
side_name_input_area = Entry(window, width=30).place(x=40, y=420)
side_amount_input_area = Entry(window, width=10).place(x=380, y=420)

submit_button = Button(window, text="Submit").place(x=240, y=480)

window.mainloop()
