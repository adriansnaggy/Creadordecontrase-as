import random


codeall = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

largocntrsñ = int(input("escribe la longitud que quieras que sea tu contraseña: "))

contraseña_final = ""

for i in range(largocntrsñ):
    contraseña_final += random.choice(codeall)
    
    
print(f"tu contraseña ideal es: {contraseña_final}")
