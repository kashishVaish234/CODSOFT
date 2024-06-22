import random
import string

def password_generate(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for _ in range(length))
    return password

password_length = int(input("enter the desired length of password: "))

generated_passsword = password_generate(password_length)

print("Your grnerated password: " + generated_passsword)