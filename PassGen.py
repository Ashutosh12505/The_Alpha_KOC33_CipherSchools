import random
import string

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digits=string.digits
sym=string.punctuation


symbol=list(sym)
symbol.remove("<")
symbol.remove(">")

spchar=''
for i in symbol:
    spchar+=i


string = upper + lower + digits + spchar

print("WELCOME TO THE PASSWORD GENERATOR:)")
pwlen = int(input("Enter your desired length of the password:"))

if pwlen < 12:
    print("Password should have atleast 12 characters:")
else:
    password = ''
    for i in range(pwlen):
     password += ''.join(random.choice(string))

    while True:
        password = ''
        for i in range(pwlen):
           password += ''.join(random.choice(string))

        if (sum(var in sym for var in password) >= 1):
            break 
    print("Here is your password:",password)
    print("Thank You!")