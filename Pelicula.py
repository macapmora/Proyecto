class Pelicula:
    """
    Funcionalidad de la clase: Esta clase representa una película disponible en el sistema.
    Esta clase contiene los detalles generales de cada pelicula, les permite a los clientes consultar esta información y a los administradores
    les permite agregar esta información y modificarla.También sirve para que los administradoresprogramen las películas en las salas.
    Autora: Manuela Jimenez Muñoz Y Maria Camila Parra
    Fecha: 28/05/2025
    """
    # Atributos
    nombre_espannol = str
    anno_estreno = int
    duracion = int
    nombre_original = str 
    genero = int 
    pais_origen = str
    estado = bool
    ARCHIVO = "datos_pelicula.npy"

    # Constantes de la clase
    GEN_DRAMA = 1
    GEN_SUSPENSO = 2
    GEN_TERROR = 3
    GEN_ACCION = 4
    GEN_COMEDIA = 5
    GEN_INFANTIL = 6

    # Constructor de la clase
    def __init__(self):
        self.nombre_espannol = ""
        self.anno_estreno = 0
        self.duracion = 0
        self.nombre_original = ""
        self.genero = 0
        self.pais_origen = ""
        self.estado = True
    
    # Este método pide los datos básicos de la pelicula 
    def pedir_datos(self):

        flag = True

        self.nombre_espannol = input("Ingrese el nombre en español de la pelicula: ")
        self.anno_estreno = int(input("Ingrese el año de estreno de la pelicula: "))
        self.duracion = int(input("Ingrese la duración de la pelicula en minutos: "))
        self.nombre_original = input("Ingrese el nombre original de la pelicula: ")

        while(flag):

            self.genero = int(input("Ingrese el genero de la pelicula:\n1.Drama\n2.Suspenso\n3.Terror\n4.Acción\n5.Comedia\n6.Infantil\n"))

            if(self.genero > 6):

                print("El valor ingresado no es correcto, por favor ingrese otra opcion\n")
            else:
                flag = False

        self.pais_origen = input("Ingrese en pais de origen de la pelicula: ")
    
    # Este método muestra a los clientes los daatos basicos de la pelicula
    def mostrar_datos(self):
        opcion = 0

        while (opcion != 3):
            print ("\n*** INFORMACIÓN PELICULAS ***\n")
            print(f"1. El nombre en español de la película es: {self.nombre_espannol}\n2. El año de estreno de la película es: {self.anno_estreno}")
            print(f"3. La duración en minutos es de: {self.duracion}\n4. El nombre original es: {self.nombre_original}")
            print(f"5. El genero es: {self.genero}\n6. El pais de origen es: {self.pais_origen}")
            print(f"7. Volver al menu principal")
            opcion = int(input("Seleccione 7 si desea volver al menu anterior"))
            
            match(opcion):
                case 7:
                    input("\nIngresó a la opción 7. Volver al menu principal. Presione enter para continuar ...")
                case _:
                    input("\nIngresó una opción incorrecta. Presione enter para continuar ...")

