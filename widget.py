from tkinter import *
root = Tk()
root.title("entry widget")
root.iconbitmap("C:\\users\\simran\\Downloads\\logo1.png")
root.geometry("400x400")
def  number():

    try:
        int(my_box.get())
        answer.config(text="That is a number")
    except ValueError:
        answer.config(text="not a number")

my_label = Label(root, text="enter a number")
my_label.pack(pady=20)
my_box = Entry(root)
my_box.pack(pady=10)
my_button = Button(root, text="enter a number", command= number)
my_button.pack(pady=5)
answer = Label(root, text='')
answer.pack(pady=20)
root.mainloop()






