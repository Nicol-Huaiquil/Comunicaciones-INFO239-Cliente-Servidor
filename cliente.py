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
mensaje = ""
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
            # Funciona para reiniciar el servidor pero cambia dirección IP del cliente (soluciona problema de cola)
            # Llega el nombre bien con N clientes
            # Falla cuando el servidor rechaza algún caracter, (servidor actualmente en True)
            UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # Si se comenta problema con cola
            UDPClientSocket.settimeout(2)
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            
        else:
            print("Caracter aceptado")
            booleano = False

    mensaje += msgFromServer[0].decode()
    
print(mensaje)
msg = "Mensaje del servidor {}".format(msgFromServer[0])
print(msg)