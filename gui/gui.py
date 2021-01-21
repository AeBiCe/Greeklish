import os,sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
import GLdict as gl

root = tk.Tk()
root.title("Greeklish")
root.resizable(False, False) # Disable resize of program

subfolders  = False
directory   = ""
files       = ""

def set_dir(directory):
    global files
    os.chdir(directory) # Change to entry
    files = os.listdir(os.getcwd()) # Get files in directory


def clear_text(event):
    entry.delete(0,"end")
    translate_button.config(state="normal")
    return None

def set_entry(): # todo: error handling when entry isinvalid or empty
    global directory
    entry.config(state="normal")
    directory = filedialog.askdirectory()
    entry.delete(0,"end") # Clear entry field
    entry.insert(0,directory) # Show chosen directory
    set_dir(directory)
    entry.config(state="readonly")
    translate_button.config(state="normal")

def alert(title,text):
    messagebox.showinfo(title, text)

def set_subfolder():
    global subfolders
    if (var.get() == True):
        subfolders = True
    else:
        subfolders = False

def translate(file,subdir):
    try:
        os.rename((os.path.join(subdir,file)),os.path.join(subdir,gl.greeklish(file))) # Rename file
    except PermissionError: # Skips files with special permissions
        pass

def GLrename():
    global directory
    global files
    set_dir(entry.get())
    if subfolders:
        for subdir, dirs, sub_files in os.walk(directory):
            for file in sub_files:
                translate(file,subdir)

    else:
        for file in files:
            translate(file,"")
    alert("done","Translation complete!")


# GUI
entry = tk.Entry(root,bd=2,width=35)
entry.insert(0,"Enter directory...",)
entry.bind("<Button-1>", clear_text)
entry.grid(row=0,column=0,columnspan=3,padx=6,pady=6)

browse_button = tk.Button(root, text="Browse",command=lambda: set_entry())
browse_button.grid(row=1,column=0,pady=3)

translate_button = tk.Button(root, text="Translate",state="disabled",command=lambda: GLrename())
translate_button.grid(row=1,column=1,padx=0)

var = tk.BooleanVar()
check = tk.Checkbutton(root, text="Subfolders",variable=var,command=set_subfolder)
check.grid(row=1,column=2)



if __name__ == "__main__":
    root.mainloop()
