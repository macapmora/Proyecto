class SalaCine:
    """
    Funcionalidad de la clase: Esta clase representa una sala de cine dentro del complejo.
    Su función principal es organizar los datos de cada sala de cine, también la disposición física de los asientos
    y almacenar la programación de funciones de películas.
    Autora: Manuela Jimenez Muñoz
    Fecha: 28/05/2025
    """
    # Atributos
    id_sala = str
    valor_boleta = float
    filas = int
    sillas_fila = int
    programacion = object
    ARCHIVO = "datos_salacine.npy"

    # Constructor de la clase
    def __init__(self):
        self.id_sala = 0
        self.valor_boleta = 0
        self.filas = 0
        self.sillas_fila = 0
        self.programacion = Programacion()

    # Este método pide los datos básicos de la sala de cine
    def pedir_datos(self):
        self.id_sala = input("Ingrese en identificador de la sala: ")
        self.valor_boleta = float(input("Ingrese el valor de la boleta: "))
        self.filas = int(input("Ingrese el numero de filas: "))
        self.sillas_fila = int(input("Ingrese el numero de sillas por fila: "))

    # Este método muestra a los clientes los datos basicos de la sala de cine
    def mostrar_datos(self):
        print(f"""1. El ID de la sala es: {self.id_sala}\n2. El valor de la boleta es: {self.valor_boleta}
3. El número de filas de la sala es: {self.filas}\n4. El número de sillas por fila es: {self.sillas_fila}""")
        return ""