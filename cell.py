from window import Window
from shapes import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = -1
        self.x2 = -1
        self.y1 = -1
        self.y2 = -1
        self.win = win
        self.visited = False
        
    def draw(self, pt1, pt2):
        if self.win: canvas = self.win.canvas_widget
        self.x1, self.y1 = pt1.x, pt1.y
        self.x2, self.y2 = pt2.x, pt2.y
        top_left, bottom_right = pt1, pt2
        top_right, bottom_left = Point(pt2.x,pt1.y), Point(pt1.x,pt2.y)
        if not self.win: return
        color = {True: "black", False: "white"}
        Line(top_left, bottom_left).draw(canvas, color[self.has_left_wall])
        Line(top_right, bottom_right).draw(canvas, color[self.has_right_wall])
        Line(top_left, top_right).draw(canvas, color[self.has_top_wall])
        Line(bottom_right, bottom_left).draw(canvas, color[self.has_bottom_wall])

    def draw_move(self, dest, undo=False):
        color = "gray" if undo else "red"
        Line(self.center(), dest.center()).draw(self.win.canvas_widget, color)
        
    def center(self):
        return Point((self.x1+self.x2)//2, (self.y1+self.y2)//2)
    