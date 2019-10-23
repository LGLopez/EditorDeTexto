import tkinter as tk
from tkinter.simpledialog import askstring

def highlight():
    var = askstring("Text Highlighter", "format: x.x-x.x")
    a,b = var.split("-")
    aText.tag_add("bt", a, b)

txt = "First line of text \nSecond line of text \nThird line of text"

lord = tk.Tk()

aText = tk.Text(lord, font=("Georgia", "12"))
aText.grid()

aText.insert(tk.INSERT, txt)

aButton = tk.Button(lord, text="highlight", command=highlight)
aButton.grid()

aText.tag_config("bt", background="yellow")

lord.mainloop()