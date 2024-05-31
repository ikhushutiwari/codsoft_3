import random
from tkinter import * 

root = Tk()
root.title('Password Generator')
root.geometry('450x450')
root.resizable(False, False)
root.config(bg="beige")

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*_-+='

characters = alpha + numbers + symbols

label_characters = Label(root, text="Number of Characters:", bg="ivory", fg="Blue", font=('Ubuntu', 18))
label_characters.pack(padx=20, pady=15)

character_length = Entry(root, font="Arial 16", fg="Brown", justify='center')
character_length.pack(pady=15)

def generate_password():
    length = character_length.get()
    if length.isdigit():  # Check if the entered length is a number
        password = "".join(random.sample(characters, int(length)))
        label_password.config(text='Generated Password: ' + password)
    else:
        label_password.config(text='Please enter a valid number')

Button(root, text="Generate Password", command=generate_password, font=('Arial', 12)).pack(pady=15)

label_password = Label(root,  bg="#000080", fg="#FFFFE0", font=("Arial", 16), wraplength=400)
label_password.pack(padx=20, pady=15)

root.mainloop()
