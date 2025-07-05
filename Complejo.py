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

        if self.cont_usuarios == 0:
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
            while arreglo_de_datos[i] is not None:
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError):
            print(f"No se pudo cargar el archivo {archivo}. Se creará un arreglo de datos vacío!")
            arreglo_de_datos = np.full(max_datos, fill_value=None, dtype=object)
            return arreglo_de_datos, 0

    def guardar_datos(self, arreglo_de_datos, archivo):
        while True:
            try:
                print("\n¿Desea guardar los cambios realizados?")
                continua = int(input("Digite 1 para Sí, 0 para No: "))
            except ValueError:
                print("Opción inválida. Inténtelo nuevamente...")
            else:
                while True:
                    # noinspection PyUnreachableCode
                    match continua:
                        case 0:
                            print("Cambios no guardados.")
                            return False
                        case 1:
                            try:
                                np.save(archivo, arreglo_de_datos)
                                return True
                            except (FileNotFoundError, EOFError):
                                print(f"Error: No se pudieron almacenar los datos del archivo {archivo}.")
                                return False
                        case _:
                            print("Opción incorrecta. Por favor inténtelo nuevamente...")
                            break
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

        if self.guardar_datos(self.usuarios, Usuario.ARCHIVO):
            print(f"\n¡Información de Usuario actualizada exitosamente!")
        input("\nPresione Enter para volver al menú anterior...")

    def buscar_sala(self, id_buscar):
        """Recibe el ID de la sala a buscar y devuelve el ID si se encuentra en el arreglo de salas de cine.
        De lo contrario, devuelve None."""
        for i in range(self.cont_salas):
            sala = self.salascine[i]
            if sala.id_sala == id_buscar:
                return i
        return None

    def imprimir_listado(self, arreglo, objeto):
        for i in range(len(arreglo)):
            if arreglo[i] is None:
                break
            else:
                print(f"\t{objeto.title()} #{i+1}\t")
                print(f"{arreglo[i].mostrar_datos()}")

    def modificar_sala(self):
        print("*************************")
        print("\tMODIFICAR SALA CINE\t")
        print("*************************")
        while True:
            self.imprimir_listado(self.salascine, "Sala de Cine")
            id_modificar = input("Ingrese el ID de la sala a modificar o presione Enter para volver al menú principal: ")
            if id_modificar == "":
                return None
            sala_id = self.buscar_sala(id_modificar)
            if sala_id is None:
                print(f"\nNo se encontró la sala con el ID ingresado. Por favor inténtelo nuevamente...")
            else:
                sala = self.salascine[sala_id]
                while True:
                    print(f"\n\tDatos de la Sala: {sala.id_sala}\n")
                    print(sala.mostrar_datos())
                    datos_amodificar = input("Seleccione el número del dato que desea cambiar o presione Enter para volver al menú principal: ")
                    if datos_amodificar != "":
                        try:
                            datos_amodificar = int(datos_amodificar)
                        except ValueError:
                            print(f"\nError en la selección del menú. Por favor, vuelva a intentarlo...")
                        else:
                            while True:
                                match datos_amodificar:
                                    case 1:
                                        sala.nombre_sala = input("\nIngrese el nuevo nombre de la sala: ")
                                    case 2:
                                        while True:
                                            try:
                                                sala.valor_boleta = float(input("\nIngrese el nuevo valor de la boleta: "))
                                                break
                                            except ValueError:
                                                print("\nError en la asignación del valor de la voleta. Por favor, vuelva a intentarlo...")
                                    case 3:
                                        while True:
                                            try:
                                                sala.filas = int(input("\nIngrese el número de filas: "))
                                                break
                                            except ValueError:
                                                print("\nError en la asignación del número de filas. Por favor, vuelva a intentarlo...")
                                    case 4:
                                        while True:
                                            try:
                                                sala.sillas_fila = int(input("\nIngrese el número de sillas por filas: "))
                                                break
                                            except ValueError:
                                                print("\nError en la asignación del número de sillas por filas. Por favor, vuelva a intentarlo...")
                                    case _:
                                        print("\nOpción no válida. Vuelva a intentarlo...")
                                        break
                                self.salascine[sala_id] = sala
                                if self.guardar_datos(self.salascine, SalaCine.ARCHIVO):
                                    print(f"\n!Información de Sala {sala.id_sala} actualizada exitosamente!")
                                input("\nPresione Enter para volver al menú anterior...")
                                return None
                    else:
                        return None

    def consultar_info_peliculas(self):
        while True:
            print("\n*** Información Películas ***\n")
            for i in range(self.cont_peliculas):
                pelicula = self.peliculas[i]
                print(f"{i + 1}. {pelicula.nombre_espannol}")
            try:
                indice = int(input("\nIngrese el número de la película de la cual desea consultar información: "))
            except ValueError:
                print("\nError en la selección del menú. Por favor intente nuevamente...")
            else:
                while True:
                    try:
                        print("")
                        pelicula = self.peliculas[indice - 1]
                        pelicula.mostrar_datos()
                        return ""
                    except (AttributeError, IndexError):
                        print("Error en la selección del menú. Por favor intente nuevamente...")
                        break

    def cambiar_estado_pelicula(self):
        while True:
            print("\n Listado de peliculas\n")
            for i in range(self.cont_peliculas):
                pelicula = self.peliculas[i]
                estado = pelicula.estado
                if estado:
                    estado = "Activa"
                else:
                    estado = "Inactiva"
                print(f"{i + 1}. {pelicula.nombre_espannol} ({estado})")
            try:
                indice = int(input("Ingrese el número de la película para cambiar su estado: "))
            except ValueError:
                print("\nError en la selección del menú. Por favor inténtelo nuevamente...")
            else:
                while True:
                    try:
                        pelicula = self.peliculas[indice - 1]
                        if pelicula.estado:
                            pelicula.set_estado(False)
                        else:
                            pelicula.set_estado(True)
                    except (AttributeError, IndexError):
                        print("\nError en la selección del menú. Por favor inténtelo nuevamente...")
                        break
                    else:
                        return f"\nEstado actualizado: la película '{pelicula.nombre_espannol.title()}' ahora se encuentra '{pelicula.get_estado()}'."

    # Muestra el menu del administrador, tiene la misma base de funciones que el vendedor y el usuario
    # También puede agregar o eliminar salas, cambiar el estado de las peliculas y modificar la información de estas
    def mostrar_menu_admin(self):
        opcion = 0
        while opcion != 12:
            while True:
                print("\n************************")
                print(" MENU DE ADMINISTRADOR")
                print("************************\n")

                try:
                    print("1. Registrar nuevo cliente\n2. Agregar Sala\n3. Modificar datos de una sala\n4. Consultar salas de cine\n5. Agregar programación\n6. Modificar programacion películas\n7. Consultar programación películas\n8. Agregar película\n9. Modificar información de una película\n10. Cambiar estado de una películas\n11. Consultar informacion películas\n12. Cerrar sesión\n")
                    opcion = int(input("Seleccione una opción del menú: "))
                    break
                except ValueError:
                    print("\nError en la selección del menú. Por favor inténtelo nuevamente...\n")
            match opcion:
                case 1:
                    input("\nIngresó a la opción 1. Registrar nuevo Cliente. Presione Enter para continuar ...")
                    print("\n*** Registro de Cliente Nuevo ***\n")
                    self.registrar_usuario()
                case 2:
                    input("\nIngresó a la opción 2. Agregar sala. Presione Enter para continuar...")
                    print ("\n Registro de Sala \n")
                    salita = SalaCine()
                    salita.pedir_datos()

                    # Almacena la sala creada al arreglo y aumenta el contador de salas registradas en 1
                    self.salascine[self.cont_salas] = salita
                    self.cont_salas += 1
                    print ("\n ¡La sala ha sido agregada con éxito! \n")

                    if self.guardar_datos(self.salascine, SalaCine.ARCHIVO):
                        print(f"\n¡Información de Sala actualizada exitosamente!")
                    input("\nPresione Enter para volver al menú anterior...")
                case 3:
                    input("\nIngresó a la opción 3. Modificar sala. Presione Enter para continuar...")
                    if self.cont_salas == 0:
                        print("No hay salas de cine registradas.")
                    else:
                        if self.modificar_sala() is None:
                            self.mostrar_menu_admin()
                case 4:
                    input("\nIngresó a la opción 4. Consultar salas de cine. Presione Enter para continuar ...")
                    print ("\n*** Listado de Salas ***\n")
                    if self.cont_salas == 0:
                        print("No hay salas de cine registradas.")
                    else:
                        self.imprimir_listado(self.salascine, "Sala de Cine")
                        input("Presione Enter para volver al menú anterior...")
                case 5:
                    pass
                case 6:
                    input ("\nIngresó a la opción 6. Modificar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Modificación Programación Películas ***\n")
                    program = Programacion()
                    program.pedir_datos()

                    # Almacena la programación creada al arreglo y aumenta el contador de programaciones registradas en 1
                    self.programaciona[self.cont_programacion] = program
                    self.cont_programacion += 1
                    print ("\n ¡La programación ha sido agregada con éxito! \n")

                    if self.guardar_datos(self.programaciona, Programacion.ARCHIVO):
                        print(f"\n¡Información de Programación actualizada exitosamente!")
                    input("\nPresione Enter para volver al menú anterior...")
                case 7:
                    input("\nIngresó a la opción 7. Consultar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Programación Películas ***\n")
                    if self.cont_programacion == 0:
                        print("No hay ninguna programación registrada.")
                    else:
                        print("\n Listado de programaciones\n")
                        self.imprimir_listado(self.programaciona, "Programación")
                case 8:
                    input("\nIngresó a la opción 8. Agregar pelicula. Presione Enter para continuar ...")
                    print ("\n*** Registro de Película ***\n")
                    pelis = Pelicula()
                    pelis.pedir_datos()

                    # Almacena la película creada al arreglo y aumenta el contador de películas registradas en 1
                    self.peliculas[self.cont_peliculas] = pelis
                    self.cont_peliculas += 1

                    if self.guardar_datos(self.peliculas,Pelicula.ARCHIVO):
                        print ("\n¡La película ha sido agregada con éxito!")
                    input("\nPresione Enter para volver al menú anterior...")
                case 9:
                    pass
                case 10:
                    input("\nIngresó la opción 10. Cambiar estado película. Presione Enter para continuar ...")
                    print ("Cambio de estado en una película")

                    if self.cont_peliculas == 0:
                        print("No hay ninguna pelicula registrada")
                    else:
                        print(self.cambiar_estado_pelicula())
                        if self.guardar_datos(self.peliculas, Pelicula.ARCHIVO):
                            print(f"\n¡Información de Películas actualizada exitosamente!")
                        input("\nPresione Enter para volver al menú anterior...")
                case 11:
                    input("\nIngresó a la opción 11. Consultar información películas. Presione Enter para continuar ...")
                    print ("\n*** Información Películas ***\n")
                    if self.cont_peliculas == 0:
                        print("No hay ninguna película registrada.")
                    else:
                        self.consultar_info_peliculas()
                        input("\nPresione Enter para continuar y volver al menú principal...")
                case 12:
                    self.usuario_auntenticado = None
                case _: 
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")

    # Muestra el menu del Vendedor, sus funcionalidades son iguales a las del cliente y además puede registrar nuevos clientes
    def mostrar_menu_vendedor(self):
        opcion = 0

        while opcion != 5:
            while True:
                try:
                    print("\n********************")
                    print(" MENU DE VENDEDOR")
                    print("********************\n")
                    print("1. Registrar nuevo cliente\n2. Consultar salas de cine")
                    print("3. Consultar programacion peliculas\n4. Consultar informacion peliculas\n5. Cerrar sesion")
                    opcion = int(input("Seleccione una opción del menú: "))
                    break
                except ValueError:
                    print("\nError en la selección del menú. Por favor inténtelo nuevamente...\n")
            match opcion:
                case 1:
                    input("\nIngresó a la opción 1. Registrar nuevo Cliente. Presione Enter para continuar ...")
                    print("\n*** Registro de Cliente Nuevo ***\n")
                    self.registrar_usuario()
                case 2:
                    input("\nIngresó a la opción 2. Consultar salas de cine. Presione Enter para continuar ...")
                    print ("\n*** Listado de Salas ***\n")
                    if self.cont_salas == 0:
                        print("No hay salas de cine registradas.")
                    else: 
                        self.imprimir_listado(self.salascine, "Salas de Cine")
                        input("Presione Enter para volver al menu anterior...")
                case 3:
                    input("\nIngresó a la opción 3. Consultar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Programación Películas ***\n")
                    if self.cont_programacion == 0:
                        print("No hay ninguna programación registrada.")
                case 4:
                    input("\nIngresó a la opción 4. Consultar información películas. Presione Enter para continuar ...")
                    if self.cont_peliculas == 0:
                        print("\nNo hay ninguna película registrada.")
                    else:
                        self.consultar_info_peliculas()
                case 5:
                    self.usuario_auntenticado= None
                case _:
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")

    # Muestra el menu del Cliente con sus respectivas funcionalidades
    def mostrar_menu_cliente(self):
        opcion = 0

        while opcion != 5:
            while True:
                try:
                    print ("\n********************")
                    print (" MENU DE CLIENTE")
                    print ("********************\n")
                    print("1. Consultar salas de cine\n2. Consultar programacion peliculas")
                    print("3. Consultar informacion peliculas\n4. Realizar una reserva\n5.Cerrar sesion")
                    opcion = int(input("Seleccione una opción del menú: "))
                    break
                except ValueError:
                    print("\nError en la selección del menú. Por favor inténtelo nuevamente...\n")
            match opcion:
                case 1:
                    input("\nIngresó a la opción 1. Consultar salas de cine. Presione Enter para continuar ...")
                    print ("\n*** Listado de Salas ***\n")
                    if self.cont_salas == 0:
                        print("No hay salas de cine registradas.")
                    else: 
                        self.imprimir_listado(self.salascine, "Salas de Cine")
                        input("Presione Enter para volver al menu anterior...")
                case 2:
                    input("\nIngresó a la opción 2. Consultar programacion peliculas. Presione Enter para continuar ...")
                    print ("\n*** Programación Películas ***\n")
                    if self.cont_programacion == 0:
                        print("No hay ninguna programación registrada.")
                    else:
                        self.imprimir_listado(self.programaciona,"Pogramación")
                case 3:
                    input("\nIngresó a la opción 3. Consultar información películas. Presione Enter para continuar ...")
                    print ("\n*** Información Películas ***\n")
                    if self.cont_peliculas == 0:
                        print("No hay ninguna película registrada.")
                    else: 
                        self.consultar_info_peliculas()
                case 4:
                    input("\nIngresó a la opción 4. Realizar una reserva. Presione Enter para continuar ...")
                    print ("\n*** RESERVA ***\n")
                case 5:
                    self.usuario_auntenticado= None
                case _:
                    input("\nIngresó una opción incorrecta. Presione Enter para continuar ...")

    # Este método permite autenticar a un usuario y ademas retorna True si se pudo autenticar el usaurio, False en caso contrario
    def autenticar_usuario(self):
        id_usuario = 0
        # Se piden los datos de autenticación
        print ("\n****************************************")
        print (" Autenticación de Usuarios")
        print ("****************************************\n")

        while True:
            try:
                id_usuario = int(input("Ingrese el número de documento del usuario: "))
                break
            except ValueError:
                print("\nError en la autenticación. Por favor ingrese un número de documento válido e intente nuevamente.\n")

        # Busca al usuario con el ID ingresado en el arreglo de usuarios
        for i in range(self.cont_usuarios):
            if self.usuarios[i].id == id_usuario:
                contrasenna = input("Ingrese la contraseña del usuario: ")
                # Si la contraseña coincide con la que ya fue almacenada, se actualiza el usuario autenticado y retorna True
                if self.usuarios[i].contrasenna == contrasenna:
                    self.usuario_auntenticado = self.usuarios[i]
                    return True
                else:
                    # Si la contraseña no coincide se muestra un mensaje y se retorna False
                    input("\nError en la autenticación: Contraseña incorrecta. Presione Enter para continuar ...")
                    return False

        # Si no se cumple ninguno de los casos anteriores se muestra
        input(f"\nEl usuario con ID {id_usuario} no se encuentra registrado en la base de datos. Por favor presione Enter y vuélvalo a intentar.")
        return False
    
    # Este el método es el que inicia la aplicación
    def menu_principal(self):
        opcion = 0
        while opcion != 2:
            print ("\n****************************************")
            print(f"\tMenú Principal Complejo {self.nombre_complejo}")
            print ("****************************************\n")
            while True:
                try:
                    print("1. Autenticarse\n2. Salir de la app")
                    opcion = int(input("Seleccione una opción del menú: "))
                    break
                except ValueError:
                    print("\nError en la autenticación. Por favor inténtelo nuevamente.\n")

            # noinspection PyUnreachableCode
            match opcion:
                case 1:
                    if self.autenticar_usuario():
                        if self.usuario_auntenticado.tipo == Usuario.PERFIL_ADMINISTRADOR:
                            self.mostrar_menu_admin()
                        elif self.usuario_auntenticado.tipo == Usuario.PERFIL_VENDEDOR:
                            self.mostrar_menu_vendedor()
                        elif self.usuario_auntenticado.tipo == Usuario.PERFIL_CLIENTE:
                            self.mostrar_menu_cliente()
                        else:
                            print("PERFIL NO RECONOCIDO")
                case 2:
                    self.usuario_auntenticado = None
                    print("\nVuelva pronto. Aplicación terminada")
                case _:
                    print("\nOpción incorrecta. Inténtelo de nuevo")

obj = Complejo()
print("Bienvenido a ¿Que hay para ver?")
obj.pedir_datos()
obj.menu_principal()

