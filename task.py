#Program to setup a company's employee account details
import random
import string

 #Employees data containers
user_data = []
names = ()

 #Individual details
str1 = input("Enter your firstname: ")
str2 = input("Your lastname, please: ")
email = input("Your email also: ")
names = str1[:2]+str2[-2:]

 #Defining the password function
def random_password():
    char = string.ascii_letters
    stringLength = 5
    randon_source = ''.join(random.choice(char) for i in range (stringLength))
    random_password = names + randon_source

    return random_password


 #List class for storing all information
while (True):
    user_data.append({
    "firstname": str1,
    "lastname": str2,
    "email": email,
    "password": random_password
     })

    print (f"{str1}, this password has been generated for you: {random_password} ")
    cont = input("Are you okay with it? (Y/N) ")
    if cont == "Y":
        break

    else:
        new_password = input("Enter your choice password: ")

        def new_password():
            if len(new_password) >= 7:
                random_password.clear
                random_password += new_password
                return new_password


            return "Password must be greater than or equal to 7"

print(f"Here are your details")
print(user_data)
