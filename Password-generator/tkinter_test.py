import tkinter as tk
from tkinter import messagebox

def login():
    length = length_entry.get() #Entrada de dados, basicamente input usando a função get
    amount = amount_entry.get()


    # For simplicity, let's assume valid username and password
    if length == 1 and amount == 1:
        messagebox.showinfo("Senha gerada com sucesso!")
    else:
        messagebox.showerror("Digite um número válido!")

# Create the main tkinter window
root = tk.Tk()
root.title("Gerador de senhas")

username_label = tk.Label(root, text="Caracteres:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Quantidade de senhas:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

login_button = tk.Button(root, text="Gerar!", command=login)
login_button.pack()

root.mainloop()
