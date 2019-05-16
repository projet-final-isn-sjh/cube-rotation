from math import cos,sin,sqrt,pi
import tkinter as tk


class cube():
    def __init__(self,r,lenght_jmp):
        self.coords=list()
        
        for i in range(lenght_jmp):
            t=pi/(2*lenght_jmp)*i
            self.coords.append(self.pc(r,t+3*pi/4)+self.pc(r,t+pi/4)+self.pc(r,t-pi/4)+self.pc(r,t-3*pi/4))
            
        self.cube=canvas.create_polygon(self.rotation(400,0),fill="red",outline="green",width=5)

    def pc(self,r,t):
        return int(r*cos(t)),int(r*sin(t))

    def rotation(self,y,m):
        l=[200,y]
        return [self.coords[m][i]+l[i%2] for i in range(len(self.coords[m]))]

    def __call__(self,y,m):
        canvas.coords(self.cube,self.rotation(y,m))

def append():
    global i
    a(400,i%20)
    i+=1
    root.after(13,append)

root=tk.Tk()
canvas=tk.Canvas(root,width=800,height=450)
canvas.pack()
a=cube(sqrt(2)*15,20)
i=0
append()
root.mainloop()
        
