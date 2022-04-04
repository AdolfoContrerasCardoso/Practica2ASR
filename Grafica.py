import re
import sys
import rrdtool
import time


def obtenerDatos(minutos,hostname,var):
   tiempo_actual = int(time.time())
   #Grafica desde el tiempo actual menos diez minutos
   tiempo_inicial = tiempo_actual - minutos
   tiempo_inicial = str(tiempo_inicial)

   ret = rrdtool.graphv(f"img/{var}.png",
                        "--start",tiempo_inicial,
                        "--end","N",
                        "--vertical-label=Segmentos",
                        "--title=Segmentos TCP de un agente \n Usando SNMP y RRDtools",
                        f"DEF:{var}={hostname}/{hostname}.rrd:{var}:AVERAGE",
                        f"VDEF:{var}Last={var},MAXIMUM",
                        f"VDEF:{var}Min={var},MINIMUM",
                        f"PRINT:{var}Last:%6.2lf",
                        f"PRINT:{var}Min:%6.2lf",
                        f"LINE3:{var}#0000FF:Segmentos enviados")

   data = []
   for i in ret.items():
      data.append(list(i))
   max = data[0][1]
   min = data[1][1]
   diferencia = float(max)-float(min)
   return diferencia
   
   

if(__name__=='__main__'):
   obtenerDatos(2,'localhost','tcpin')