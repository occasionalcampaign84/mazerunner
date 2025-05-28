from tkinter import Tk, BOTH, Canvas
from shapes import Line, Point
from random import randint

class Window:
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.root_widget = Tk()
        self.root_widget.title("This is not a title.")
        self.canvas_widget = Canvas(self.root_widget, bg="white", height=height, width=width)
        self.canvas_widget.pack(fill=BOTH,expand=1)
        self.window_is_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

        
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()
    
    def wait_for_close(self):
        self.window_is_running = True
        while self.window_is_running:
            self.redraw()
        #print("closing")
    
    def close(self):
        self.window_is_running = False
        self.root_widget.destroy()
        
    def draw_line(self, line, color):
        line.draw(self.canvas_widget, color)
        
    def draw_random_lines(self):
        while True:
            pts = [Point(randint(0,self.width-1),randint(0,self.height-1)) for i in range(2)]
            line = Line(pts[0],pts[1])
            colors = [randint(16,255) for i in range(3)]
            colors = [hex(color)[2:].upper() for color in colors]
            color = '#' + colors[0] + colors[1] + colors[2]
            line.draw(self.canvas_widget, color)
            self.redraw()
