from tkinter import *
# import tkinter 
top = Tk()
top.title("แอปของฉัน")
top.geometry("480x640")
lbl_name=Label(top,text="Name ::") # Label of main 
txt_name = Text(top,width=20,height=1)
txt_name.pack(side=LEFT)
lbl_name.pack(side=LEFT)
btn_cancel = Button(top,text="Cancel")
btn_cancel.pack(side=LEFT)
btn_ok = Button(top,text="OK")
btn_ok.pack(side=LEFT)
top.mainloop()