import os
import threading
from RRDcreator import *
from Grafica import *
from SNMPget import *
from Contabilidad import *


class Menu():


    def Operacion(opcion,host,min):
        if(opcion=='s'):
            print('Creando reporte')
            hostname = host[0][0]
            version = host[0][1]
            comunidad = host[0][2]
            puerto = host[0][3]
            tcpin = obtenerDatos(min,hostname,'tcpin')
            tcpout = obtenerDatos(min,hostname,'tcpout')
            octin = obtenerDatos(min,hostname,'octin')
            octout = obtenerDatos(min,hostname,'octout')
            crearReporte(hostname,version,comunidad,puerto,tcpin,tcpout,octin,octout)
            print(f'Se ha creado el reporte de: {hostname}')
        elif(opcion=='n'):
            print('Cerrando programa')
            quit()

    def Opciones(host,min):
        r = input('¿Crear reporte de contabilidad? (s/n): ')
        Menu.Operacion(r,host,min)

    def __init__(self):
        agente = []
        host = []
        print('Practica 2')
        hostname = input('Introduce la direccion del hostname: ')
        version = int(input('Introduce la version SNMP: '))
        comunidad = input('Introduce la comunidad: ')
        puerto = int(input('Introduce el puerto: '))
        mins = int(input('Introduce el tiempo en min para generar datos: '))
        mins = mins*60
        agente.append(hostname)
        agente.append(version)
        agente.append(comunidad)
        agente.append(puerto)
        host.append(agente)
        m = Creator(host)
        m.CrearCarpetas()
        m.CrearRRD()

        hilo = threading.Thread(target=m.Update,)
        hilo2 = threading.Thread(target=Menu.Opciones,args=(host,mins),)

        hilo.start()
        hilo2.start()

if(__name__=='__main__'):
    Menu()