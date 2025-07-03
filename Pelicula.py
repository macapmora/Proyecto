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
    genero = str 
    pais_origen = str
    estado = bool
    ARCHIVO = "datos_peliculas.npy"

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
        self.genero = ""
        self.pais_origen = ""
        self.estado = True
    
    # Este método pide los datos básicos de la pelicula 
    def pedir_datos(self):
        opcion = 0
        self.nombre_espannol = input("Ingrese el nombre en español de la pelicula: ")
        self.anno_estreno = int(input("Ingrese el año de estreno de la pelicula: "))
        self.duracion = int(input("Ingrese la duración de la pelicula en minutos: "))
        self.nombre_original = input("Ingrese el nombre original de la pelicula: ")

        while (opcion == 0):
            print("\nGéneros de Películas")
            print("1. Drama\n2. Suspenso\n3. Terror\n4. Acción\n5. Comedia\n6. Infantil")
            opcion = int(input("Ingrese el número del género de la película: "))
            match(opcion):
                case 1: 
                    print("\nIngreso el género 1. Drama.")
                    self.genero = "Drama"
                case 2:
                    print("Ingreso el género 2. Suspenso")
                    self.genero = "Suspenso"
                case 3:
                    print("Ingreso el género 3. Terror")
                    self.genero = "Terror"
                case 4:
                    print("Ingreso el género 4.Ación")
                    self.genero = "Acción"
                case 5:
                    print("Ingreso el género 5. Comedia")
                    self.genero = "Comedia"
                case 6:
                    print("Ingreso el género 6. Infantil")
                    self.genero = "Infantil"
                case _:
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")
        
        self.pais_origen = input("Ingrese el país de origen de la pelicula: ")
    # Este método muestra a los clientes los daatos basicos de la pelicula
    def mostrar_datos(self):
        print ("\n*** INFORMACIÓN PELICULAS ***\n")
        print(f"1. El nombre en español de la película es: {self.nombre_espannol}\n2. El año de estreno de la película es: {self.anno_estreno}")
        print(f"3. La duración en minutos es de: {self.duracion}\n4. El nombre original es: {self.nombre_original}")
        print(f"5. El genero es: {self.genero}\n6. El pais de origen es: {self.pais_origen}")
        input("\nPara volver al menu principal. Presione Enter...") 


