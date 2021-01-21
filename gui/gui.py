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

def clear_text(event):
    entry.delete(0,"end")
    return None

def set_dir(): # todo: error handling when entry isinvalid or empty
    global directory
    global files
    entry.config(state="normal")
    directory = filedialog.askdirectory()
    entry.delete(0,"end") # Clear entry field
    entry.insert(0,directory) # Show chosen directory
    os.chdir(directory) # Change to entry
    files = os.listdir(os.getcwd()) # Get files in directory
    entry.config(state="readonly")

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

browse_button = tk.Button(root, text="Browse",command=lambda: set_dir())
browse_button.grid(row=1,column=0,pady=3)

translate_button = tk.Button(root, text="Translate",command=lambda: GLrename())
translate_button.grid(row=1,column=1,padx=0)

var = tk.BooleanVar()
translate_button2 = tk.Checkbutton(root, text="Subfolders",variable=var,command=set_subfolder)
translate_button2.grid(row=1,column=2)


if __name__ == "__main__":
    root.mainloop()
