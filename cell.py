from tkinter import *
from tkinter import messagebox
import random
import sys
import os
import time

class Cell:
    all = []
    cell_count = None
    cells_left = 36
    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.button = None
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        Cell.all.append(self)
        
    def create_button(self, location):
        self.location = location
        btn = Button(location, width = 10, height= 5)
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-2>', self.right_click)
        self.button = btn
        
    @staticmethod    
    def display_cell_count(location):
        label = Label(location, text = f"\n\n   CELLS\n  LEFT : {Cell.cells_left}", bg='black', font=("Times New Roman",30), fg = "white")
        Cell.cell_count = label
        
        
    def left_click(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_surrounding_cells()
            self.show_cell()
            if Cell.cells_left == 5:
                response = messagebox.showinfo("Game Over!", "CONGRATULATIONS! You won the game!")
            
        self.button.unbind('<Button-1>')
        self.button.unbind('<Button-2>')
            
    def show_surrounding_cells(self):
        if self.surrounding_mines_length == 0:
            if not self.is_opened:
                for cell in self.surrounded_cells:
                    self.show_cell()
                    cell.show_surrounding_cells()
        self.show_cell()
            
    def get_cell(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell(self.x-1, self.y-1), 
            self.get_cell(self.x-1, self.y),
            self.get_cell(self.x, self.y-1),
            self.get_cell(self.x+1, self.y+1),
            self.get_cell(self.x+1, self.y),
            self.get_cell(self.x, self.y+1),
            self.get_cell(self.x-1, self.y+1),
            self.get_cell(self.x+1, self.y-1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounding_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter
            
    def show_cell(self):
        if not self.is_opened:
            Cell.cells_left -= 1
            self.button.grid_forget()
            btn = Button(self.location, text=f"{self.surrounding_mines_length}", width = 10, height= 5, bg="red")
            btn.grid(row = self.x, column = self.y)
            if Cell.cell_count:
                Cell.cell_count.configure(text = f"\n\n   CELLS\n  LEFT : {Cell.cells_left}")
        self.is_opened = True
            
    def show_mine(self):
        """
        self.button.grid_forget()
        btn = Button(self.location, text="💣", width = 10, height= 5 ,state=DISABLED)
        btn.grid(row = self.x, column = self.y)
        Cell.show_mines()
        """
        self.button.configure(text="💣", state = DISABLED)
        Cell.show_mines()
        response = messagebox.askretrycancel("Game Over!", "You clicked on a mine.")
        if response==1:
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        else:
            sys.exit()
        #self.button.configure(bg="red")
    
    @staticmethod
    def show_mines():
        for cell in Cell.all:
            if cell.is_mine:
                cell.button.configure(text = "💣", state=DISABLED)

    def right_click(self, event):
        if not self.is_mine_candidate:
            self.is_mine_candidate = True
            self.button.configure(text = "❌", fg="red")
        else:
            self.button.configure(text = "")
            self.is_mine_candidate = False
        
    @staticmethod
    def randomize_mines():
        mines = random.sample(Cell.all, 5)
        for mine in mines:
            mine.is_mine = True
    
    def __repr__(self):
        return f"({self.x},{self.y})"