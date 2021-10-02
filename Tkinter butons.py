def mathsmarks():
    print(40)
def sciencemarks():
    print(50)    
def englishmarks():
    print(60)
def hindimarks():
    print(70)
from tkinter import *
root=Tk()
root.title("MARKS")
frame=Frame(root,borderwidth=5,bg="black")
frame.pack(side=LEFT,anchor="nw",fill="x")
b1=Button(frame,text="MATHS MARKS",command=mathsmarks)
b1.pack(side=LEFT)
b2=Button(frame,text="SCIENCE MARKS",command=sciencemarks)
b2.pack(side=LEFT)
b3=Button(frame,text="ENGLISH MARKS",command=englishmarks)
b3.pack(side=LEFT)
b4=Button(frame,text="HINDI MARKS",command=hindimarks)
b4.pack(side=LEFT)
root.mainloop()
