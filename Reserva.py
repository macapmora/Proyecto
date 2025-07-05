import numpy as np
from Complejo import Complejo

class Reserva:
    """
    Funcionalidad de la clase: Esta clase nos permite realizar las reservas del complejo.
    Esta clase contiene los datos de la reserva, como el nombre del usuario, la fecha de la venta, el nombre del complejo, 
    el id de la sala, el nombre de la película, la hora de la función, el mapa de asientos, el número de asientos reservados y el precio total.
    Esta clase permite a los clientes realizar reservas de asientos para las funciones de cine, y a su vez a partir de esta clase se
    generan las boletas de cada reserva.
    Autora: Maria Camila Parra
    Fecha: 28/06/2025
    """
    # Atributos
    nombre_usuario = str
    id_usuario = int
    fecha_venta = str
    nombre_complejo = str
    id_sala = str
    nombre_pelicula = str
    hora_funcion = str
    mapa_asientos = np.ndarray
    numero_asientos = int
    precio_total = float

    def __init__(self):
        self.nombre_usuario = ""
        self.id_usuario = 0
        self.fecha_venta = ""
        self.nombre_complejo = ""
        self.id_sala = ""
        self.nombre_pelicula = ""
        self.hora_funcion = ""
        self.mapa_asientos = np.ndarray
        self.numero_asientos = 0
        self.precio_total = 0
    
    def pedir_datos(self):
        self.nombre_usuario = input("Ingrese el nombre del usuario: ")
        self.id_usuario = int(input("Ingrese el ID del usuario: "))
        self.fecha_venta = input("Ingrese la fecha de la venta en formato (DD/MM/AAAA): ")
        comple = Complejo()
        self.nombre_complejo = comple.nombre_complejo
        self.id_sala = input("Ingrese el ID de la sala: ")
        self.nombre_pelicula = input("Ingrese el nombre de la película: ")
        self.hora_funcion = input("Ingrese la hora de la función (HH:MM): ")
        self.precio_total = float(input("Ingrese el precio total de la reserva: "))

