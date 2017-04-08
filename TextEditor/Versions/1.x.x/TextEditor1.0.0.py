# -*- coding: utf-8 -*-

import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className=" Text Editor")
textPad = ScrolledText(root, width=100, height=80)

# create a menu & define functions for each menu item

def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
        
def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def about_command():
    label = tkMessageBox.showinfo("TextEditor", "Created By Dylan Richards \n \n \n V1.0.0")
        
def new_command():
    file = tkFileDialog.asksaveasfile(mode='w')
        
def redbg():
    textPad.config(bg="red")
    
def greenbg():
    textPad.config(bg="green")
    
def bluebg():
    textPad.config(bg="blue") 
    
def yellowbg():
    textPad.config(bg="yellow") 
    
def orangebg():
    textPad.config(bg="orange")
    
def pinkbg():
    textPad.config(bg="pink")  
    
def saveclose(event):
    if tkMessageBox.askokcancel("Save File and Quit", "Do you want to save and quit?"):
        data = textPad.get('1.0', END+'-1c')
        file = tkFileDialog.asksaveasfile(mode='w')
        file.write(data)
        file.close()
        root.destroy()  
        
def choosecolor():
    colorselector = Tk(className=" Select a colour")
    colorselector.geometry("{}x{}".format(200, 400))
    normal = Label(colorselector, text="Standard Colours:")
    normal.grid(row=0, column=0)
    red = Label(colorselector, text="Red")
    red.grid(row=1, column=0)
    redB = Button(colorselector, text="Select", command=redbg)
    redB.grid(row=1, column=1)
    green = Label(colorselector, text="Green")
    green.grid(row=2, column=0)
    greenB = Button(colorselector, text="Select", command=greenbg)
    greenB.grid(row=2, column=1)
    blue = Label(colorselector, text="Blue")
    blue.grid(row=3, column=0)
    blueB = Button(colorselector, text="Select", command=bluebg)
    blueB.grid(row=3, column=1)
    yellow = Label(colorselector, text="Yellow")
    yellow.grid(row=4, column=0)
    yellowB = Button(colorselector, text="Select", command=yellowbg)
    yellowB.grid(row=4, column=1)
    orange = Label(colorselector, text="Orange")
    orange.grid(row=5, column=0)
    orangeB = Button(colorselector, text="Select", command=orangebg)
    orangeB.grid(row=5, column=1)
    pink = Label(colorselector, text="Pink")
    pink.grid(row=6, column=0)
    pinkB = Button(colorselector, text="Select", command=pinkbg)
    pinkB.grid(row=6, column=1)
    
    rgblabel = Label(colorselector, text="RGB Colour:")
    rgblabel.grid(row=7, column=0)
    
    
    rgb = "#%02x%02x%02x" % (255, 255, 255)
    #Function to get RGB value
    def updateValue(self):
        global rgb
        red2 = r_scale.get()
        green2 = g_scale.get()
        blue2 = b_scale.get()
        rgb = "#%02x%02x%02x" % (red2, green2, blue2)
        textPad.configure(bg = rgb)
    
    #Color labels
    red = Label (colorselector, text='R', font='Calibri', fg='red')
    green = Label (colorselector, text='G', font='Calibri', fg='green')
    blue = Label (colorselector, text='B', font='Calibri', fg='blue')

    #scale colors
    r_scale = Scale(colorselector, from_=0, to=255, length=300, sliderlength=60, orient=HORIZONTAL,command=updateValue)
    g_scale = Scale(colorselector, from_=0, to=255, length=300, sliderlength=60, orient=HORIZONTAL,command=updateValue)
    b_scale = Scale(colorselector, from_=0, to=255, length=300, sliderlength=60, orient=HORIZONTAL,command=updateValue)
    r_scale.set(255)
    g_scale.set(255)
    b_scale.set(255)
   
    #Position of labels and buttons
    red.grid (row=8, column=0, sticky=W)
    green.grid (row=9, column=0, sticky=W)
    blue.grid (row=10, column=0, sticky=W)

    r_scale.grid (row=8, column=1)
    g_scale.grid (row=9, column=1)
    b_scale.grid (row=10, column=1)

    #setwindow size
    colorselector.resizable(width=True, height=True)
    colorselector.minsize(width=500, height=350)
    
def wordcount():
    num_words = 0
    data = textPad.get('1.0', END+'-1c')
    tempwords = data.split(None)
    num_words += len(tempwords)
    tkMessageBox.showinfo("WordCount", "Total Words: " + str(num_words))

menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New…", command=new_command)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)

formatmenu = Menu(menu)
menu.add_cascade(label="Formatting", menu=formatmenu)
formatmenu.add_command(label="Background Color", command=choosecolor)
formatmenu.add_command(label="Word Count", command=wordcount)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

root.bind("<Control-w>", saveclose)


textPad.pack()
root.mainloop()
