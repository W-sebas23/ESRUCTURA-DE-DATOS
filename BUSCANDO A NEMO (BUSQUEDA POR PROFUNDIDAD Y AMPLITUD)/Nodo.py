#PROYECTO FINAL - JUNIO 9 2022
#Wilson Sebastian Martinez Reina, 73589
#nicolle galvis, 72973
#Sebastian Quintero, 73883



class Nodo:
    def __init__(self,matriz,pos_robot,estado,recorrido,marcados):
        """
        matriz = Estado actual del juego
        pos_raton = posición actual del ratón x,y (enteros)
        estado = estado de los objetivos queso,pelota (booleanos)
        """
        self.matriz = matriz
        self.x = pos_robot[0]
        self.y = pos_robot[1]
        self.Nemo = estado[0]
        self.Marlin = estado[1]
        self.Dory = estado[2]
        self.recorrido = recorrido
        self.marcados = marcados


    def verificar_perdi(self):
        # tiburon=3, arpon=8, tortuga=4
        return self.matriz[self.x,self.y] == 3 or self.matriz[self.x,self.y] == 8 or self.matriz[self.x,self.y] == 4
               

    def verificar_ganar(self):
        return self.Dory== True and self.Marlin == True and self.Nemo == True #Verificar que encontré los dos objetivos

    def marcar_objetivos(self):
        #nemo = 7 , marlin = 6, Dory = 5
        if  not(self.Nemo) and self.matriz[self.x,self.y]==7:
            self.Nemo = True
            # self.Marlin = False
            # self.Dory = False
            self.marcados = [] #Al encontrar a nemo, puedo devolverme
        
        if self.matriz[self.x,self.y]==6 and self.Nemo:
            self.Marlin = True
            self.marcados =[] 
        
            
        if self.matriz[self.x,self.y]==5 and self.Nemo and self.Marlin:
            # self.Marlin = True
            # self.Nemo = True
            self.Dory= True
            self.marcados =[]


    def generar_hijos(self):
        #Hijos de arriba
        hijos = []
        x = self.x #-1  ?
        y = self.y-1
        
        if y >= 0 and not((x,y) in self.marcados) and self.matriz[x,y]!=1:
            
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y))
            
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.Nemo,self.Marlin,self.Dory),
                recorrido,   
                marcados   
            )
            hijo.marcar_objetivos()
            hijos.append(hijo) 
        
        #hijo abajo 
        x = self.x
        y = self.y+1
        
        if y < self.matriz.shape[0]  and not((x,y) in self.marcados) and self.matriz[x,y]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.Nemo,self.Marlin,self.Dory),
                recorrido,   
                marcados    
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)    
        
        #hijo izquierda
        
        x = self.x-1
        y = self.y
        
        if x >= 0 and not((x,y) in self.marcados) and self.matriz[x,y]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.Nemo,self.Marlin,self.Dory),
                recorrido,       
                marcados
            )
            hijo.marcar_objetivos()
            hijos.append(hijo)
        
        
        #hijo derecha
        x = self.x+1
        y = self.y
        
        if x < self.matriz.shape[1] and not((x,y) in self.marcados) and self.matriz[x,y]!=1: #Verificar que estoy en el tablero
            recorrido = self.recorrido.copy() #Garantizar que sea independiente
            recorrido.append((x,y)) #Agregar la posición actual
            marcados = self.marcados.copy() #Nodos ya visitados
            marcados.append((x,y)) 
            hijo = Nodo(
                self.matriz,
                (x,y),
                (self.Nemo,self.Marlin,self.Dory),
                recorrido,
                marcados

            )
            hijo.marcar_objetivos()
            hijos.append(hijo)
        
        return hijos        