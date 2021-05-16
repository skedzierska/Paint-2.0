from tkinter import *
from random import choice
from tkinter.font import Font
from tkinter import ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image, ImageDraw
from PIL import ImageGrab

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.canvas.bind('<B1-Motion>',self.paint)

    def paint(self,e):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND)

        self.old_x = e.x
        self.old_y = e.y     

    def changeW(self,e): 
        self.penwidth = e

    def change_fg(self):
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.canvas['bg'] = self.color_bg
        
    def save(self):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics','*.png')])
        if file:
            x = self.master.winfo_rootx() + self.canvas.winfo_x()
            y = self.master.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()

            PIL.ImageGrab.grab().crop((x,y,x1,y1)).save(file + '.png')
            
    def drawWidgets(self):
        
        topFrame =  Frame(okno)
        topFrame.pack()
        s = Scale(okno, from_=0, to = 100, orient  = HORIZONTAL, command = self.changeW)
        s.pack()
        theLabel = Label(okno, text='grubosc linii').pack()
        przycisk1 = Button(topFrame, text = "zmiana koloru narzędzia",command=self.change_fg )
        przycisk1.pack(side = LEFT)
        przycisk3 = Button(topFrame, text = "narysuj koło")
        przycisk3.pack(side = LEFT)
        przycisk4 = Button(topFrame, text = "narysuj kwadrat")
        przycisk4.pack(side = LEFT)
        przycisk5 = Button(topFrame, text = "obrót o 90 stopni w lewo")
        przycisk5.pack(side = LEFT)
        przycisk6 = Button(topFrame, text = "obrót o 90 stopni w prawo")
        przycisk6.pack(side = LEFT)
        przycisk7 = Button(topFrame, text = "zapisz",command=self.save)
        przycisk7.pack(side = LEFT)
        przycisk8 = Button(topFrame, text = "zmiana koloru płótna",command=self.change_bg )
        przycisk8.pack(side = LEFT)
        
        self.canvas = Canvas(self.master,width=880,height=650,bg=self.color_bg,)
        self.canvas.pack()
        self.canvas.pack(expand=YES, fill=BOTH)


if __name__ == '__main__':
    okno = Tk()
    main(okno)
    okno.title('Paint 2.0')
    okno.mainloop()

