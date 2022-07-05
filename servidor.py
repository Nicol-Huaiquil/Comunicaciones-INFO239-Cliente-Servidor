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
    #tiempo = random.randint(1,3)   # con 0.5 da error 
    tiempo = random.randint(500,3000)
    tiempo=tiempo/1000
    time.sleep(tiempo)


localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Datagram Aceptado"
bytesToSendA        = str.encode(msgFromServer)

#msgFromServer       = "Datagram Rechazado"
#bytesToSendR        = str.encode(msgFromServer)

# Crear un socket de datagrama
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Vinculando con dirección IP
UDPServerSocket.bind((localIP, localPort))
print("Link Available")

# Escuchando los datagramas entrantes

while(True):
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Mensaje del cliente:{}".format(message)
        #clientIP  = "IP del cliente:{}".format(address)
        
        print(clientMsg)
        #print(clientIP)

        print("Link ocupado")

        #if(aceptar()):
        if(True):
            print("Caracter aceptado")
    
            tiempo_respuesta()

            # Enviando respuesta al cliente
            UDPServerSocket.sendto(bytesToSendA, address)

        else:
            print("Caracter rechazado")
            # Enviando respuesta al cliente
            #UDPServerSocket.sendto(bytesToSendR, address)


        print("Link disponible")
        print()
    except:
        pass
        

