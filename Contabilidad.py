import os
import datetime

from SNMPget import *

def crearReporte(hostname,version,comunidad,puerto,tcpin,tcpout,octin,octout):
        nombre = getConsulta(hostname,version,comunidad,puerto,'1.3.6.1.2.1.1.5.0')
        descripcion = getConsulta(hostname,version,comunidad,puerto,'1.3.6.1.2.1.1.1.0')
        tcpPassiveOpens = getConsulta(hostname,version,comunidad,puerto,'1.3.6.1.2.1.6.6.0')
        fecha = datetime.datetime.now()
        archivo = f'{hostname}.txt'
        f = open(archivo,'w')
        f.write(f'''date: {fecha} device: {nombre} 
        description: {descripcion}
        defaultProtocol: radius
        rdate: {fecha}
        #NAS-IP-Address
        4: {hostname}
        #NAS-Port
        5: 22
        #NAS-Port-Type
        61: 2
        #User-Name
        1: ssh1
        #Acct-Status-Type
        40: 2
        #Acct-Delay-Time
        41: 12
        #Acct-Input-Octets
        42: {octin}
        #Acct-Output-Octets
        43: {octout}
        #Acct-Session-Id
        44: 121
        #Acct-Authentic
        45: 1
        #Acct-Session-Time
        46: 1453
        #Acct-Input-Packets
        47: {tcpin}
        #Acct-Output-Packets
        48: {tcpout}
        #Acct-Terminate-Cause
        49: 7
        #Acct-Multi-Session-Id
        50: 63
        #Acct-Link-Count
        51: 1
        #tcpPassiveOpens
        52: {tcpPassiveOpens}
        ''')
        f.write
        f.close()
if __name__ == '__main__':
    crearReporte()