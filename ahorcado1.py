import time
nombre=input("¿COMO TE LLAMAS? ")
print("HOLA, "+nombre," JUGUEMOS ADIVINANDO EL NOMBRE DE UN ANIMAL")
print(" ")
time.sleep(1)
print("COMIENZA")
time.sleep(1)
palabra="murcielago"
tupalabra=" "
vidas=5

while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("*",end="")
            fallas+=1
    if fallas==0:
        input()
        print("")
        print("¡FELICITACIONES! GANASTE")
        input()
        break

    tuletra=input("PRUEBA UNA LETRA: ")
    tupalabra+=tuletra

    if tuletra not in palabra:
        vidas-=1
        print("¡NO! TE EQUIVOCASTE")
        print("AHORA TENES",+vidas," VIDAS")
    if vidas== 0:
        print("¡PERDISTE!")
else:
    input()
    print("GRACIAS POR PARTICIPAR")
    input()
