from tkinter import *

# Creating a GUI Window
window = Tk()
window.title('Weight Converter')
window.geometry('1100x400')


def from_kg():

    gram = float(Label2_value.get())*1000
    pound = float(Label2_value.get())*2.20462
    ounce = float(Label2_value.get())*35.274
    milligram = float(Label2_value.get()) * 1000000

    Text1.delete("1.0",END)
    Text1.insert(END, gram)
    Text2.delete("1.0", END)
    Text2.insert(END, pound)
    Text3.delete("1.0", END)
    Text3.insert(END, ounce)
    Text4.delete("1.0", END)
    Text4.insert(END, milligram)

Label1 = Label(window, text="Input the weight in KG :", font=16)
Label2_value = StringVar()
Label2 = Entry(window, textvariable=Label2_value)
Label3 = Label(window, text="Gram", font=16)
Label4 = Label(window, text="Pound", font=16)
Label5 = Label(window, text="Ounce", font=16)
Label6 = Label(window, text="Milligram", font=16)

Text1 = Text(window, height=7, width=29, font=12)
Text2 = Text(window, height=7, width=29, font=12)
Text3 = Text(window, height=7, width=29, font=12)
Text4 = Text(window, height=7, width=29, font=12)

Button1 = Button(window, text="Convert", font=16, command=from_kg)

Label1.grid(row=0, column=0, pady=20)
Label2.grid(row=0, column=1, pady=20)
Label3.grid(row=1, column=0)
Label4.grid(row=1, column=1)
Label5.grid(row=1, column=2)
Label6.grid(row=1, column=3)
Text1.grid(row=2, column=0, padx=5, pady=20)
Text2.grid(row=2, column=1, padx=5, pady=20)
Text3.grid(row=2, column=2, padx=5, pady=20)
Text4.grid(row=2, column=3, padx=5, pady=20)
Button1.grid(row=0, column=2, pady=20)

window.mainloop()