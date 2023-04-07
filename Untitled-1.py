import random


lengeth = int(input(  "choose your pasword lengeth:  "))
caps = input ("choose if you want caps.      y / n  :")

numbers = input ("choose if you want numbers.      y / n  :")

alphabet = ("qwertyuiopasdfghjklzxcvbnm")

allnumbers = ("1234567890")

alphabet_caps = ("QWERTYUIOPASDFGHJKLZXCVBNM")


passwordwithcaps = ''.join(random.sample(alphabet + alphabet_caps , lengeth))


password = ''.join(random.sample(alphabet, lengeth))

passwordwithnumbers = ''.join(random.sample(alphabet + allnumbers, lengeth))

passwordwithcapsandnumbers = ''.join(random.sample(alphabet + alphabet_caps + allnumbers , lengeth))




if caps == "y" and numbers == ("y"):
    print ("your password is:",passwordwithcapsandnumbers)

if caps == "y" and numbers == ("f"):
    print ("your password is:",passwordwithcaps)

if numbers == "y" and caps == ("n"):
    print ("your password is:",passwordwithnumbers)

if caps == "n" and numbers == "n":
    print ("your password is:",password)


