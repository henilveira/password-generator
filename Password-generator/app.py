import random
import  tkinter

class PasswordGenerator(): 
    def __init__(self, amount, length):
        self.amount = amount
        self.length = length

    def generate_password(self):
        symb = "!@#$%&*(){}[]^_-?/><*"
        num = "1234567890"
        lower_letter = "qwertyuiopasdfghjklzxcvbnm"
        upper_letter = "QWERTYUIOPASDFGHJKLZXCVBNM"

        string = symb + num + lower_letter + upper_letter

        passwords = []
        for _ in range(self.amount):
            password = "".join(random.sample(string, self.length))
            passwords.append(password)

        return passwords

amount = int(input("Quantas senhas deseja gerar?: "))
length = int(input("Quantos caracteres deseja na sua senha?: "))

generator = PasswordGenerator(amount, length)
passwords = generator.generate_password()

for password in passwords:
    print(password)


