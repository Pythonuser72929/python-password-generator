import random as rd
def contraseña():
   lettersmax = "QWERTYUIOPASDFGHJKLÑZXCVBNM"
   lettersmin = "qwertyuiopasdfghjklñzxcvbnm"
   numbers = "123456789"
   print(rd.choice(lettersmax),rd.choice(lettersmax),rd.choice(lettersmin),rd.choice(numbers),rd.choice(numbers),rd.choice(numbers))
   loop = str(input("cargar otra contraseña?  no/si: "))
   if loop == "si" or loop == "yes":
   	contraseña()
   else:
   	print("fin del programa")
contraseña()   		