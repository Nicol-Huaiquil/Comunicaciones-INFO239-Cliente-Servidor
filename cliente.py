import socket
import time

def tiempo_espera():
    time.sleep(2)

msgFromClient       = "NICOL"
#bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Crear un socket UDP en el lado del cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("Intentando enviar mensaje")
for i in range (len(msgFromClient)):
    bytesToSend = str.encode(msgFromClient[i])

    # Enviar al servidor usando el socket UDP creado
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("Caracter {} enviado".format(msgFromClient[i]))

    tiempo_espera()

    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    booleano = True
    while(booleano):
        if(b"Aceptado" in msgFromServer[0]):
            print("Caracter aceptado")
            booleano = False

        else:
            print("Caracter rechazado")
            print("Reenviando")
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            tiempo_espera()
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
msg = "Mensaje del servidor {}".format(msgFromServer[0])
#print("msgFromServer = ", msgFromServer)
print(msg)