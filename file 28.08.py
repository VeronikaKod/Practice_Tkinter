# вес / (рост ** 2)

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Индекс массы тела")
window.geometry('400x400')

result=0
ves = 0
rost = 0
def calk():
    global result, ves, rost
    ves = int(vvod.get())
    rost = float(vvod1.get()) / 100
    result = ves / (rost ** 2)
    text3["text"] = f"Ваш ИМТ = {float(result)}"
    if result < 18.5:
        messagebox.showinfo("Внимание", "У Вас недостаточно массы тела")
    elif result >= 18.5 and result <= 24.9:
        messagebox.showinfo("Внимание","У Вас нормальный вес")
    elif result >= 25.0 and result <= 29.9:
        messagebox.showinfo("Внимание","У Вас избыточная масса тела")
    elif result >= 30.0 and result <= 34.9:
        messagebox.showinfo("Внимание","У Вас ожирение I степени")
    elif result >= 35.0 and result <= 39.9:
        messagebox.showinfo("Внимание","У Вас ожирение II степени")
    elif result >= 40.0 :
        messagebox.showinfo("Внимание","У Вас ожирение III степени")






text0 = Label(window, text="Введите свои данные" )
text0.grid(row= 1,column=2)

text1 = Label(window, text="Введите вес" )
text1.grid(row= 2,column=1)

vvod=Entry(window)
vvod.grid(row = 2, column = 2)

text2 = Label(window, text="Введите рост" )
text2.grid(row= 3, column=1)

vvod1=Entry(window)
vvod1.grid(row = 3, column = 2)

but1 = Button(window, text = "Рассчитать", command=calk)
but1.grid(row=4, column=2)

text3 = Label(window, text="")
text3.grid(row= 5, column= 2)



window.mainloop()