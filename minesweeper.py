from tkinter import *
from cell import Cell
import os
import sys

root = Tk()
root.title("Minesweeper")
root.geometry("940x675")
root.resizable(False, False)
root.configure(bg="black")

top_frame = Frame(root, bg='black', width=1080, height= 120)
top_frame.place(x=0, y=0)
text = Label(top_frame, text = "MINESWEEPER", font=("Times New Roman",60),fg="white",bg="black")
text.place(x=250,y=20)

left_frame = Frame(root, bg = 'black', width = 180, height = 600)
left_frame.place(x=0,y=120)

center_frame = Frame(root, bg = 'black', width = 900, height = 600)
center_frame.place(x=180, y=120)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

for i in range(6):
    for j in range(6):
        c = Cell(x=i, y=j)
        c.create_button(center_frame)
        c.button.grid(row = i, column = j)
        
Cell.display_cell_count(left_frame)
Cell.cell_count.grid(row= 0, column= 0)

mine_count = Label(left_frame,text = f"\n\n  💣 : 5\n\n\n\n\n\n", bg='black', font=("Times New Roman",30), fg = "white")
mine_count.grid(row=2,column=0)

restart_button = Button(left_frame, text = "Restart", bg="black",padx=10,pady=8,command=restart)
restart_button.grid(row=4,column=0)

exit_button = Button(left_frame, text = "Exit ", bg="black",padx=19,pady=8,command=root.quit)
exit_button.grid(row=6,column=0)

Cell.randomize_mines()

root.mainloop()