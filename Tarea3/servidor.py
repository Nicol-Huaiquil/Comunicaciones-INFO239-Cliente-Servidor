import socket
import time
import random

def aceptar():
    perdida = random.randint(0,100)
    if(perdida >30):
        return True

    else:
        return False

def tiempo_respuesta():
    tiempo = random.randint(0.5,3)
    time.sleep(tiempo)


localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Datagram Acepted"
bytesToSend         = str.encode(msgFromServer)

# Crear un socket de datagrama
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Vincular a dirección e ip
UDPServerSocket.bind((localIP, localPort))
print("Link Available")

# Escuche los datagramas entrantes
while(True):
    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    #clientMsg = "Mensaje del cliente:{}".format(message)
    print("Link ocupado")

    if(aceptar()):
        print("Caracter aceptado")
        clientMsg = format(message) 
        
        print(clientMsg)

        tiempo = random.randint(1,3)   # con 0.5 da error 
        time.sleep(tiempo)

        # Enviando una respuesta al cliente
        UDPServerSocket.sendto(bytesToSend, address)
    else:
        print("Caracter rechazado")

    print("Link disponible")
        

