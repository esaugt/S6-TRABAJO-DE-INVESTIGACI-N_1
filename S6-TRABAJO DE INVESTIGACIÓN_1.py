from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado

    @abstractmethod
    def mostarDatos(self):
        pass

class Cliente(Persona):
    idCliente = 0
    #contadorCliente muestra el número del cliente al momento de ingresar por teclado
    contadorCliente = 1
    def __init__(self, nombre, cedula, estado):
        super().__init__(nombre, estado)
        Cliente.idCliente += 1
        Cliente.contadorCliente += 1
        self.idCliente = Cliente.idCliente
        self.cedula = cedula

    def mostarDatos(self):
        print("\nCliente: ", self.idCliente)
        print("Nombre:", self.nombre)
        print("Cedula:", self.cedula)
        print("Estado:", self.estado)

class Factura:
    idFactura = 0

    #contadorFactura muestra el número del cliente al momento de ingresar por teclado
    contadorFactura = 1
    def __init__(self, cliente, fecha, total, estado):
        Factura.idFactura += 1
        Factura.contadorFactura += 1 
        self.idFactura = Factura.idFactura
        self.cliente = cliente
        self.fecha = fecha
        self.total = total
        self.estado = estado

    def mostarDatosF(self):
        print("Id Factura:", self.idFactura)
        print("Fecha:", self.fecha)
        print("Total:", self.total)
        print("Estado:", self.estado)

class CabCredito:
    idCadCredito = 1
    contadorCredito = 1
    def __init__(self, factura, fecha, deuda, numeroCuotas, cuota, aamminicial, detalleCredito, estado):
        CabCredito.idCadCredito +=1
        CabCredito.contadorCredito +=1
        self.idCadCredito = CabCredito.idCadCredito
        self.factura = factura
        self.fecha = fecha
        self.deuda = deuda
        self.numeroCuotas = numeroCuotas
        self.cuota = cuota
        self.aamminicial = aamminicial
        self.detalleCredito = detalleCredito
        self.estado = estado

    def mostarDatosC(self):
        print("Id CadCredito:", self.idCadCredito)
        print("Código de Factura:", self.factura)
        print("Fecha:", self.fecha)
        print("Deuda:", self.deuda)
        print("Numero de Cuotas:", self.numeroCuotas)
        print("Cuota:", self.cuota)
        print("Aamm Inicial:", self.aamminicial)
        print("Detalle Crédito:", self.detalleCredito)
        print("Estado:", self.estado)

    @staticmethod
    def getintere():
        return 0.01

class DetCredito:
    idDetCredito = 0
    def __init__(self, aamm, cuota, detPago, estado):
        DetCredito.idDetCredito += 1
        self.idDetCredito = DetCredito.idDetCredito
        self.aamm = aamm
        self.cuota = cuota
        self.detPago = detPago
        self.estado = estado

    def mostarDatos(self):
        print("Id DetCredito:", self.idDetCredito)
        print("Aamm:", self.aamm)
        print("Cuota:", self.cuota)
        print("DetPago:", self.detPago.idPago)
        print("Estado:", self.estado)

    def agregarPago(self):
        self.detPago.realizarPAgo()
        self.estado = True
        print("Pago realizado con éxito!")

class Pago:
    idPago = 0
    def __init__(self, fechaPago, valor):
        Pago.idPago += 1
        self.idPago = Pago.idPago
        self.fechaPago = fechaPago
        self.valor = valor

    def mostarDatos(self):
        print("Id Pago:", self.idPago)
        print("Fecha Pago:", self.fechaPago)
        print("Valor:", self.valor)

    def realizarPAgo(self):
        self.valor = CabCredito.deuda - self.valor
        print("Pago realizado exitosamente, el valor debido es:", self.valor)

class Calculo(ABC):
    @abstractmethod
    def realizarPago(self, int, float):
        pass
    
lstCliente=[]
FacT=[]
cabCredito = []
Pag= []

