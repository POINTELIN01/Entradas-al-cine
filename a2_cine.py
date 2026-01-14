boleto = input("¿Tiene usted boleto? si/no ").lower()

if boleto == "si":
    print("Acceso permitido")
elif boleto == "no":
    print("Acceso denegado")
else:
    print("Respuesta no válida, por favor escriba si o no")