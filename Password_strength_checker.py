#password strength checker program
import re

password=input("Enter your password:")
#password should be of 8 character
if len(password)<8:
     print("Your password is weak.")
     print("Password must contain at least 8 character length")
#password must contain one upper case letter
elif not re.search("[A-Z]",password):
     print("Your password is weak.")
     print("Password must contain one uppercase letter ")
#password must contain one digit
elif not re.search("[0-9]",password):
     print("Your password is weak.")
     print("Password must contain one digit")
#password must contain one special character
elif not re.search("[^A-Za-z0-9]",password):
     print("Your password is weak.")
     print("Password must contain one special character ")
else:
     print("your Password is strong")