#Menú principal
def menu():
    while True:
        print("""
        *------------------------------------*
        |      MENU CUENTAS POR COBRAR       |
        |------------------------------------|
        | 1. Cliente                         |
        | 2. Factura                         |
        | 3. Crédito                         |
        | 4. Pagos                           |
        | 5. Consultas Generales             |
        | 6. Salir                           |
        *------------------------------------*
        """)
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            while True:
                print("""
                *------------------------------------*
                |  MENU CUENTAS POR COBRAR - CLIENTE |
                |------------------------------------|
                | 1. Ingresar Datos                  |
                | 2. Mostrar Datos                   |
                | 3. Salir                           |
                *------------------------------------*
                """)
                opcion = int(input("Ingrese una opción: "))
                print("""""")
                if opcion ==1:
                    print("Codigo del Cliente: ", Cliente.contadorCliente)
                    Persona.nombre = input("Ingresa el nombre del cliente: ")
                    Persona.cedula = int(input("Ingresa cedula del cliente: "))
                    Persona.estado = bool(True)
                    cliente1 = Cliente(Persona.nombre, Persona.cedula, Persona.estado)
                    lstCliente.append(cliente1)
                    with open("clientes.txt", "w") as file:
                        for cliente in lstCliente:
                            file.write("Codigo del Cliente: " + str(cliente.idCliente) + "\n")
                            file.write("Nombre del Cliente: " + cliente.nombre + "\n")
                            file.write("Cedula del Cliente: " + str(cliente.cedula) + "\n")
                            file.write("Estado del Cliente: " + str(cliente.estado) + "\n")
                    print("Datos de los clientes guardados en clientes.txt")
                    print("\nCliente agregado correctamente.")
                elif opcion ==2:
                    try:
                        with open("clientes.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de clientes guardados en el archivo clientes.txt")
                elif opcion ==3:        
                    break
        elif opcion == 2:
            while True:
                print("""
                *------------------------------------*
                | MENU CUENTAS POR COBRAR - FACTURA  |
                |------------------------------------|
                | 1. Ingresar factura                |
                | 2. Mostrar factura                 |
                | 3. Salir                           |
                *------------------------------------*
                """)
                opcion = int(input("Ingrese una opción: "))
                if opcion ==1:
                    print("Codigo de Factura: ", Factura.contadorFactura)
                    Factura.cliente= input("Ingresa el nombre del cliente: ")
                    Factura.fecha= input("Ingresa fecha de factura -DD/MM/AAAA- : ")
                    Factura.total = input("Ingresa el total $: ")
                    factura1 = Factura(Factura.cliente, Factura.fecha, Factura.total, estado = True)
                    FacT.append(factura1)
                    with open("facturas.txt", "a") as file:
                        for factura in FacT:
                            file.write("Codigo de Factura: " + str(factura.contadorFactura) + "\n")
                            file.write("Nombre del Cliente: " + factura.cliente + "\n")
                            file.write("Fecha de Factura: " + factura.fecha + "\n")
                            file.write("Total: " + str(factura.total) + "\n")
                            file.write("Estado de la Factura: " + str(factura.estado) + "\n")
                    print("Datos de las facturas guardados en facturas.txt")
                    print("\nFactura agregada correctamente")
                elif opcion == 2:
                    try:
                        with open("facturas.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de facturas guardados en el archivo facturas.txt")
        
                elif opcion == 3:
                    break

        
        elif opcion == 3:
            while True:
                print("""
                *------------------------------------*
                |  MENU CUENTAS POR COBRAR - CRÉDITO |
                |------------------------------------|
                | 1. Ingresar Datos del Crédito      |
                | 2. Mostrar Detalles                |
                | 3. Salir                           |
                *------------------------------------*
                """)
                opcion = int(input("Ingrese una opción: "))
                if opcion ==1:
                    print("ID Credito: ", CabCredito.contadorCredito)
                    CabCredito.factura = input("Ingrese Número de Factura: ")
                    CabCredito.fecha = input("Ingresa la Fecha DD-MM-AAAA: ")
                    CabCredito.deuda = float(input("Ingrese el Valor de la Deuda $: "))
                    CabCredito.numeroCuotas = int(input("Ingrese la Cantidad de Cuota $: "))
                    CabCredito.cuota = int(input("Ingrese el Número de Cuota #: "))
                    CabCredito.aamminicial = input("Ingrese el AAAA-MM inicial: ")
                    CabCredito.detalleCredito= input("Ingrese los Detalles de Crédito: ")
                    cabCredito1= CabCredito(CabCredito.factura, CabCredito.fecha, CabCredito.deuda, CabCredito.numeroCuotas, CabCredito.cuota, CabCredito.aamminicial,CabCredito.detalleCredito, estado = True)
                    cabCredito.append(cabCredito1)
                    with open("creditos.txt", "a") as file:
                        for credito in cabCredito:
                            file.write("ID Credito: " + str(credito.contadorCredito) + "\n")
                            file.write("Número de Factura: " + credito.factura + "\n")
                            file.write("Fecha: " + credito.fecha + "\n")
                            file.write("Deuda: " + str(credito.deuda) + "\n")
                            file.write("Numero de Cuotas: " + str(credito.numeroCuotas) + "\n")
                            file.write("Numero de Cuota: " + str(credito.cuota) + "\n")
                            file.write("Año y Mes Inicial: " + str(credito.aamminicial) + "\n")
                            file.write("Detalles de Crédito: " + str(credito.detalleCredito) + "\n")
                            file.write("Estado de Crédito: " + str(credito.estado) + "\n")
                    print("Datos de los créditos guardados en creditos.txt")
                    print("\Datos agregados correctamente.")
                elif opcion ==2:
                    try:
                        with open("creditos.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except:
                        print("No hay datos de créditos guardados en el archivo creditos.txt")
                elif opcion ==3:        
                    break 
        elif opcion == 4:
            while True:
                print("""
                *------------------------------------*
                |   MENU CUENTAS POR COBRAR - PAGO   |
                |------------------------------------|
                | 1. Ingresar Pago                   |
                | 2. Mostrar Pagos                   |
                | 3. Salir                           |
                *------------------------------------*
                """)
                opcion = int(input("Ingrese una opción: "))
                print("""""")
                if opcion ==1:
                    print("ID Credito: ", Pago.idPago)
                    Pago.fecha = input("Ingresa fecha de pago -DD/MM/AAAA- : ")
                    Pago.valor = float(input("Ingrese el Valor a Pagar: "))
                    pago1 = Pago(Pago.fecha, Pago.valor)
                    Pag.append(pago1)
                    with open("pagos.txt", "a") as file:
                        for pago in Pag:
                            file.write("ID Pago: " + str(pago.idPago) + "\n")
                            file.write("Fecha de Pago: " + pago.fecha + "\n")
                            file.write("Valor a Pagar: " + str(pago.valor) + "\n")
                    print("Datos de los pagos guardados en pagos.txt")
                    print("n\Pago agregado correctamente.")
                elif opcion ==2:
                    try:
                        with open("pagos.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de pagos guardados en el archivo pagos.txt")
                elif opcion ==3:        
                    break  
        elif opcion == 5:
            while True:
                print("""
                *-------------------------------------------*
                |MENU CUENTAS POR COBRAR-CONSULTAS GENERALES|
                |-------------------------------------------|
                | 1. Consultar Cliente                      |
                | 2. Consultar Factura                      |
                | 3. Consultar Credito                      |
                | 4. Consultar Pagos                        |
                | 5. Salir                                  |
                *-------------------------------------------*
                """)
                opcion = int(input("Ingrese una opción: "))
                print("""""")
                if opcion == 1:
                    try:
                        with open("clientes.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de clientes guardados en el archivo clientes.txt")
                
                elif opcion == 2:
                    try:
                        with open("facturas.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de facturas guardados en el archivo facturas.txt")
                
                elif opcion == 3:
                    try:
                        with open("creditos.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de créditos guardados en el archivo creditos.txt")
                
                elif opcion == 4:
                    try:
                        with open("pagos.txt", "r") as file:
                            datos = file.read()
                            print(datos)
                    except FileNotFoundError:
                        print("No hay datos de pagos guardados en el archivo pagos.txt")
                
                elif opcion == 5:
                    break
                else:
                    print("Opción inválida.")

        elif opcion == 6:
            while True:
                print("""
                *------------------------------------*
                |      SEGURO QUE DESEA SALIR        |
                |------------------------------------|
                |      S = si     o   N = NO         |
                *------------------------------------*
                """)
                opcion = input("QUE OPCION DESEA: ")
                if opcion == "S":
                    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~
                    Gracias por visitarnos
                    ~~~~~~~~~~~~~~~~~~~~~~""")
                    print(exit)
                    exit()
                elif opcion == "n":
                    menu()
                else:
                    print("Opción inválida")             
menu()