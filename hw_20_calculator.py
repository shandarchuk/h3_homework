from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

bttn_list = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text = i, command = cmd, width = 10).grid(row = r, column = c)
    c += 1
    if c > 3:
        c = 0
        r += 1

calc_entry = Entry(root, width = 40)
calc_entry.grid(row = 0, column = 0, columnspan = 5)


def calc(key):
    global memory
    if key == "=":
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

root.mainloop()