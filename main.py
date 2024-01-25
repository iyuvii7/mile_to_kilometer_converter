from tkinter import *

def button_click():
    text = int(entry.get())
    # Kilometers = Miles×1.60934
    km = round(text * 1.60934, 2)
    label3.config(text=f"{km}")


window = Tk()
window.title("Mile to km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)
#4 label 1 entry 1 button
entry = Entry(width=10)
entry.grid(column=1,row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1,row=1)

label4 = Label(text="Km")
label4.grid(column=2,row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1,row=2)

window.mainloop()