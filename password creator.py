import random as rd
def password():
   lettersmax = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
   lettersmin = "qwertyuiopasdfghjklñzxcvbnm"
   numbers = "123456789"
   print(rd.choice(lettersmax),rd.choice(lettersmax),rd.choice(lettersmin),rd.choice(numbers),rd.choice(numbers),rd.choice(numbers))
   loop = str(input("load another password?  no/yes: "))
   if loop == "yes":
   	password()
   else:
   	print("end")
password()   		
