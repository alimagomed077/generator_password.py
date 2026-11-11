import random
import string

def generator_password(lenght):
    characters = str(string.ascii_letters + string.digits)
    password = "".join(random.choices(characters, k=lenght))
    return password

user_length = int(input("Какой длины пароль"))

my_password = generator_password(user_length)

print("Ваш новый пароль:", my_password)

    