#PROYECTO FINAL - JUNIO 9 2022
#Wilson Sebastian Martinez Reina, 73589
#nicolle galvis, 72973
#Sebastian Quintero, 73883
#UNIVERSIDAD DE SAN BUENAVENTURA

from filecmp import clear_cache
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from tkinter import *
from tkinter import filedialog
from busqueda_amp import busqueda_amp 
from busqueda_prof import busqueda_prof
import numpy as np


class interfaz_nemo_3(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("GUI_JUEGO_NEMO.ui", self)
        self.Boton_B_Amplitud.setEnabled(False)
        self.Boton_B_Profundidad.setEnabled(False)
        self.boton_buscar.clicked.connect(self.selecccionar_archivo)
        self.Boton_B_Amplitud.clicked.connect(self.busqueda_por_amplitud)
        self.Boton_B_Profundidad.clicked.connect(self.busqueda_por_profundidad)
        self.archivo_amplitud = self.barra_ruta_txt
        self.archivo_profundidad = self.barra_ruta_txt

    def selecccionar_archivo(self):
        # funcion para selecccionar el archivo archivo
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "archivo de texto (*.txt),(*.TXT)", options=options)
        if fileName:

            self.barra_ruta_txt.setText(fileName)
            print(self.barra_ruta_txt)
            self.archivo_amplitud = np.loadtxt(fileName, skiprows=0)
            self.archivo_profundidad = np.loadtxt(fileName, skiprows=0)
            self.Boton_B_Amplitud.setEnabled(True)
            self.Boton_B_Profundidad.setEnabled(True)
            # return fileName
    
    def busqueda_por_amplitud(self):
        jueguito = self.archivo_amplitud
        print(jueguito.copy())
        busqueda_amp.busqueda_amplitud(jueguito.copy())
    
    def busqueda_por_profundidad(self):
        jueguitos = self.archivo_profundidad
        print(jueguitos)
        busqueda_prof.busqueda_profundidad(jueguitos.copy())
        
        
        
    #     return 0
    #     buscar = juego.busqueda_por_Profundidad()
    #     return buscar

if __name__ == "__main__":
    app = QApplication(sys.argv)          # iniciar aplicacion
    GUI = interfaz_nemo_3()               # cargar archivos ui, ventana de arranque
    GUI.show()                            # muestra la ventana
    app.exec_()  # ejecuta la app hasta que se cierra
    
