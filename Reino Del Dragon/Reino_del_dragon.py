from random import randrange

print("Escriba su nombre")
nom=input()
pts=0
x=""
while(x!="N"):
    pts=0
    print("Elija una cueva para entrar")
    t1=randrange(0,2)
    
    t2=randrange(0,2)
    
    t3=randrange(0,2)
    
    print("1-Izquierda, 2-Derecha")
    c=int(input())-1
    if c==t1:
        print("Encontraste un dragon amable, ahora tienes que elegir de nuevo")
        pts=pts+100
        c=int(input())-1
        if c==t2:
            pts=pts+100
            print("Encontraste un dragon amable, ahora tienes que elegir de nuevo")
            c=int(input())-1
            if c==t3:
                pts=pts+100
                print("Encontraste un dragon amable, Has ganado")
                print("Felicidades",nom,"Has obtenido",pts,"puntos")
                print("deseas continuar?")
                print("S o N?")
                x=input()
                if x=="N":
                    break
                else:
                    continue
            else:
                print("Encontraste un dragon hambriento, has sido devorado")
                print("Perdiste ",pts,"puntos acumulados")
                print("deseas continuar?")
                print("S o N?")
                x=input()
                if x=="N":
                    break
                else:
                    continue
        else:
            print("Encontraste un dragon hambriento, has sido devorado")
            print("Perdiste ",pts,"puntos acumulados")
            print("deseas continuar?")
            print("S o N?")
            x=input()
            if x=="N":
                break
            else:
                continue

    else:
        print("Encontraste un dragon hambriento, has sido devorado")
        print("Perdiste",pts,"puntos acumulados")
        print("deseas continuar?")
        print("S o N?")
        x=input()
        if x=="N":
            break
        else:
            continue
    