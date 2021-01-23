import numpy as np

k = 3
x = 1
o = 2

def hayEmpate(matriz):
    hayEmpate = False
    for i in range (k):
        if(np.all(matriz[: , :] !=0)):
            hayEmpate = True
            return hayEmpate
 
def hayGanadorHoriz(matriz):
    ganoX = False
    ganoO = False
    for i in range (k):
        if (np.all(matriz[i]==x)):
            ganoX = True
        elif (np.all(matriz[i]==o)):
            ganoO = True
    return  (ganoO, ganoX)
    
def hayGanadorVert(matriz):
    ganoX = False
    ganoO = False
    for j in range (k):
        if np.all(matriz[: , j]==x):
                ganoX = True
        elif np.all(matriz[: , j]==o):  
                ganoO = True
    return (ganoO, ganoX)
    
def hayGanadorDiag1(matriz):
    ganoX = False
    ganoO = False
    vec = []
    for i in range(k):
        for j in range(k):
            if (i == j):
                vec.append(matriz[i,j])
    if np.all(np.array(vec) == x):
        ganoX = True
    elif np.all(np.array(vec) == o):
        ganoO = True
    return (ganoO, ganoX)            
                
def hayGanadorDiag2(matriz):
    ganoX = False
    ganoO = False
    vec = []
    for i in range (k):
        for j in range (k):
            if (i == (k-1)-j):
                vec.append(matriz[i,j])
    if np.all(np.array(vec) == x):
        ganoX = True
    elif np.all(np.array(vec) == o):
        ganoO = True
    return (ganoO, ganoX)

def validarJugada():
    condicion = False 
    print("Realice su jugada segun lo indicado")
    coordenada = input()
      
    while(condicion == False):
        if (int(coordenada[0])>0 and int(coordenada[0])<4) and (int(coordenada[2])>0 and int(coordenada[2])<4) and (len(coordenada)== 3):
            condicion = True
            return (coordenada, condicion)
        else: 
            condicion = False
            print("Error, valor numerico ingresado incorrecto")
            coordenada = input()
            
def marcarTablero(matriz,coordenada,turno,codigo,codigoMat):
    movPosible = False
    if matriz [int(coordenada[0])-1][int(coordenada[2])-1] == 0:
        marca = codigoMat[coordenada]
        movPosible = True
        if turno == "x":
            matriz [int(coordenada[0])-1][int (coordenada[2])-1] = x
            codigo[marca] = "X"
        elif turno == "o": 
            matriz [int(coordenada[0])-1][int (coordenada[2])-1] = o
            codigo[marca] = "o"         
    return (codigo, matriz, movPosible)        
    

def mostrarTablero(codigo):
    
    print (("|"+codigo[1]+"|" + "|"+codigo[2]+"|" + "|"+codigo[3]+"|").center(100, " "))
    print (("|"+codigo[4]+"|" + "|"+codigo[5]+"|" + "|"+codigo[6]+"|").center(100, " "))
    print (("|"+codigo[7]+"|" + "|"+codigo[8]+"|" + "|"+codigo[9]+"|").center(100, " "))


cadena = "Bienvenido al Ta-Te-Ti-Virtual"
print (cadena.center(100, "="))
print ("\nLas X juegan primero. Cada jugador en su turno debe ingresar la coordenada donde marcara su jugada\ncon un valor de fila y luego de columna separados por una , (ambos valores van del 1 al 3).")
print ("A modo de ejemplo la casilla central debería indicarse como el valor 2,2\n")
print ("Que comience el juego!")

codigoMat = {'1,1': 1, '1,2': 2, '1,3': 3,
             '2,1': 4, '2,2': 5, '2,3': 6 ,
             '3,1': 7, '3,2': 8, '3,3': 9}
             
codigo = {1 : '_', 2 : '_', 3 : '_', 4 : '_', 5 : '_',
         6 : '_', 7 : '_', 8 : '_', 9 : '_'}
mostrarTablero(codigo)
contador = 0
turno = ""
matrix = [[0,0,0],[0,0,0],[0,0,0]]
matriz = np.array(matrix)
hayGanador = False

while hayGanador == False:
    if (contador % 2 == 0 ):
        turno = "x"
    else:
        turno = "o"
    print("Turno de jugador " + turno)
    movPosible=False
    while (movPosible == False):
        coordenada, condicion = validarJugada()
        codigo,matriz,movPosible = marcarTablero(matriz,coordenada,turno,codigo,codigoMat)
        print("Casillero ya marcado, elija otro")
    
    contador = contador + 1
    mostrarTablero(codigo)  

    ganadorO,ganadorX = hayGanadorHoriz(matriz)
    if (ganadorX == True):
        hayGanador == True
        print("Felicidades, gano el jugador X")
        break
    elif (ganadorO == True):
        print("Felicidades, gano el jugador O")
        hayGanador == True
        break
    ganadorO,ganadorX = hayGanadorVert(matriz)
    if (ganadorX == True):
        hayGanador == True
        print("Felicidades, gano el jugador X")
        break
    elif (ganadorO == True):
        hayGanador == True
        print("Felicidades, gano el jugador O")    
        break
        
    ganadorO, ganadorX = hayGanadorDiag1(matriz)
    if (ganadorX == True):
        hayGanador == True            
        print("Felicidades, gano el jugador X")
        break
    elif (ganadorO == True):
        hayGanador == True
        print("Felicidades, gano el jugador O")   
        break

    ganadorO, ganadorX = hayGanadorDiag2(matriz)
    if (ganadorX == True):
        hayGanador == True
        print("Felicidades, gano el jugador X")
        break
    elif (ganadorO == True):
        hayGanador == True
        print("Felicidades, gano el jugador O") 
        break  
    empate = hayEmpate(matriz)
    if (empate == True):
        print("Juego empatado")
        break