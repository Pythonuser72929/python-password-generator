import random as rd
def password():
   lettersmax = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
   lettersmin = "qwertyuiopasdfghjklñzxcvbnm"
   numbers = "123456789"
   print(rd.choice(lettersmax),rd.choice(lettersmax),rd.choice(lettersmin),rd.choice(numbers),rd.choice(numbers),rd.choice(numbers))
   loop = str(input("press enter (load another password): "))
   if loop == "":
   	password()
   else:
   	print("invalid comand only press enter(reestart and try again)")   	
password()   
