import socket
import time
import statistics

def tiempo_espera():
    time.sleep(2)

msgFromClient       = input("Escriba su nombre: ")
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Crear un socket UDP en el lado del cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(2)
mensaje = ""
print("Intentando enviar mensaje")
lista_tiempos_caracteres = []
inicio_tiempo_mensaje = time.time()
for i in range (len(msgFromClient)):
    bytesToSend = str.encode(msgFromClient[i])
    inicio_tiempo_caracter = time.time()
    # Envia al servidor usando el socket UDP creado
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("Caracter {} enviado".format(msgFromClient[i]))

    booleano = True
    while(booleano):
        try:
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        except:
            print("Ha expirado el tiempo de espera, reenviando")
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            
        else:
            fin_tiempo_caracter = time.time()
            fin_tiempo_caracter = fin_tiempo_caracter - inicio_tiempo_caracter
            lista_tiempos_caracteres.append(round(fin_tiempo_caracter, 2))
            print("Caracter aceptado")
            booleano = False

    mensaje += msgFromServer[0].decode()

fin_tiempo_mensaje = time.time()
fin_tiempo_mensaje = round(fin_tiempo_mensaje - inicio_tiempo_mensaje, 2)

promedio_tiempos_caracter = round(statistics.mean(lista_tiempos_caracteres), 2)
print("Mensaje del servidor: {}".format(mensaje))
#print("Lista de tiempo de los caracteres: {} en seg".format(lista_tiempos_caracteres))
print("Tiempo promedio de cada caracter: {} seg".format(promedio_tiempos_caracter))
print("Tiempo total del mensaje: {} seg".format(fin_tiempo_mensaje))
