from tkinter import *

root = Tk()
root.wm_attributes('-transparentcolor', '#abcdef')
root.config(bg='#abcdef')
root.geometry('400x200+0+0')
label1 = Label(root, text="F9 Screenshot, ESC quit", fg="red", bg="black", font=("Times New Roman",18,"bold"), relief="solid")
label1.pack(side='left', anchor=NW)

root.overrideredirect(True)
root.wm_attributes("-topmost", 1)

root.mainloop()