#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mariadb
import os
import time
def menuGral():
	limpioPantalla()
	print("\n" + '''
* * * * * * * * * * * * * * * * * * * * * * *

 * * * * * * MENU PPAL. COMERCIO * * * * * *

* * * * * * * * * * * * * * * * * * * * * * *

	1 - CAJA

	2 - DEPOSITO

	3 - ADMINISTRACION
	
	0 - SALIR''' + "\n")
def limpioPantalla():
	sisOper = os.name
	if sisOper == "posix":
		os.system("clear")
	elif sisOper == "ce" or sisOper == "nt" or sisOper == "dos":  # windows
		os.system("cls")
class ArtLimp(object):
	def __init__(self): #ya esta
		self.mydb = ""
		self.mycursor = ""
#############################################################################################		
################### DESDE ACA HAY QUE PEGAR EL CONECTOR PROPIO PARA LA BD####################		
	def coneccionMDB(self):
		self.mydb = mariadb.connect(
						 host="127.0.0.1",
						 user="root",
						 autocommit=True)
					
	def conecBD(self):
		self.mydb = mariadb.connect(
					host="127.0.0.1",
					user="root",
					database = "ARTICULOS_LIMPIEZA"
		)
	def nuevaBD(self):
		while True:
			try:
				self.mydb = mariadb.connect(
									host="127.0.0.1",
									user="root",
									autocommit=True
				)
				print(self.mydb)        
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE DATABASE ARTICULOS_LIMPIEZA")
				print("\n" + "SE GENERO DATABASE ARTICULOS_LIMPIEZA")
				self.mycursor.execute("SHOW DATABASES")
				for ind in self.mycursor:
					print(ind)
			except mariadb.ProgrammingError:
				print("\n" + "La base YA EXISTE")
			continuar=str(input("\n" + "Pulse ENTER para continuar..."))
			break
