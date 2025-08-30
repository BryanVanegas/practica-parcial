print("Hola Bienvenido a los saludos.com") #cambié este texto
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}")
apellido = input("Ingrese su apellido:")
print(f"hola, {nombre} {apellido}")
print((nombre + " ")* 4 + " - " + (apellido + " " )* 3) #cambie los números
len_nom = len(nombre)
len_apell = len(apellido)


nombre_completo = nombre + " " + apellido
print(f"Su nombre completo es: {nombre_completo}")


print(f"tu nombre tiene {len_nom} letras y tu apellido tiene {len_apell} letras")
print(f"tu primera letra de tu apellido es: {apellido[0]} y la ultima es: {apellido[-1]}")
print(f"tu nombre en mayusculas es {nombre.upper()}")
print(f"tu apellido en mayusculas es: {apellido.upper()}")
print(f"tu nombre en minusculas es: {nombre.lower()}")
print(f"tu apellido en letras minusculas es: {apellido.lower()}")
print(f"Tu primera letra de tu nombre en mayuscula {nombre.title()}")
print(f"Tu primera letra de tu apellido en mayuscula es: {apellido.title()}")
print(f"tu nombre sin espacios es: {nombre.strip()}")
print(f"tu apellido sin espacios es: {apellido.strip()}")
print(f"tu nombre reemplazando la letra a por e es: {nombre.replace('a', 'e')}")
print(f"tu apellido reemplazando la letra a por e es: {apellido.replace('a', 'e')}")
print(f"tu primera letra de tu nombre es: {nombre[0]} y la ultima es: {apellido[-1]}")
