import math

#Implementación algoritmo
def GuessGame(n,k,inf,sup):
    if sup<inf:
        return 0
    max=sup
    min=inf
    cont=min
    p=math.floor((sup-inf)/(n+1))
    for i in range(0,n):
        cont=cont+p
        if(cont==k):
            return cont
        elif(cont>k and cont<max):
            max=cont
        elif(cont<k and cont>min):
            min=cont
        #end for
    return GuessGame(n,k,min,max)

#Implementación de la interfaz jugable
def GuessGamePlay(n,inf,sup,turno):
    turno+=1
    print("Turno: "+str(turno))
    if sup<inf:
        return 0
    max=sup
    min=inf
    cont=min
    p=math.floor((sup-inf)/(n+1))
    for i in range(0,n):
        cont=cont+p
        opcion=input("El número que pensó es: "+str(cont)+"? (si/no): ")
        if(opcion=="si"):
            return cont
            print("Gracias por jugar!\n")
            print("Número de turnos: "+str(turno))
        else:
            opcion2=input("El número que pensó es mayor que: "+str(cont)+"? (si/no): ")
            if(opcion2=="no" and cont<max):
                max=cont
            elif(opcion2=="si" and cont>min):
                min=cont
            #end for
    print("inf, sup: " + str(min) + " " + str(max))
    return GuessGamePlay(n,min,max, turno)



#Ejecución del algoritmo
print("Bienvenido al juego de adivinanzas. Por favor piense en un número natural entre 1 y 1000!\n")
n=int(input("Ingrese el numero de oportunidades que tendrá el adivinador por turno: "))
GuessGamePlay(n,1,1000, 0)