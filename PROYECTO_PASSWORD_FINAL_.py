#PROYECTO PASSWORD

#Requisitos de la contraseña
print("El password debe cumplir estos requisitos:")
print("1. El password ha de tenir una longitud entre 6 i 8 caracters")
print("2. Un numero major o igual a 1 o menor o igual a 5.")
print("3. una lletra minuscula")
print("4. Una lletra mayuscula")
print("5. Un dels següents símbols: * _ @ ")
print("6. una lletra minuscula")
print("7. Un numero major o igual a 6 i menor o igual que 9")
print("8. Un dels següents simbols: &, /, #")
print("9. un numero menos o igual que 5")


#Introducir password
password = input("Introduce tu password: ")


#Comprobar si los requisitos estan correctamente.

if len(password) < 6 or len(password) > 8: 
    print(f"Error, el password tiene una longitud de {len(password)} caracteres.")
else:
    if len(password) >= 1:
        if not password[0].isdigit() or not (1 >= int(password[0]) <= 5):
            print("Error en el requisito 1: debe ser un número major o igual a 1 o menor o igual a 5.")
    if len(password) >= 2:
        if not password[1].islower():
            print("Error en el requisito 2: debe ser una letra minúscula.")
    if len(password) >= 3:    
        if not password[2].isupper():
            print("Error en el requisito 3: debe ser una letra mayúscula.")
    if len(password) >= 4:    
        if password[3] not in '*_@':
            print("Error en el requisito 4: debe ser uno de estos símbolos: * _ @.")
    if len(password) >= 5:   
        if not password[4].islower():
            print("Error en el requisito 5: debe ser una letra minúscula.")
    if len(password) >= 6:    
        if not password[5].isdigit() or not (6 <= int(password[5]) <= 9):
            print("Error en el requisito 6: debe ser un numero major o igual a 6 i menor o igual que 9.")
    if len(password) >= 7:
        if password[6] not in '&/#':
            print("Error en el requisito 7: debe ser uno de estos símbolos: & / #.") 
    if len(password) == 8:
        if not password[7].isdigit() or not (int(password[7]) <= 5):
            print("Error en el requisito 8: debe ser un numero menor o igual que 5.")   
    else: 
        print("El formato del password es correcto. ")

        
