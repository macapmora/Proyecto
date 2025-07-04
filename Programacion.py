import numpy as np
from SalaCine import SalaCine
from Pelicula import Pelicula
from datetime import datetime

class Programacion:
    peliculas = np.ndarray
    horario = np.ndarray
    filas = int
    columnas = int
    mapa_sala = np.ndarray
    cont_peliculas = int
    ARCHIVO = "datos_programacion.npy"

    MAX_PELICULAS = 5

    def __init__(self):
        self.peliculas = np.full(self.MAX_PELICULAS, fill_value= None, dtype= object)
        self.cont_peliculas = 0
        self.horario = np.full(self.MAX_PELICULAS, fill_value= None, dtype= datetime)
        self.filas = self.sala.filas
        self.columnas = self.sala.sillas_fila
        self.mapa_sala = np.full((self.filas, self.columnas), fill_value= 0, dtype=int)

    def pedir_datos(self):
        if self.cont_peliculas < self.MAX_PELICULAS:
            peli = Pelicula()
            peli.pedir_datos()
            self.peliculas[self.cont_peliculas] = peli
            if self.peliculas[self.cont_peliculas].estado:
                self.horario[self.cont_peliculas] = datetime(input("Ingrese el horario asignado para la pelicula: "))
            else:
                print("La pelicula se encuentra inactiva, por lo cual no se le puede asignar un horario")
        else:
            print("La programacion de la sala ya tiene su maximo de peliculas.")

    def disponibilidad(self):
        peli_escogida = str
        i = int
        i = 0

        peli_escogida = input("Ingrese el nombre de la pelicula de la cual desea ver su programacion: ")

        for i in range(0,self.MAX_PELICULAS):
            if peli_escogida == self.peliculas[i].nombre_espannol:
                print(f"Los horarios de la pelicula {self.peliculas[i].nombre_espannol} son:\n{self.horario[i]}")

    def reservar_asientos(self):
        i = int
        j = int
        i = 0
        j = 0
        fila_reservada = int
        silla_reservada = int

        self.mapa_sala = np.zeros((self.filas, self.columnas), dtype=int)
        print ("El mapa de la sala es el siguiente (los asientos revserados se ven con 1 y los disponibles con 0): ")
        print(self.mapa_sala)

        fila_reservada = int(input("Ingrese la fila en la que desea reservar asiento: "))
        silla_reservada = int(input("Ingrese la silla que desea reservar"))

        self.mapa_sala[fila_reservada, silla_reservada] = 1
