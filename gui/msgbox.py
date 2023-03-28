from tkinter import * 
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
#function messgebox Show messgebox
def show_messgebox():
    messagebox.showinfo("Hello World !!")
    #root.destroy()
btn_show=Button(root,text="Show Messgebox",command=show_messgebox)
btn_show.pack(side=LEFT)
root.mainloop()