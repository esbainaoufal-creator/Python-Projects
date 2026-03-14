import random
import string
print("<------------ Welcome to Our Password generator ------------>")
print("<=====You insert a degit and we generate a goddamn password=====>")
def generator():    
    while True:
        word = string.ascii_letters + string.digits + string.punctuation
        length = int(input("Insert the length of the password>> "))
        letters = random.sample(word, length)
        password = "".join(letters)
        print(password)

generator()