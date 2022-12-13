def hola(nom,num):
   print("hola mundo",nom,num)
hola ("luisa",1)

def tiempo(horas,min,seg):
    dato=(horas*3600)+(min*60)+(seg)
    print ("resultado", dato)
tiempo(3,10,40)

def frase(palabra,n):
    palabra=(palabra*n)
    print (palabra)
frase("hola ",3)

segundo =(2000360)
def segundo1 (segundo):
    hora1=(segundo/3600)
    minuto1=(segundo/60)
    print("las horas son: ",hora1)
    print("los minutos son: ",minuto1)
segundo1(segundo)


def parimpar(n1,n2):
    cont= 0
    for i in range (n1,n2):
        if (i%2==0):
             cont=cont + 1
    print("numero par ", i)
    print ("los numeros pares entre ", n1,"y",n2, "total:", cont)
parimpar(7,20)


def domino(na,nx):
    print("fichas del domino")
    for i in range (na,nx):
        for j in range (0,i+1):
            print("/"+ str(i)+"/"+str(j),end="\n")
domino(0,7)




    



