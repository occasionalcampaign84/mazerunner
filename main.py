from window import Window
from shapes import Line, Point
from cell import Cell
from maze import Maze

WINX, WINY = 800, 600
SIDE = 40

def cell_test(win):
    cells = [Cell(win), Cell(win)]
    cells[0].draw(Point(20,30), Point(120,130))
    cells[1].draw(Point(300,400), Point(400,500))
    cells[0].draw_move(cells[1])

def line_test():
    line = Line(Point(0,0),Point(WINX-1,WINY-1))
    win.draw_line(line,"green")
    win.draw_random_lines()

def maze_test(win):
    maze = Maze(x1=SIDE,y1=SIDE,
                num_rows=(WINY-2*SIDE)//SIDE,  #(600-2*40)/40 = 520/40 = 13
                num_cols=(WINX-2*SIDE)//SIDE,  #(800-2*40)/40 = 720/40 = 18
                cell_size_x=SIDE,cell_size_y=SIDE,win=win)
    maze.break_entrance_and_exit()
    maze.break_walls_r(0,0)
    maze.reset_cells_visited()
    maze.solve(0,0)

def main():
    win = Window(WINX,WINY)
    maze_test(win)
    win.wait_for_close()

main()



