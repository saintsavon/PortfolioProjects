from random import *
char1="ABCDEFGHIJKLMNOPQRTUVWXYZ"
char2=char1.lower()
char3="!@#$%^&*()"
char4="0123456789"
def message():
    print("Welcome to your random password generator!")
    print("Please select the length of each of your characters")
    print(userGen())
def userGen():
    upper=int(input("Amount of upper case letters:"))
    lower=int(input("Amount of lower case letters:"))
    spec=int(input("Amount of special characters:"))
    num=int(input("Amount of numbers:"))
    return passGen(upper,lower,spec,num)
def passGen(upper,lower,spec,num):
    new_password=""
    if (upper+lower+spec+num)<6:
        print("Please enter minimum 6 letters.")
    else:
        for i in range(upper):
            new_password+=choice(char1)
        for x in range(lower):
            new_password+=choice(char2)
        for y in range(spec):
            new_password+=choice(char3)
        for z in range(num):
            new_password+=choice(char4)
    pass_word=list(new_password)
    shuff=shuffle(pass_word)
    new_pass="".join(pass_word)
    return new_pass
message()