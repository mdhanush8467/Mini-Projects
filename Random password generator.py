#import password generator
import random

randomechars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789!@#$%^&"
length=int(input("Enter the Number of Passwords to be Generated: "))
password=int(input("Enter the length of the Password needed: "))

# print("Here are your random passwords: ")
for x in range(length):
    pwd= ""
    for char in range(password):
        pwd = pwd+ random.choice(randomechars)                                                                                                                                                 
    print(pwd)
    