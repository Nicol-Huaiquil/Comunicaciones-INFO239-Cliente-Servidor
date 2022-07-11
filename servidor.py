import socket
import random

from numpy import true_divide

def aceptar():
    perdida = random.randint(0,100)
    if(perdida >30):
        return True
    else:
        return False

def crc(caracter_bin_con_bandera):
    if(caracter_bin_con_bandera[-2] == caracter_bin_con_bandera[-1]):
        print("CRC correcto")
        return True
    else:
        print("CRC incorrecto")
        return False

def tiempo_respuesta():
    tiempo = random.randint(500,3000)
    tiempo=tiempo/1000
    UDPServerSocket.settimeout(tiempo)

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Datagram Aceptado"
bytesToSendA        = str.encode(msgFromServer)

# Crear un socket de datagrama
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Vinculando con dirección IP
UDPServerSocket.bind((localIP, localPort))
print("Link disponible")

# Escuchando los datagramas entrantes
while(True):
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Mensaje del cliente:{}".format(message)
        clientIP  = "IP del cliente:{}".format(address)
        print(clientMsg)
        print(clientIP)
        
        print("Link ocupado")
        if(aceptar() and crc(message)):
            message = message[0:-1]
            print("Caracter aceptado")
            tiempo_respuesta()
            
            # Enviando respuesta al cliente
            UDPServerSocket.sendto(message, address) 
            
        else:
            print("Caracter rechazado")

        print("Link disponible")
        print()

    except:
        pass
        

