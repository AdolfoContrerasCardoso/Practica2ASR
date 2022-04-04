from os import *
import sys
import rrdtool
import time
from SNMPget import *


OIDS = [
    #tcpInSegs
    '1.3.6.1.2.1.6.10.0',
    #tcpOutSegs
    '1.3.6.1.2.1.6.11.0',
    #octin
    '1.3.6.1.2.1.2.2.1.10.1',
    #octout
    '1.3.6.1.2.1.2.2.1.16.1',
]
class Creator():

    def create(host):
        ret = rrdtool.create(f'{host}/{host}.rrd',
                            "--start",'N',
                            "--step",'60',
                            "DS:tcpin:COUNTER:600:U:U",
                            "DS:tcpout:COUNTER:600:U:U",
                            "DS:octin:COUNTER:600:U:U",
                            "DS:octout:COUNTER:600:U:U",
                            "RRA:AVERAGE:0.5:6:5",
                            "RRA:AVERAGE:0.5:1:30")

        if ret:
            print (rrdtool.error())

    def graph(host, var, title, descr, ti='N', tf = 'N'):       
        ret = rrdtool.graph(f'{host}/{host} {var}.png',
                        "--start",ti,
                        "--end",tf,
                        "--vertical-label=Bytes/s",
                        f"--title={title}",
                        f"DEF:{var}={host}/{host}.rrd:{var}:AVERAGE",
                        f"LINE3:{var}#0000FF:{descr}") 

    def Update(self):
        while(True):
            for host in self.host:
                info = [getConsulta(host[0],host[1],host[2],host[3],oid) for oid in OIDS]
                info = 'N:' + ':'.join([str(e) for e in info])
                rrdtool.update(f'{host[0]}/{host[0]}.rrd', info)
                rrdtool.dump(f'{host[0]}/{host[0]}.rrd', f'{host[0]}/{host[0]}.xml')
    

    def __init__(self,host):
        self.host = host

    def CrearRRD(self):
        for i in self.host:
            Creator.create(i[0])