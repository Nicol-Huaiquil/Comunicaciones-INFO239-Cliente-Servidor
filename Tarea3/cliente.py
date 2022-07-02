import socket
import time
from xmlrpc.client import Boolean

def tiempo_espera():
    time.sleep(2)

msgFromClient       = "Using Link Client 1"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Crear un socket UDP en el lado del cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviar al servidor usando el socket UDP creado
print("Intentando enviar")

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
tiempo_espera()
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

'''
booleano = True
while(booleano):
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    tiempo_espera()
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    if( == -1):
        print("Reenviando")
    else:
        booleano = False
'''

print(msgFromServer)

msg = "Mensaje del servidor {}".format(msgFromServer[0])
print(msg)