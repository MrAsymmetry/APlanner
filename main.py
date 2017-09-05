"""Main Window creation"""

from Tkinter import *

root = Tk()

root.title('Architect Planner 1.0')
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

app = Frame(root)
app.grid()

# Run loop
root.mainloop()
