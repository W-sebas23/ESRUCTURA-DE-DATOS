#PROYECTO FINAL - JUNIO 9 2022
#Wilson Sebastian Martinez Reina, 73589
#nicolle galvis, 72973
#Sebastian Quintero, 73883


import numpy as np
from Nodo import Nodo
import turtle

class busqueda_prof():
    def __init__(self,juego):
        self.juego = np.array
    
    def busqueda_profundidad(juego):
        for i in range(0, juego.shape[0]):
            for j in range(0, juego.shape[1]):
                if juego[i, j] == 0:
                    pos_robot = (i, j)
                    juego[i, j] = 2  # Colocar la posición como un espacio libre
                    break  # Salga del for
        raiz = Nodo(
            juego,
            pos_robot,
            (False, False, False),
            [pos_robot],
            [pos_robot]
        )
        pila = [raiz]
        nodos_expandidos = 1
        nodos_creados = 1
        while True:
            nodo = pila.pop(-1)  # quito el primero elemento
            nodos_expandidos += 1
            # Condicion de ganar
            if nodo.verificar_ganar():
                print("nodos expandidos: ")
                print(nodos_expandidos)
                print("nodos creados: ")
                print(nodos_creados)
                ###########
                turtle.TurtleScreen._RUNNING=True
                Win = turtle.Screen()
                Win.bgcolor("#023F6B")
                Win.title("Mapa ejemplo")
                Win.setup(500,500)
                def __init__(forma,color):
                    elemento = turtle.Turtle()
                    elemento.shape(forma)
                    elemento.color(color)
                    elemento.penup()
                    elemento.speed(0.2)
                    return elemento
                
                roca = __init__('square','#C39EDA') 
                tortuga = __init__('square','#33F63B')
                tiburon =  __init__('square','#FF4769')
                nemo =  __init__('square','#F5935F')
                marlin = __init__('square','#F65C0A')
                dory = __init__('square', '#B527FF')
                humano = __init__('square','#F7C598')
                espacio = __init__('square','#98FFF3')
                robot = __init__('circle','#000000')
                
                ###########
                lista_de_cambios = nodo.recorrido.copy()
                Matriz =[] #lista de matrices con las cooredenadas
                Matriz0 = juego.copy() #se copia la matriz sin el robot
                Matriz.append(Matriz0) #se añade la visualizacion del mapa sin el robot
                len(lista_de_cambios)
                for j in range(len(lista_de_cambios)): #entra a la lista
                    #lista de cambios [j] represeta la coordenada que se cambia
                    if Matriz0[lista_de_cambios[j]] == 2 or Matriz0[lista_de_cambios[j]] == 7 or Matriz0[lista_de_cambios[j]] == 6 or Matriz0[lista_de_cambios[j]] == 5:
                        matriz_n = Matriz0.copy() #copia de la matriz sin el robot
                        matriz_n[lista_de_cambios[j]] = 0 #donde habia un espacio o pez se le asigan un espacio en la coordenada (x,y)
                        Matriz.append(matriz_n) #se añade la matriz modificada
                    #validaciones: si es un pez colocar un espacio libre cuando llega a esa coordenada  
                    if Matriz0[lista_de_cambios[j]] == 7:
                        Matriz0[lista_de_cambios[j]] = 2
                        Matriz.append(Matriz0) #se modifica a la matriz original para que el pez no vuelva a aparecer en el camino, no  se genera copiaa
                    if Matriz0[lista_de_cambios[j]] == 6:
                        Matriz0[lista_de_cambios[j]] = 2
                        Matriz.append(Matriz0)
                    if  Matriz0[lista_de_cambios[j]] == 5:
                        Matriz0[lista_de_cambios[j]] = 2
                        Matriz.append(Matriz0)
                ###########
                for j in range(len(Matriz)):
                 for f in range(len(Matriz[j])):    
                    for k in range(len(Matriz[j][f])):     
                        elm_x = -150 + (k * 60)
                        elm_y = 150 - (f * 60)
                        
                        elemento = Matriz[j][f][k]
                        
                        if elemento == 1:
                            roca.goto(elm_x,elm_y)
                            roca.stamp()

                        if elemento == 4:
                            tortuga.goto(elm_x,elm_y)
                            tortuga.stamp()
                            
                        if elemento == 3:
                            tiburon.goto(elm_x,elm_y)
                            tiburon.stamp()
                        
                        if elemento == 7:
                            nemo.goto(elm_x,elm_y)
                            nemo.stamp()
                            
                        if elemento == 6:
                            marlin.goto(elm_x,elm_y)
                            marlin.stamp()
                            
                        if elemento== 8:
                            humano.goto(elm_x,elm_y)
                            humano.stamp()
                            
                        if elemento == 5:
                            dory.goto(elm_x,elm_y)
                            dory.stamp()
                        
                        if elemento == 2:
                            espacio.goto(elm_x,elm_y)
                            espacio.stamp()
                    
                        if elemento == 0:
                            robot.goto(elm_x,elm_y)
                            robot.stamp()
                        
                ###########
                turtle.TurtleScreen._RUNNING=False
                turtle.bye()
                print(nodo.recorrido)
                return nodo.recorrido

            hijos = nodo.generar_hijos()
            for h in hijos:
                if not(h.verificar_perdi()):  # Solo evaluo nodos en cuales no pierdo
                    pila.append(h)
                nodos_creados += 1
            # Condición de no encontrar
            if len(pila) == 0:
                print("nodos expandidos: ")
                print(nodos_expandidos)
                print("nodos creados: ")
                print(nodos_creados)
                return None
    