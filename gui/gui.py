import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("Greeklish")
root.resizable(False, False) # Disable resize of program

def clear_text(event):
    entry.delete(0,"end")
    return None

def dirsec(): # todo: error handling when entry isinvalid or empty
    entry.config(state="normal")
    folder_selected = filedialog.askdirectory()
    entry.delete(0,"end") # Clear entry field
    entry.insert(0,folder_selected) # Show chosen directory
    entry.config(state="readonly")

def show_m():
    messagebox.showinfo("Done", "Translation complete!")

def subfolder_alert():
    if (var.get() == True):
        print('ticked')
    else:
        print('unticked')

entry = tk.Entry(root,bd=2,width=35)
entry.insert(0,"Enter directory...",)
entry.bind("<Button-1>", clear_text)
entry.grid(row=0,column=0,columnspan=3,padx=6,pady=6)

browse_button = tk.Button(root, text="Browse",command=dirsec)
browse_button.grid(row=1,column=0,pady=3)

translate_button = tk.Button(root, text="Translate",command=show_m)
translate_button.grid(row=1,column=1,padx=0)

var = tk.BooleanVar()
translate_button2 = tk.Checkbutton(root, text="Subfolders",variable=var,command=subfolder_alert)
translate_button2.grid(row=1,column=2)


if __name__ == "__main__":
    root.mainloop()
