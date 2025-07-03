import numpy as np 
from Usuario import Usuario 
from SalaCine import SalaCine
from Pelicula import Pelicula
from Programacion import Programacion 

class Complejo:
    """
    Funcionalidad de la clase:Esta es la clase principal del programa, en esta clase se registran los usuarios y se almacenan sus datos; además 
    se realiza el cambio de tipo de rol. En esta clase se conectan y ejecutan todas las demás.
    Autora: Maria Camila Parra
    Fecha: 28/05/2025
    """
    # Atributos
    nombre_complejo = str
    direccion_complejo = str
    usuario_auntenticado = Usuario
    usuarios = np.ndarray 
    cont_usuarios = int
    salascine = np.ndarray 
    cont_salas = int
    peliculas = np.ndarray
    cont_peliculas = int
    programaciona = np.ndarray
    cont_programacion = int

    # Constantes de la clase
    MAX_USUARIOS = 200
    MAX_SALASCINE = 12
    MAX_PELICULAS = 100
    MAX_PROGRAMACION = 5

    # Constructor de la clase
    def __init__(self):
        self.nombre_complejo = ""
        self.direccion_complejo = ""
        self.usuario_auntenticado = None 
        self.cont_usuarios = 3
        self.cont_salas = 0
        self.cont_peliculas = 0
        self.cont_programacion = 0

        # Crea el arreglo para almacenar los usuarios
        self.usuarios, self.cont_usuarios = self.cargar_datos(Usuario.ARCHIVO, self.MAX_USUARIOS)

        # Crea el arreglo para almacenar las salas de cine
        self.salascine, self.cont_salas = self.cargar_datos(SalaCine.ARCHIVO, self.MAX_SALASCINE)
        
        # Crea el arreglo para almacenar las películas
        self.peliculas, self.cont_peliculas= self.cargar_datos(Pelicula.ARCHIVO, self.MAX_PELICULAS)
        
        # Crea el arreglo para almacenar la programación
        self.programaciona, self.cont_programacion = self.cargar_datos(Programacion.ARCHIVO, self.MAX_PROGRAMACION)

        if (self.cont_usuarios == 0):
            self.usuarios[0] = Usuario(nombre="Camila", id=111, contrasenna="MCP")
            self.usuarios[0].cambiar_tipo(Usuario.PERFIL_ADMINISTRADOR)

            self.usuarios[1] = Usuario(nombre="Manuela", id=222, contrasenna="MJM")
            self.usuarios[1].cambiar_tipo(Usuario.PERFIL_VENDEDOR)

            self.usuarios[2] = Usuario(nombre="Alejandro", id=333, contrasenna="EAL")

            self.cont_usuarios = 3
    
    def cargar_datos(self, archivo, max_datos):
        try:
            arreglo_de_datos = np.load(archivo, allow_pickle=True)
            i = 0
            while arreglo_de_datos[i] != None:
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError):
            print(f"No se pudo cargar el archivo {archivo}. Se creará un arreglo de datos vacío!")
            arreglo_de_datos = np.full(max_datos, fill_value=None, dtype=object)
            return arreglo_de_datos, 0

    def guardar_datos(self, arreglo_de_datos, archivo):
        try:
            np.save(archivo, arreglo_de_datos)
            return True
        except (FileNotFoundError, EOFError):
            print(f"Error: No se pudieron almacenar los datos del archivo {archivo}.")
            return False

    # Este método pide los datos básicos del complejo
    def pedir_datos(self):
        
        print ("\n********************")
        print(" Datos del Complejo")
        print ("********************\n")
        """
        self.nombre_complejo = input("El nombre de el complejo es: ")
        self.direccion_complejo = input("La dirección del complejo es: ")
        """
    
    # Este método registra un usuario
    def registrar_usuario(self):
        print ("\n****************************************")
        print (" Registro de Usuario")
        print ("****************************************\n")
        user = Usuario()
        user.pedir_datos()

        # Almacena el usuario creado al arreglo y aumenta el contador de usuarios registrados en 1
        self.usuarios[self.cont_usuarios] = user
        self.cont_usuarios += 1

        if not self.guardar_datos(self.usuarios, Usuario.ARCHIVO):
            print("No se pudo guardar el archivo")
        else:
            print("Se actualizó el archivo")

    # Muestra el menu del administrador, tiene la misma base de funciones que el vendedor y el usuario
    # También puede agregar o eliminar salas, cambiar el estado de las peliculas y modificar la información de estas
    def mostrar_menu_admin(self):
        opcion = 0

        while (opcion != 9):
            print ("\n********************")
            print (" MENU DE ADMINISTRADOR")
            print ("********************\n")
            print("1. Registrar nuevo cliente\n2. Agregar Sala\n3. Consultar salas de cine\n4. Modificar programacion películas\n5. Consultar programación peliculas")
            print("6. Agregar pelicula\n7. Cambiar estado de una pelicula\n8. Consultar informacion películas\n9. Cerrar sesion")
            opcion = int(input("Seleccione una opción del menú: "))

            match(opcion):
                case 1:
                    input("\nIngresó a la opción 1. Registrar nuevo Cliente. Presione Enter para continuar ...")
                    print("\n*** Registro de Cliente Nuevo ***\n")
                    self.registrar_usuario()
                case 2:
                    input("\nIngresó a la opción 2. Agregar sala. Presione Enter para continuar ...")
                    print ("\n Registro de Sala \n")
                    salita = SalaCine()
                    salita.pedir_datos()

                    # Almacena la sala creada al arreglo y aumenta el contador de sala registrados en 1
                    self.salascine[self.cont_salas] = salita
                    self.cont_salas += 1
                    print ("\n ¡La sala ha sido agregada con éxito! \n")

                    if not self.guardar_datos(self.salascine, SalaCine.ARCHIVO):
                        print("No se pudo guardar el archivo")
                    else:
                        print("Se actualizó el archivo")

                case 3:
                    input("\nIngresó a la opción 3. Consultar salas de cine. Presione Enter para continuar ...")
                    print ("\n*** Listado de Salas ***\n")
                    if (self.cont_salas == 0):
                        print("No hay salas de cine registradas.")
                    else: 
                        for i in range(self.cont_salas):
                            salita = self.salascine[i]
                            print(f"\tSALA CINE #{i+1}\t")
                            salita.mostrar_datos()
                        input("Presione Enter para volver al menu anterior...")
                case 4:
                    input ("\nIngresó a la opción 4. Modificar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Modificación Programación Películas ***\n")
                    program = Programacion()
                    program.pedir_datos()

                    # Almacena la programación creada al arreglo y aumenta el contador de programación registrados en 1
                    self.programaciona[self.cont_programacion] = program
                    self.cont_programacion += 1
                    print ("\n ¡La programación ha sido agregada con éxito! \n")

                    if not self.guardar_datos(self.programaciona, Programacion.ARCHIVO):
                        print("No se pudo guardar el archivo")
                    else:
                        print("Se actualizó el archivo")
                case 5:
                    input("\nIngresó a la opción 5. Consultar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Programación Películas ***\n")
                    if (self.cont_programacion == 0):
                        print("No hay ninguna programación registrada.")
                    else:
                        print(self.programaciona)
                case 6:
                    input("\nIngresó a la opción 6. Agregar pelicula. Presione Enter para continuar ...")
                    print ("\n*** Registro de Película ***\n")
                    pelis = Pelicula()
                    pelis.pedir_datos()

                    # Almacena la película creada al arreglo y aumenta el contador de película registrados en 1
                    self.peliculas[self.cont_peliculas] = pelis
                    self.cont_peliculas += 1
                    print ("\n ¡La película ha sido agregada con éxito! \n")

                    if not self.guardar_datos(self.peliculas, Pelicula.ARCHIVO):
                        print("No se pudo guardar el archivo")
                    else:
                        print("Se actualizó el archivo")
                case 7:
                    input("\nIngresó la opción 7. Cambiar estado película. Presione Enter para continuar ...")
                    print ("\n Cambio de estado en una película \n")

                    if (self.cont_peliculas == 0):
                        print("No hay ninguna pelicula registrada")
                    else:
                        print("\n Listado de peliculas\n")
                        for i in range(self.cont_peliculas):
                            pelicula = self.peliculas[i]
                            estado = pelicula.estado 
                            if (estado):
                                estado = "Activa"
                            else: 
                                estado = "Inactiva"
                            print(f"{i+1}. {pelicula.nombre_espannol} ({estado})")
                    
                        indice = int(input("Ingrese el número de la película para cambiar su estado: "))
                        pelicula = self.peliculas[indice-1]
                        if (pelicula.estado):
                            pelicula.estado = False
                        else:
                            pelicula.estado = True 
                        
                        if not self.guardar_datos(self.peliculas, Pelicula.ARCHIVO):
                            print("No se pudo guardar el archivo")
                        else:
                            print("\nEl estado de la película se actualizo exitosamente")
                case 8:
                    input("\nIngresó a la opción 8. Consultar información películas. Presione Enter para continuar ...")
                    print ("\n*** Información Películas ***\n")
                    if (self.cont_peliculas == 0):
                        print("No hay ninguna película registrada.")
                    else: 
                        for i in range(self.cont_peliculas):
                            pelicula = self.peliculas[i]
                            estado = pelicula.estado
                            if (estado):
                                estado = "Activa"
                            else: 
                                estado = "Inactiva"
                            print(f"{i+1}. {pelicula.nombre_espannol} ({estado})")
                        
                        indice = int(input("Ingrese el número de la película de la cual desea consultar información: "))
                        pelicula = self.peliculas[indice-1]
                        pelicula.mostrar_datos()
                case 9:
                    self.usuario_auntenticado= None
                case _: 
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")

    # Muestra el menu del Vendedor, sus funcionalidades son iguales a las del cliente y ademas puede registrar nuevos clientes
    def mostrar_menu_vendedor(self):
        opcion = 0

        while (opcion != 5):
            print ("\n********************")
            print (" MENU DE VENDEDOR")
            print ("********************\n")
            print("1. Registrar nuevo cliente\n2. Consultar salas de cine")
            print("3. Consultar programacion peliculas\n4. Consultar informacion peliculas\n5. Cerrar sesion")
            opcion = int(input("Seleccione una opción del menú: "))

            match(opcion):
                case 1:
                    input("\nIngresó a la opción 1. Registrar nuevo Cliente. Presione Enter para continuar ...")
                    print("\n*** Registro de Cliente Nuevo ***\n")
                    self.registrar_usuario()
                case 2:
                    input("\nIngresó a la opción 2. Consultar salas de cine. Presione Enter para continuar ...")
                    print ("\n*** Listado de Salas ***\n")
                    if (self.cont_salas == 0):
                        print("No hay salas de cine registradas.")
                    else: 
                        for i in range(self.cont_salas):
                            salita = self.salascine[i]
                            print(f"\tSALA CINE #{i+1}\t")
                            salita.mostrar_datos()
                        input("Presione Enter para volver al menu anterior...")
                case 3:
                    input("\nIngresó a la opción 3. Consultar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Programación Películas ***\n")
                    if (self.cont_programacion == 0):
                        print("No hay ninguna programación registrada.")
                case 4:
                    input("\nIngresó a la opción 4. Consultar información películas. Presione Enter para continuar ...")
                    print ("\n*** Información Películas ***\n")
                    if (self.cont_peliculas == 0):
                        print("No hay ninguna película registrada.")
                    else: 
                        for i in range(self.cont_peliculas):
                            pelicula = self.peliculas[i]
                            print(f"{i+1}. {pelicula.nombre_espannol}")
                        
                        indice = int(input("Ingrese el número de la película de la cual desea consultar información: "))
                        pelicula = self.peliculas[indice-1]
                        pelicula.mostrar_datos()
                case 5:
                    self.usuario_auntenticado= None
                case _:
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")

    # Muestra el menu del Cliente en base a sus funcionalidades
    def mostrar_menu_cliente(self):
        opcion = 0

        while (opcion != 5):
            print ("\n********************")
            print (" MENU DE CLIENTE")
            print ("********************\n")
            print("1. Consultar salas de cine\n2. Consultar programacion peliculas")
            print("3. Consultar informacion peliculas\n4. Realizar una reserva\n5.Cerrar sesion")
            opcion = int(input("Seleccione una opción del menú: "))

            match(opcion):
                case 1:
                    input("\nIngresó a la opción 1. Consultar salas de cine. Presione Enter para continuar ...")
                    print ("\n*** Listado de Salas ***\n")
                    if (self.cont_salas == 0):
                        print("No hay salas de cine registradas.")
                    else: 
                        for i in range(self.cont_salas):
                            salita = self.salascine[i]
                            print(f"\tSALA CINE #{i+1}\t")
                            salita.mostrar_datos()
                        input("Presione Enter para volver al menu anterior...")
                case 2:
                    input("\nIngresó a la opción 2. Consultar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Programación Películas ***\n")
                    if (self.cont_programacion == 0):
                        print("No hay ninguna programación registrada.")
                case 3:
                    input("\nIngresó a la opción 3. Consultar información películas. Presione Enter para continuar ...")
                    print ("\n*** Información Películas ***\n")
                    if (self.cont_peliculas == 0):
                        print("No hay ninguna película registrada.")
                    else: 
                        for i in range(self.cont_peliculas):
                            pelicula = self.peliculas[i]
                            print(f"{i+1}. {pelicula.nombre_espannol}")
                        
                        indice = int(input("Ingrese el número de la película de la cual desea consultar información: "))
                        pelicula = self.peliculas[indice-1]
                        pelicula.mostrar_datos()
                case 4:
                    input("\nIngresó a la opción 4. Realizar una reserva. Presione Enter para continuar ...")
                    print ("\n*** RESERVA ***\n")
                case 5:
                    self.usuario_auntenticado= None
                case _:
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")

    # Este método permite autenticar a un usuario y ademas retorna True si se pudo autenticar el usaurio, False en caso contrario
    def autenticar_usuario(self):

        # Se piden los datos de autenticación
        print ("\n****************************************")
        print (" Autenticación de Usuarios")
        print ("****************************************\n")

        while True:
            try:
                id = int(input("Ingrese el número de documento del usuario: "))
                break
            except ValueError:
                print(
                    "\nError en la autenticación. Por favor ingrese un número de documento válido e intente nuevamente.\n")

        # Busca al usuario con el id ingresado en el arreglo de usuarios
        for i in range(self.cont_usuarios):
            if (self.usuarios[i].id == id):
                contrasenna = input("Ingrese la contraseña del usuario: ")
                # Si la contraseña coincide con la que ya fue almacenada, se actualiza el usuario autenticado y retorna True
                if (self.usuarios[i].contrasenna == contrasenna):
                    self.usuario_auntenticado = self.usuarios[i]
                    return True
                else:
                    # Si la contraseña no coincide se muestra un mensaje y se retorna False
                    input("\nError en la autenticación: Contraseña incorrecta. Presione Enter para continuar ...")
                    return False

        # Si no se cumple ninguno de los casos anteriores se muestra
        input(f"\nEl usuario con id {id} no se encuentra registrado en la base de datos. Por favor presione Enter y vuélvalo a intentar.")
        return False
    
    # Este el método es el que inicia la aplicación
    def menu_principal(self):
        opcion = 0

        while(opcion != 2):
            
            print ("\n****************************************")
            print(f"\tMenú Principal Complejo {self.nombre_complejo}")
            print ("****************************************\n")
            while True:
                try:
                    print("1. Autenticarse\n2. Salir de la app")
                    opcion = float(input("Seleccione una opción del menú: "))
                    break
                except:
                    print("\nError en la autenticación. Por favor inténtelo nuevamente.\n")

            match(opcion):

                case 1:
                    if (self.autenticar_usuario()):
                        if (self.usuario_auntenticado.tipo == Usuario.PERFIL_ADMINISTRADOR):
                            print()
                            self.mostrar_menu_admin()
                        elif (self.usuario_auntenticado.tipo == Usuario.PERFIL_VENDEDOR):
                            self.mostrar_menu_vendedor()
                        elif (self.usuario_auntenticado.tipo == Usuario.PERFIL_CLIENTE):
                            self.mostrar_menu_cliente()
                        else:
                            print("PERFIL NO RECONOCIDO")
                case 2:
                    self.usuario_auntenticado = None
                    print("\n Vuelva pronto. Aplicación terminada")
                case _:
                    print("\n Opción incorrecta. Inténtelo de nuevo")
    
obj = Complejo()
print("Bienvenido a ¿Que hay para ver?")
obj.pedir_datos()
obj.menu_principal()


