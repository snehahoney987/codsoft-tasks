import random
length=int(input("Enter the password length:"))

chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

password=""

for i in range(length):
    password +=random.choice(chars)
print("Password:",password)