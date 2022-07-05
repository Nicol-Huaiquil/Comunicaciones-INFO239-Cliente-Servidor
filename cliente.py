import socket
import time

def tiempo_espera():
    time.sleep(2)

msgFromClient       = input("Escriba su nombre: ")
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Crear un socket UDP en el lado del cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(2)

print("Intentando enviar mensaje")
for i in range (len(msgFromClient)):
    bytesToSend = str.encode(msgFromClient[i])

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
            print("Caracter aceptado")
            booleano = False

    '''
    booleano = True
    while(booleano):
        if(b"Aceptado" in msgFromServer[0]):
            print("Caracter aceptado")
            booleano = False

        else:
            print("Caracter rechazado")
            print("Ha expirado el tiempo de espera, reenviando")
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            tiempo_espera()
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    '''
    
msg = "Mensaje del servidor {}".format(msgFromServer[0])
print(msg)