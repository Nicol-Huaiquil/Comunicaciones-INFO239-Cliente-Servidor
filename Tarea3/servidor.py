import socket
import time

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

    #clientMsg = "Mensaje del cliente:{}".format(mensaje)
    print("Link bussy")
    clientMsg = format(message) 
    print(clientMsg)
    time.sleep(30)

    # Enviando una respuesta al cliente
    UDPServerSocket.sendto(bytesToSend, address)
    print("Link Available")