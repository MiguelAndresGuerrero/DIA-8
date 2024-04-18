#Bienvenida al usuario
name = input("Ingresa tu nombre ")
print("Bienvenido ",name)
chek = float(input("Ingresa el saldo de tu tarjeta "))

#Listas donde se guardan la membresia
Suscripcion1=[]

#menu interactivo del usuario
print("========================================================================")
print("                           MENU                                         ")
print("========================================================================")
print("""
"1. comprar suscripcion"
"2. regalar suscripcion "
"3. Verifivar saldo en la cuenta "
"selecciona una opcion usando los numeros(1,2,3)"
      """)
OP = int(input("Seleccione la opción: "))

#membresias que se les mostara al usuario
if OP==1:
    #susucricion que se le mostrataran al usuario
    print("Esta suscripcion tiene un valor de 60 USD por año")
    TiempoActiva = int(input("Cuánto tiempo quieres mantener tu suscripción activa: "))
    CostoTotal = 60 * TiempoActiva
     
    if chek >= CostoTotal:
        chek -= CostoTotal
        Suscripcion1.append(TiempoActiva)
        print(f"Has comprado la suscripcion por {TiempoActiva} Años")
        print(f"El costo total para mantener la suscripción activa por {TiempoActiva} meses es: {CostoTotal} USD")
    else:
       print("Fondos insuficientes en tu tarjeta")

    #Si el usuario desea regalar una suscripcion
elif OP==2:
    name2 = input("A quien desea regalar la cuenta, por favor ingresa el nombre: ")
    input("Cuanto tiempo deseas regalarle la suscripcion ")
    MembrasiaRegalada=int(input(f"Cuantos años desea regalarle la suscripcion a {name2}: "))
    
    #verificamos que el usuario si tenga fondos suficientes
    if chek >=MembrasiaRegalada*60:
        chek -=MembrasiaRegalada*60
        print("tu amigo",name2), print("Activo su suscripcion gracias a ",name)
    #Si el usuario desea verificar el saldo que le queda en la tarjeta
elif OP==3:
    print(f"El saldo actual de tu tarjeta es: {chek} USD")

#le agradecemos al usuario por comprar la suscripcion
print("Gracias por comprar la suscripcion ", name)

#creado por Miguel Guerrero C.C 1090381839