import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import random
import secrets
from tkinter import messagebox
def generate():
  global numbers
  start = textb1.get()
  end = textb2.get()
  try:
    start = int(start)
    end = int(end)
  except ValueError:
        messagebox.showerror("Error", "Please enter numbers for start and end")
        return
  numbers = ','.join(str(secrets.randbelow(end-start+1) + start) for _ in range(end-start+1))


  try:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        with open(filename, 'w') as f:
            f.write(numbers)
        messagebox.showinfo("Success", "Numbers saved to {}".format(filename))
  except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.geometry("500x300")
window.title("Random number Gen")
window.config(bg="white")
label1=tk.Label(window,text="Enter a starting numner :")
label1.pack(pady=5)
validate_start = window.register(lambda s: s.isdigit())
textb1= tk.Entry(window,validate="key", validatecommand=(validate_start, '%S'))
textb1.pack()
label2=tk.Label(window,text="Enter a starting numner :")
label2.pack(pady=30)
validate_End = window.register(lambda s: s.isdigit())
textb2= tk.Entry(window,validate="key", validatecommand=(validate_End, '%S'))
textb2.pack()
buttomg = tk.Button(window,text="Generate",highlightbackground="blue",command=generate)
buttomg.pack(pady=10)

window =tk.mainloop()