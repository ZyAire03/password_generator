# password generator 

# importing library 
import random
import string
# Name 
print("Password Generator")

# length of the password 
len_passwords = int(input('Length of Passowrds:'))
# num_passwords =  4

# empty str and list
passwords = ''
final_passwords = []

# user to pick the type of password 
while True:
    passowrds_types = input('Pick the Characters for the Passwords (Letters, Numbers or Special Characters)! Type Done to stop:')
    
    if passowrds_types == 'Letters':
                passwords += string.ascii_letters
    elif passowrds_types == 'Numbers':
                passwords += string.digits
    elif passowrds_types == 'Special Characters':
                passwords += string.punctuation
    elif passowrds_types == 'Done':
            break
    else:
                print('Input is incorrect! Input the following')

# create function that will return the random choice passwords 
def generator ():
        for i in range(len_passwords): 
                random_passwords = random.choices(passwords)
                # print(random_passwords)
                final_passwords.append(random_passwords)
              

generator()
print('Your Passwords', final_passwords )