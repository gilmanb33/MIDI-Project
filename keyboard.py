from Tkinter import *

root = Tk()

def key(event):
	received_character = event.char
	#print received_character	
	v.set(received_character)
	#print "pressed", repr(event.char)
	

def mouse_click(event):
	frame.focus_set()
	print "clicked at", event.x, event.y
	

frame = Frame(root, width=500, height=300)
frame.bind("<Key>", key)
frame.bind("<Button-1>", mouse_click)
frame.pack()

v = StringVar()
key_label = Label(root,textvariable=v,font = ("Helvetica",200))
key_label.pack();


root.mainloop()
