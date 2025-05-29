from cell import Cell
from time import sleep
from shapes import Point
import random

class Maze():
    
    def __init__(self,x1,y1,num_rows,num_cols,
                cell_size_x,cell_size_y,win=None,
                 random_seed=3846):                         # strange incomplete maze with random seed = 2135
        self.x1 = x1                                        # before changing to offsets = self.directions.copy()
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        #walls_to_break = {(0,1):}
        
        if random_seed:
            random.seed(random_seed)
        self.create_cells()
        
    def create_cells(self):
        self.cells = [[Cell(self.win) for row in range(self.num_rows)] for col in range(self.num_cols)]
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.draw_cell(col,row)
        
    def draw_cell(self,col,row):
        cell = self.cells[col][row]
        top_left = Point(col*self.cell_size_x + self.x1, row*self.cell_size_y + self.y1)
        bottom_right = Point((col+1)*self.cell_size_x - 1 + self.x1, (row+1)*self.cell_size_y - 1 + self.y1)
        cell.draw(top_left,bottom_right)
        if self.win: self.animate()
        
    def animate(self):
        self.win.redraw()
        #sleep(.01)
        
    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        if not self.win: return
        self.draw_cell(0,0)
        self.draw_cell(self.num_cols-1, self.num_rows-1)
    
    def in_bounds(self, col, row):
        return all([0 <= col, col <= self.num_cols-1,
                    0 <= row, row <= self.num_rows-1])

    def break_walls_r(self, col, row):
        #sleep(.05)
        this_cell = self.cells[col][row]
        this_cell.visited = True
        offsets = self.directions.copy()
        random.shuffle(offsets)
        for offset in offsets:
            next_col = col + offset[0]
            next_row = row + offset[1]
            if not self.in_bounds(next_col, next_row):
                continue
            next_cell = self.cells[next_col][next_row]
            if next_cell.visited:
                continue
            
            if offset[0] == -1:  # left move
                this_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif offset[0] == 1: # right move
                this_cell.has_right_wall = False
                next_cell.has_left_wall = False                
            elif offset[1] == -1: # up move
                this_cell.has_top_wall = False
                next_cell.has_bottom_wall = False                
            elif offset[1] == 1: # down move
                this_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            else:
                raise Exception("soemthing went wrong in break_walls_r")
            self.draw_cell(col,row)
            self.draw_cell(next_col,next_row)
            self.break_walls_r(next_col,next_row)
    
    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False
                
    def solve(self,col,row):
        #x = [[cell.visited for cell in col] for col in self.cells]
        #for col in x:
        #    print(col)
        return self.solve_r(col,row)
    
    def solve_r(self,col,row):
        #sleep(.05)
        this_cell = self.cells[col][row]
        this_cell.visited = True
        offsets = self.directions.copy()
        random.shuffle(offsets)
        for offset in offsets:
            next_col = col + offset[0]
            next_row = row + offset[1]
            if not self.in_bounds(next_col, next_row):
                continue
            next_cell = self.cells[next_col][next_row]
            if next_cell.visited:
                continue

            if offset[0] == -1 and this_cell.has_left_wall:
                continue
            elif offset[0] == 1 and this_cell.has_right_wall:
                continue
            elif offset[1] == -1 and this_cell.has_top_wall:
                continue     
            elif offset[1] == 1 and this_cell.has_bottom_wall:
                continue

            this_cell.draw_move(next_cell, undo=False)
            self.win.redraw()
            if next_col == self.num_cols-1 and next_row == self.num_rows-1:
                return True
            if self.solve_r(next_col,next_row):
                return True
            this_cell.draw_move(next_cell, undo=True)
            self.win.redraw()
        return False
        