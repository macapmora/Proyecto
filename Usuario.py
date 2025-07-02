class Usuario:
    """
    Funcionalidad de la clase: Esta es la clase base para los diferentes tipos de usuarios del sistema (Cliente, Vendedor, Administrador).
    En esta se proporcionan atributos y métodos que sirven para el registro de nuevos usuarios.
    Autora: Maria Camila Parra
    Fecha: 31/05/2025
    """
    # Atributos
    id = int
    contrasenna = str
    nombre = str
    num_telefono = int
    correo = str
    tipo = int
    ARCHIVO = "datos_usuario.npy"

    # Constantes
    PERFIL_CLIENTE = 1
    PERFIL_VENDEDOR = 2
    PERFIL_ADMINISTRADOR = 3

    # Constructor de la clase: todos los usuarios inician como clientes
    def __init__(self, nombre = "", id = 0, contrasenna = "", num_telefono = 0, correo = ""):
        self.id = id
        self.contrasenna = contrasenna
        self.nombre = nombre
        self.num_telefono = num_telefono
        self.correo = correo 
        self.tipo = self.PERFIL_CLIENTE 

    # Este método pide los datos básicos del usuario
    def pedir_datos(self):
        self.id = int(input("Ingrese el ID del usuario (Número de documento): "))
        self.contrasenna = input("Ingrese la contraseña: ")
        self.nombre = input("Ingrese el nombre completo del usuario: ")
        self.num_telefono = int(input("Ingrese el número de telefono del usuario: "))
        self.correo = input("Ingrese el correo electronico del usuario: ")

    # Este metodo sirve para cambiar el tipo de usuario cliente a un vendedor o administrador
    def cambiar_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo 