from login import *
from recommendation import *
from update_points import *

print("Hello User")
var = input("Do you already have an account??yes/no: ")

#to create account
if var == 'no':
    create_account()

#to log in
if var == 'yes':
    user = login()
    
    if user is not None:
        recommend(user[0],user[1])

        mov = input("From the above which movie do you prefer to watch: ")
        update_points(mov,user[0],user[1])


