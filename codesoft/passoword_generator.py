import random
import string
import tkinter as t
from tkinter import messagebox
window = t.Tk()
window.title("Random Password Generator")
window.geometry("300x200")
window.configure(bg='peach puff')
def generate_password():
    try:
        length = int(entry.get())
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        label2.config(text=password)
    except ValueError:
        label2.config(text="Invalid length")

def copy_to_clipboard():
    password = label2.cget("text")
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        window.update()
        messagebox.showinfo("Copied", "Password has been copied to clipboard!")
label1 = t.Label(window, text="Enter password length:",bg='papaya whip')
label1.pack(pady=5)
entry = t.Entry(window, font=("Courier New", 16), bg='antique white',justify='center')
entry.pack(padx=20, ipady=1, pady=10, fill=t.BOTH)
entry.insert(0, "")
label2 = t.Label(window, text=" ", font=("Courier New", 16),bg='peach puff')
label2.pack(pady=5)
button1 = t.Button(window, text="Generate Password",bg='Skyblue1', command=generate_password)
button1.pack(pady=10)
button2 = t.Button(window, text="Copy to Clipboard",bg='skyblue1', command=copy_to_clipboard)
button2.pack(pady=5)
# Run the application
window.mainloop()