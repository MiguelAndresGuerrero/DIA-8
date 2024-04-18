#Bienvenida al usuario
name = input("Ingresa tu nombre ")
print("Bienvenido ",name)
chek = input("Ingresa el saldo de tu tarjeta ")

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

    #planes de susucricion que se le mostrataran al usuario
    if Suscripcion1:
        print("Esta suscripcion tiene un valor de 20 USD ")
        TiempoActiva = input("Cuanto tiempo quieres mantener tu suscripcion activa: ")
    TiempoActiva=Suscripcion1*TiempoActiva

    #Si el usuario desea regalar una suscripcion
if OP==2:
    name2 = input("A quien desea regalar la cuenta, por favor ingresa el nombre: ")
    input("Cuanto tiempo deseas regalarle la suscripcion ",TiempoActiva)
    chek=chek-TiempoActiva
    print("tu amigo",name2), print("Activo su suscripcion gracias a ",name)

    #Si el usuario desea verificar el saldo que le queda en la tarjeta
if OP==3:
    chek=chek-TiempoActiva
    print("chek")

print("Gracias por comprar la suscripcion ", name)

#creado por Miguel Guerrero C.C 1090381839