################### HASTA ACA HAY QUE PEGAR EL CONECTOR PROPIO PARA LA BD####################
#############################################################################################
	def crearTablaCli(self):
		while True:
			try:
				limpieza.conecBD()
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE TABLE ClientesArtLimp(dni_Cli INT PRIMARY KEY,nombre_Cli VARCHAR(255), apellido_Cli VARCHAR(255),telefono_Cli INT, direccion_calleCli VARCHAR(255), direccion_nroCli INT, ciudad_Cli VARCHAR(255), mail_Cli VARCHAR(150),iva_Cli INT")
				print("\n" + "SE GENERO TABLA CLIENTES EN DB ARTICULOS_LIMPIEZA")
			except mariadb.OperationalError:
				print("\n" + "LA TABLA CLIENTE YA EXISTE")
			time.sleep(1)
			break
	def crearTablaProveedor(self):
		while True:
			try:
				limpieza.conecBD()
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE TABLE ProveedorLimp(dni_Prov INT PRIMARY KEY,nombre_Prov VARCHAR(255), apellido_Prov VARCHAR(255),telefono_Prov INT, direccion_calleProv VARCHAR(255), direccion_nroProv INT, ciudad_Prov VARCHAR(255), mail_Prov VARCHAR(150),iva_Prov VARCHAR(255))")
				print("\n" + "SE GENERO TABLA PROVEEDORES EN DB ARTICULOS_LIMPIEZA")
			except mariadb.OperationalError:
				print("\n" + "LA TABLA PROVEEDORES YA EXISTE")
			time.sleep(1)
			break	
	def crearTablaProd(self):
		while True:
			try:
				limpieza.conecBD()
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE TABLE ProductosLimp(codigo_Prod INT PRIMARY KEY, marca_Prod VARCHAR(255), tipodeuso_Prod VARCHAR(255), precioProdMin INT)")
				print("\n" + "SE GENERO TABLA PRODUCTOS EN DB ARTICULOS_LIMPIEZA")
			except mariadb.OperationalError:
				print("\n" + "LA TABLA PRODUCTOS YA EXISTE")
			time.sleep(1)
			break	
	def crearTablaProdStock(self):
		while True:
			try:
				limpieza.conecBD()
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE TABLE StockProductosLimp(codigo_Prod INT PRIMARY KEY, stock_Prod INT)")
				print("\n" + "SE GENERO TABLA STOCK PRODUCTOS EN DB ARTICULOS_LIMPIEZA")
			except mariadb.OperationalError:
				print("\n" + "LA TABLA STOCK PRODUCTOS YA EXISTE")
			time.sleep(1)
			break

	def crearTablaVentas(self): # VERIFICAR LAS TABLAS PARA GENERAR LA VENTA
		while True:
			try:
				limpieza.conecBD()
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE TABLE VentasComercio(id_Venta INT PRIMARY KEY, codigo_Prod INT, Fecha_Venta VARCHAR(255), dni_Cli INT, montoTotalVenta INT)")
				print("\n" + "SE GENERO TABLA VENTAS EN DB ARTICULOS_LIMPIEZA")
			except mariadb.OperationalError:
				print("\n" + "LA TABLA VENTAS YA EXISTE")
			time.sleep(1)
			break	

	def crearTablaCompra(self): # VERIFICAR LAS TABLAS PARA GENERAR LA VENTA
		while True:
			try:
				limpieza.conecBD()				
				self.mycursor = self.mydb.cursor()
				self.mycursor.execute("CREATE TABLE TicketComercio(cod_Ticket INT PRIMARY KEY, id_Venta INT, iva_Cli VARCHAR(255), codigo_Prod INT, cant_Venta INT, montoVtaProd INT)")
				seguir=str(input("\n" + "Se genero la tabla Ticket. Pulse ENTER para continuar...."))
				print("\n" + "SE GENERO TABLA TICKETS EN DB ARTICULOS_LIMPIEZA")
			except mariadb.OperationalError:
				print("\n" + "LA TABLA TICKET YA EXISTE")
			time.sleep(1)
			break	
	def nuevo_cliente(self):
		while True:
			try:
				limpioPantalla()				
				print("\n" + "< < SE GENERARA UN NUEVO CLIENTE > >")
				print("\n" + "INGRESE")
				dni_Cli = int(input("\n" + "DNI Nº: "))
				nombre_Cli = str(input("NOMBRE: "))
				apellido_Cli = str(input("APELLIDO: "))
				telefono_Cli = int(input("TELEF0NO Nº: "))
				direccion_calleCli = str(input("NOMBRE DE CALLE: "))
				direccion_nroCli = int(input("DOMICILIO Nº: "))
				ciudad_Cli = str(input("CIUDAD: "))
				mail_Cli = str(input("MAIL: "))
				print("\n" + "RESPONSABLE INSCRIPTO: 1" + "\n" + "CONSUMIDOR FINAL: 2" + "\n")
				iva_Cli = int(input("IVA: "))
				self.mycursor = self.mydb.cursor()
				sql = "INSERT INTO ClientesArtLimp(dni_Cli,nombre_Cli,apellido_Cli,telefono_Cli,direccion_calleCli,direccion_nroCli,ciudad_Cli,mail_Cli,iva_Cli) VALUES (%d, %s, %s, %d, %s, %d, %s, %s, %d)"
				val = (dni_Cli,nombre_Cli,apellido_Cli,telefono_Cli,direccion_calleCli,direccion_nroCli,ciudad_Cli,mail_Cli,iva_Cli)
				self.mycursor.execute(sql, val)
				self.mydb.commit()
				print("\n",self.mycursor.rowcount," Registro insertado en BD ClientesArtLimp.")
				print("\n" + "SE GENERO UN NUEVO CLIENTE: ", nombre_Cli, apellido_Cli)
				continuar=str(input("\n" + "Pulse ENTER para continuar..."))
				break
			except mariadb.IntegrityError:
				print("\n" + "DNI EXISTENTE")
				continuar=str(input("\n" + "Pulse ENTER para continuar..."))
				break
	def modificar_NomClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		nombre = input("\n" + "Ingrese NOMBRE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET nombre_Cli = '"+nombre+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def modificar_ApeClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		apellido = input("\n" + "Ingrese APELLIDO a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET apellido_Cli = '"+apellido+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def modificar_DireCalleClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		direcalle = input("\n" + "Ingrese CALLE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET direccion_calleCli = '"+direcalle+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def modificar_DireNumClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		nrocalle = input("\n" + "Ingrese NUMERO CALLE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET direccion_nroCli = '"+nrocalle+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def modificar_DireCiudadClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		nombreCiudad = input("\n" + "Ingrese NOMBRE DE CIUDAD a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET ciudad_Cli = '"+nombreCiudad+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def modificar_TelClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		telefono = input("\n" + "Ingrese TELEFONO a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET telefono_Cli = '"+telefono+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def modificar_MailClientes(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		mail = input("\n" + "Ingrese MAIL a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET mail_Cli = '"+mail+"' WHERE dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where dni_Cli = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	def eliminar_cliente(self):
		print("\n" + "< < SE ELIMINARA CLIENTE > >")
		condicion=str(input("\n" + "QUE CLIENTE DESEA ELIMINAR?: "))
		self.mycursor = self.mydb.cursor()
		sql = "DELETE FROM ClientesArtLimp WHERE dni_Cli LIKE '%"+condicion+"%'"
		self.mycursor.execute(sql)
		self.mydb.commit()
		print("\n",self.mycursor.rowcount, " registros eliminados")
		continuar=str(input("\n" + "Pulse ENTER para continuar...")) # A Partir de aca 

	def nuevo_Proveedor(self): # Esta parte es de Eliam
		while True:
			try:
				limpioPantalla()				
				print("\n" + "< < SE GENERARA UN NUEVO PROVEEDOR > >")
				print("\n" + "INGRESE")
				dni_Prov = int(input("\n" + "DNI Nº: "))
				nombre_Prov = str(input("NOMBRE: "))
				apellido_Prov = str(input("APELLIDO: "))
				telefono_Prov = int(input("TELEF0NO Nº: "))
				direccion_calleProv = str(input("NOMBRE DE CALLE: "))
				direccion_nroProv = int(input("DOMICILIO Nº: "))
				ciudad_Prov = str(input("CIUDAD: "))
				mail_Prov = str(input("MAIL: "))
				iva_Prov = 1
				self.mycursor = self.mydb.cursor()
				sql = "INSERT INTO ProveedorLimp(dni_Prov,nombre_Prov,apellido_Prov,telefono_Prov,direccion_calleProv,direccion_nroProv,ciudad_Prov, mail_Prov,iva_Prov) VALUES (%d, %s, %s, %d, %s, %d, %s, %s, %s)"
				val = (dni_Prov,nombre_Prov,apellido_Prov,telefono_Prov,direccion_calleProv,direccion_nroProv,ciudad_Prov,mail_Prov,iva_Prov)
				self.mycursor.execute(sql, val)
				self.mydb.commit()
				print("\n", self.mycursor.rowcount," Registro insertado en BD ProveedorArtLimp")
				print("\n" + "SE GENERO NUEVO PROVEEDOR: ", nombre_Prov, apellido_Prov)
				continuar=str(input("\n" + "Pulse ENTER para continuar..."))
				break
			except mariadb.IntegrityError:
				print("\n" + "DNI EXISTENTE")
				continuar=str(input("\n" + "Pulse ENTER para continuar..."))
				break
    
	def modificar_NomProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		nombre = input("\n" + "Ingrese NOMBRE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET nombre_Prov = '"+nombre+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

	def modificar_ApeProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		apellido = input("\n" + "Ingrese APELLIDO a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET apellido_Prov = '"+apellido+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

	def modificar_DireCalleProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		direcalle = input("\n" + "Ingrese CALLE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET direccion_calleProv = '"+direcalle+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

	def modificar_DireNumProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		nrocalle = input("\n" + "Ingrese NUMERO CALLE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET direccion_nroProv = '"+nrocalle+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

	def modificar_DireCiudadProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		nombreCiudad = input("\n" + "Ingrese NOMBRE DE CIUDAD a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET ciudad_Prov = '"+nombreCiudad+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

	def modificar_TelProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		telefono = input("\n" + "Ingrese TELEFONO a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET telefono_Prov = '"+telefono+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

	def modificar_MailProveedor(self):
		dni = input("\n" + "Ingrese DNI de la persona a modificar: ")
		mail = input("\n" + "Ingrese MAIL a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ProveedorLimp SET mail_Prov = '"+mail+"' WHERE dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ProveedorLimp where dni_Prov = "+dni
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
	
	def eliminar_Proveedor(self):
		print("\n" + "< < SE ELIMINARA PROVEEDOR > >")
		condicion=str(input("\n" + "QUE PROVEEDOR DESEA ELIMINAR?: "))
		self.mycursor = self.mydb.cursor()
		sql = "DELETE FROM ProveedorLimp WHERE dni_Prov LIKE '%"+condicion+"%'"
		self.mycursor.execute(sql)
		self.mydb.commit()
		print("\n",self.mycursor.rowcount, " registros eliminados")
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
	def nuevo_Producto(self): #Parte de Ema
		while True:
			try:
				limpioPantalla()			
				print("\n" + "< < SE INGRESA UN NUEVO PRODUCTO > >")
				print("\n" + "INGRESE")
				codigo_Prod = int(input("\n" + "CODIGO Nº: "))
				marca_Prod = str(input("MARCA: "))
				tipodeuso_Prod = str(input("TIPO DE USO: "))
				cantidad_Prod = int(input("CANTIDAD INGRESA Nº: "))# cambiar esto
				precioProdMayo = int(input("PRECIO PROVEEDOR Nº: "))# cambiar esto
				precioProdMin = int(input("PRECIO VENTA Nº: "))
				self.mycursor = self.mydb.cursor()
				sql = "INSERT INTO ProductosLimp(codigo_Prod, marca_Prod,tipodeuso_Prod,cantidad_Prod,precioProdMayo,precioProdMin)VALUES(%d,%s,%s,%d,%d,%d)"
				val = (codigo_Prod, marca_Prod,tipodeuso_Prod,cantidad_Prod,precioProdMayo,precioProdMin)
				self.mycursor.execute(sql, val)
				self.mydb.commit()
				print("\n",self.mycursor.rowcount," Registro insertado en BD ProductosLimp" + "\n")
				print("SE GENERO NUEVO PRODUCTO: ", tipodeuso_Prod, marca_Prod)
				continuar=str(input("\n" + "Pulse ENTER para continuar..."))
				break
			except mariadb.IntegrityError:
				print("\n" + "PRODUCTO EXISTENTE")
				continuar=str(input("\n" + "Pulse ENTER para continuar..."))
				break


def codigo_prod(self):#listo
		ingreso_codigo = input("\n" + "Ingrese codigo de la persona a modificar: ")
		nombre_produ = input("\n" + "Ingrese NOMBRE a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where codigo_prod = "+ingreso_codigo
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET nombre_produ = '"+nombre_produ+"' WHERE  = "+ingreso_codigo
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where nombre_produ = "+ingreso_codigo
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
def  marca_prod(self):# listo
		codigo_marca = input("\n" + "Ingrese Codigo de la persona a modificar: ")
		nombre_marca = input("\n" + "Ingrese nombre de marca  a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where codigo_marca = "+codigo_marca
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET nombre_marca = '"+nombre_marca+"' WHERE codigo_marca = "+codigo_marca
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where codigo_marca = "+codigo_marca
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
def tipodeuso_Prod(self):# listo
		Numero_de_uso= input("\n" + "Ingrese numero de uso de la persona a modificar: ")
		numero_de_serie = input("\n" + "Ingrese numero de serie a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where Numero_de_uso  = "+Numero_de_uso
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET numero_de_serie = '"+numero_de_serie+"' WHERE Numero_de_uso = "+Numero_de_uso
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where Numero_de_uso = "+Numero_de_uso
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break
def cantidad_Prod(self):#listo
		  
        while True:
            try:
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute("CREATE TABLE cliente (dni INT PRIMARY KEY, nombre VARCHAR(255), direccion VARCHAR(255), tarjeta INT)")
            except mariadb.OperationalError:
                print("La tabla cliente ya existe")
            break
def insert_cant(self):
        self.mycursor = self.mydb.cursor()
        sql = "INSERT INTO cantidad_prod (dni, nombre, direccion, tarjeta) VALUES (%s, %d, %s, %d)"
        val = [
            (42123123,'Papu  Gomez','villa bosch 4',45673456),
            (11111111,'julian alvarez','Dillon 652', 47567676),
            (22222222,'Lionel messi','Aguado 21',45657676),
            (33333333,'Miguel scaloneta','Muñiz 345',48569898)
            ]
        self.mycursor.executemany(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "Fueron insertados.")
			
def precioProdMayo(self): # listo
		  
        while True:
            try:
                self.mycursor = self.mydb.cursor()
                self.mycursor.execute("CREATE TABLE precioprodmayo (N_mayo INT PRIMARY KEY, nombre VARCHAR(255), direccion VARCHAR(255), NUM_ID INT)")
            except mariadb.OperationalError:
                print("La tabla cliente ya existe")
            break
def insertoRegis(self):
        self.mycursor = self.mydb.cursor()
        sql = "INSERT INTO cliente (N_mayo, nombre, direccion, NUM_id) VALUES (%s, %d, %s, %d)"
        val = [
            (42123123,'Pedro Gomez','Santa Rosa 4',45673456),
            (11111111,'Amalia Perez','Dillon 652', 47567676),
            (22222222,'Analia Gonzalez','Aguado 21',45657676),
            (33333333,'Miguel Lopez','Muñiz 345',48569898)
            ]
        self.mycursor.executemany(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "Fueron insertados.")
def precioProdMin(self):# listo
		Precio_min = input("\n" + "Ingrese precio minorista  a modificar: ")
		nro_tarjeta = input("\n" + "Ingrese numero de tarjeta  a cambiar: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ClientesArtLimp where precio_min = "+Precio_min
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
		sql = "UPDATE ClientesArtLimp SET nro_tarjeta = '"+nro_tarjeta+"' WHERE Precio_min = "+Precio_min
		self.mycursor.execute(sql)
		self.mydb.commit()
		print(self.mycursor.rowcount, " registros modificados")
		time.sleep(2)
		sql = "SELECT * FROM ClientesArtLimp where Precio_min = "+Precio_min
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		for ind in self.myresultado:
			print(ind)
			time.sleep(2)
			break

def eliminar_Producto(self):
		print("\n" + "< < SE ELIMINARA PRODUCTO > >")
		condicion=str(input("\n" + "QUE PRODUCTO DESEA ELIMINAR?: "))
		self.mycursor = self.mydb.cursor()
		sql = "DELETE FROM ProductosLimp WHERE codigo_Prod LIKE '%"+condicion+"%'"
		self.mycursor.execute(sql)
		self.mydb.commit()
		print("\n",self.mycursor.rowcount, " registros eliminados")
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
def listado_Clientes(self):
		limpioPantalla()
		print("LISTADO DE CLIENTES")
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("SELECT * FROM ClientesArtLimp")
		self.myresultado = self.mycursor.fetchall()
		if len(self.myresultado) == 0:
			print("\n" + "No se han encontrado registros")
		else:
			for ind in self.myresultado:
				print("\n" + '\033[1m'"DNI:"'\033[0m', ind[0], '\033[1m'"NOMBRE:"'\033[0m', ind[1], '\033[1m'"APELLIDO:"'\033[0m', ind[2], '\033[1m'"TELEFONO:"'\033[0m', ind[3])
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
def listado_Proveedores(self):
		limpioPantalla()
		print("LISTADO DE PROVEEDORES")
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("SELECT * FROM ProveedorLimp")
		self.myresultado = self.mycursor.fetchall()
		if len(self.myresultado) == 0:
			print("\n" + "No se han encontrado registros")
		else:
			for ind in self.myresultado:
				print("\n" + '\033[1m'"DNI:"'\033[0m', ind[0], '\033[1m'"NOMBRE:"'\033[0m', ind[1], '\033[1m'"APELLIDO:"'\033[0m', ind[2], '\033[1m'"TELEFONO:"'\033[0m', ind[3])
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
def listado_Productos(self):
		limpioPantalla()
		print("LISTADO DE PRODUCTOS")
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("SELECT * FROM ProductosLimp")
		self.myresultado = self.mycursor.fetchall()
		if len(self.myresultado) == 0:
			print("\n" + "No se han encontrado registros")
		else:
			for ind in self.myresultado:
				print("\n" + '\033[1m'"CODIGO:"'\033[0m', ind[0], '\033[1m'"MARCA:"'\033[0m', ind[1], '\033[1m'"TIPO DE USO:"'\033[0m', ind[2], '\033[1m'"CANTIDAD:"'\033[0m', ind[3], '\033[1m'"PRECIO MAYORISTA:"'\033[0m', ind[4], '\033[1m'"PRECIO VENTA:"'\033[0m', ind[5])
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
def consultaPrecio(self):
		condicion = input("\n" + "Ingrese Codigo de Producto Nº: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProductosLimp where codigo_Prod LIKE '%"+condicion+"%'"
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("SELECT codigo_Prod, precioProdMin FROM ProductosLimp")
		self.miResult = self.mycursor.fetchall()
		for ind in self.miResult:
			print(ind)
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
def consultaStock(self):
		condicion = input("\n" + "Ingrese Codigo de Producto Nº: ")
		self.mycursor = self.mydb.cursor()
		sql = "SELECT * FROM ProductosLimp where codigo_Prod = '%"+condicion+"%'"
		self.mycursor.execute(sql)
		self.myresultado = self.mycursor.fetchall()
		self.mycursor = self.mydb.cursor()
		self.mycursor.execute("SELECT codigo_Prod, cantidad_Prod FROM ProductosLimp")  
		self.miResult = self.mycursor.fetchall()
		for ind in self.miResult:
			print(ind)
		continuar=str(input("\n" + "Pulse ENTER para continuar..."))
###################################################
############### INICIO DEL PROGRAMA ###############
###################################################
limpieza = ArtLimp()
limpieza.coneccionMDB()
opc = 0
while opc != 5:
	menuGral()
	opcion = int(input("ELIJA LA OPCIÓN DESEADA: "))
	if opcion == 1:
		limpioPantalla()
		print("\n"'''

  * * * * * * * LINEA DE CAJA * * * * * * *

	1 - VENTA
	
	2 - CONSULTA DE PRECIO

	3 - VERIFICAR STOCK DE PRODUCTO

	0 - VOLVER A MENU PPAL.''' + "\n")
		menuCaja = 0
		menuCaja = int(input("INGRESE OPCION: "))
		while menuCaja !=0:
			limpieza.conecBD()
			if menuCaja == 1:
				limpieza.venta()
				break	
			elif menuCaja == 2:
				limpieza.consultaPrecio()
				break		
			elif menuCaja == 3:
				limpieza.consultaStock()
				break			
			else:
				break
			mycursor.close() 
		menuGral()
	elif opcion == 2:
		limpioPantalla()
		print("\n"'''

* * * * * * * * * DEPOSITO * * * * * * * * *

	1 - VER LISTA DE PRODUCTOS
	
	2 - VERIFICAR STOCK DE PRODUCTO
	
	3 - NUEVO PRODUCTO
	
	4 - ELIMINAR PRODUCTO

	5 - VOLVER A MENU PPAL''' + "\n")
		menuDepo = 0
		menuDepo = int(input("INGRESE OPCION: "))
		while menuDepo !=0:
			limpieza.conecBD()
			limpioPantalla()
			if menuDepo == 1:
				limpieza.listado_Productos()
				break		
			elif menuDepo == 2:
				limpieza.consultaStock()
				break	
			elif menuDepo == 3:
				limpieza.nuevo_Producto()
				break
			elif menuDepo == 4:
				limpieza.eliminar_Producto()
				break			
			else:
				break
			mycursor.close() 
		menuGral()
	elif opcion == 3:
		limpioPantalla()
		print("\n"'''
			
* * * * * * * * * ADMINISTRACION * * * * * * * * *

	1 - CLIENTES
	
	2 - PROVEEDORES
	
	3 - PRODUCTOS
	
	0 - VOLVER A MENU PPAL''' + "\n")
		menuAdm = 0
		menuAdm = int(input("INGRESE OPCION: "))
		while menuAdm !=0:
			if menuAdm == 1:
				limpioPantalla()
				print("\n"'''
		
* * * * * * * * * ADMINISTRACION - CLIENTES * * * * * * * * *

	1 - VER LISTA DE CLIENTES
	
	2 - NUEVO CLIENTE
	
	3 - ELIMINAR CLIENTE
	
	4 - MODIFICAR CLIENTE
	
	0 - VOLVER A MENU PPAL''' + "\n")
				menuAdmCli = 0
				menuAdmCli = int(input("INGRESE OPCION: "))
				while menuAdmCli !=0:
					limpieza.conecBD()
					limpioPantalla()
					if menuAdmCli == 1:
						limpieza.listado_Clientes()
						break
					elif menuAdmCli == 2:
						limpieza.nuevo_cliente()
						break		
					elif menuAdmCli == 3:
						limpieza.listado_Clientes()
						limpieza.eliminar_cliente()
						break
					elif menuAdmCli == 4:
						limpioPantalla()
						print("\n"'''
		
* * * ADMINISTRACION - CLIENTES - MODIFICAR * * *

	1 - MODIFICAR NOMBRE
	
	2 - MODIFICAR APELLIDO
	
	3 - MODIFICAR DIRECCION CALLE
	
	4 - MODIFICAR DIRECCION NUMERO
	
	5 - MODIFICAR CIUDAD
	
	6 - MODIFICAR TELEFONO
	
	7 - MODIFICAR MAIL
	
	0 - VOLVER A MENU PPAL''' + "\n")
						menuModCli = 0
						menuModCli = int(input("INGRESE OPCION: "))
						while menuModCli !=0:
							limpieza.conecBD()
							limpioPantalla()
							if menuModCli == 1:
								limpieza.listado_Clientes()
								limpieza.modificar_NomClientes()
								break
							elif menuModCli == 2:
								limpieza.listado_Clientes()
								limpieza.modificar_ApeClientes()
								break
							elif menuModCli == 3:
								limpieza.listado_Clientes()
								limpieza.modificar_DireCalleClientes()
								break
							elif menuModCli == 4:
								limpieza.listado_Clientes()
								limpieza.modificar_DireNumClientes()
								break
							elif menuModCli == 5:
								limpieza.listado_Clientes()
								limpieza.modificar_DireCiudadClientes()
								break
							elif menuModCli == 6:
								limpieza.listado_Clientes()
								limpieza.modificar_TelClientes()
								break
							elif menuModCli == 7:
								limpieza.listado_Clientes()
								limpieza.modificar_MailClientes()
								break
							else:
								break
							mycursor.close()
						break
						menuGral()
					else:
						break
						menuGral()
				break
			elif menuAdm == 2:
				limpioPantalla()
				print("\n"'''
		
* * * * * * * * * ADMINISTRACION - PROVEEDORES * * * * * * * * *

	1 - VER LISTA DE PROVEEDORES
	
	2 - NUEVO PROVEEDOR
	
	3 - ELIMINAR PROVEEDOR

	4 - MODIFICAR PROVEEDOR
	
	0 - VOLVER A MENU PPAL''' + "\n")
				menuAdmProv = 0
				menuAdmProv = int(input("INGRESE OPCION: "))
				while menuAdmProv !=0:
					limpieza.conecBD()
					limpioPantalla()
					if menuAdmProv == 1:
						limpieza.listado_Proveedores()
						break	
					elif menuAdmProv == 2:
						limpieza.nuevo_Proveedor()
						break		
					elif menuAdmProv == 3:
						limpieza.listado_Proveedores()
						limpieza.eliminar_Proveedor()
						break
					elif menuAdmProv == 4:
						limpioPantalla()
						print("\n"'''
		
* * * ADMINISTRACION - PROVEEDORES - MODIFICAR * * *

	1 - MODIFICAR NOMBRE
	
	2 - MODIFICAR APELLIDO
	
	3 - MODIFICAR DIRECCION CALLE
	
	4 - MODIFICAR DIRECCION NUMERO
	
	5 - MODIFICAR CIUDAD
	
	6 - MODIFICAR TELEFONO
	
	7 - MODIFICAR MAIL
	
	0 - VOLVER A MENU PPAL''' + "\n")
						menuModProv = 0
						menuModProv = int(input("INGRESE OPCION: "))
						while menuModProv !=0:
							limpieza.conecBD()
							limpioPantalla()
							if menuModProv == 1:
								limpieza.listado_Proveedores()
								limpieza.modificar_NomProveedor()
								break
							elif menuModProv == 2:
								limpieza.listado_Proveedores()
								limpieza.modificar_ApeProveedor()
								break
							elif menuModProv == 3:
								limpieza.listado_Proveedores()
								limpieza.modificar_DireCalleProveedor()
								break
							elif menuModProv == 4:
								limpieza.listado_Proveedores()
								limpieza.modificar_DireNumProveedor()
								break
							elif menuModProv == 5:
								limpieza.listado_Proveedores()
								limpieza.modificar_DireCiudadProveedor()
								break
							elif menuModProv == 6:
								limpieza.listado_Proveedores()
								limpieza.modificar_TelProveedor()
								break
							elif menuModProv == 7:
								limpieza.listado_Proveedores()
								limpieza.modificar_MailProveedor()
								break
							else:
								break
							mycursor.close()
						break
						menuGral()
					else:
						break
					mycursor.close()
					menuGral()						
			elif menuAdm == 3:
				limpioPantalla()
				print("\n"'''
			
* * * * * * * * * ADMINISTRACION - PRODUCTOS * * * * * * * * *

	1 - VER LISTA DE PRODUCTOS
	
	2 - NUEVO PRODUCTO
	
	3 - ELIMINAR PRODUCTO
	
	0 - VOLVER A MENU PPAL''' + "\n")
				menuAdmProdu = 0
				menuAdmProdu = int(input("INGRESE OPCION: "))
				while menuAdmProdu !=0:
					limpieza.conecBD()
					limpioPantalla()
					if menuAdmProdu == 1:
						limpieza.listado_Productos()
						break	
					elif menuAdmProdu == 2:
						limpieza.nuevo_Producto()
						break		
					elif menuAdmProdu == 3:
						limpieza.listado_Productos()
						limpieza.eliminar_Producto()
						break
					else:
						break
					mycursor.close()
					menuGral()
			else:
				break
			menuGral()
	elif opcion == 4:
		limpioPantalla()
		print("\n"'''
* * * * * * * * MENU OCULTO * * * * * * * * *
* * * * * * * * * SOPORTE * * * * * * * * *

	1 - NUEVA BASE DE DATOS
	
	2 - CREAR TABLA CLIENTES
	
	3 - CREAR TABLA PROVEEDOR

	4 - CREAR TABLA PRODUCTOS
	
	5 - CREAR TABLA STOCK PRODUCTOS
	
	6 - CREAR TABLA VENTAS
	
	7 - CREAR TABLA COMPRA

	0 - VOLVER A MENU PPAL''' + "\n")
		menuSop = 0
		menuSop = int(input("INGRESE OPCION: "))
		while menuSop !=0:
			limpioPantalla()
			if menuSop == 1:
				limpieza.nuevaBD()
				break
			elif menuSop == 2:
				limpieza.crearTablaCli()
				break
			elif menuSop == 3:
				limpieza.crearTablaProveedor()
				break
			elif menuSop == 4:
				limpieza.crearTablaProd()
				break	
			elif menuSop == 5:
				limpieza.crearTablaProdStock()
				break	
			elif menuSop == 6:
				limpieza.crearTablaVentas()
				break
			elif menuSop == 7:
				limpieza.crearTablaCompra()
				break			
			else:
				break
			break
	else:
		exit()
	
