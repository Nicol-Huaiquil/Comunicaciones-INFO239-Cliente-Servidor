import socket
import time
import statistics

def CRC(caracter):
    caracter_en_binario = ' '.join(format(ord(x), 'b') for x in caracter)
    if(caracter_en_binario[-1] == "0"):
        #par
        caracter_con_bandera = caracter_en_binario + "0"
    else:
        #impar
        caracter_con_bandera = caracter_en_binario + "1"
    return caracter_con_bandera


msgFromClient       = input("Escriba su nombre: ")
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Crear un socket UDP en el lado del cliente
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(2)

print("Intentando enviar mensaje")
lista_tiempos_caracteres = []
mensaje = ""
caracteres_perdidos = 0
inicio_tiempo_mensaje = time.time()
for i in range (len(msgFromClient)):
    bytesToSend = CRC(msgFromClient[i])
    bytesToSend =bytesToSend.encode('ascii')
    inicio_tiempo_caracter = time.time()
    # Envia al servidor usando el socket UDP creado
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("Caracter {} enviado".format(msgFromClient[i]))

    booleano = True
    while(booleano):
        try:
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        except:
            caracteres_perdidos+=1
            print("Ha expirado el tiempo de espera, reenviando")
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            
        else:
            fin_tiempo_caracter = time.time()
            fin_tiempo_caracter = fin_tiempo_caracter - inicio_tiempo_caracter
            lista_tiempos_caracteres.append(round(fin_tiempo_caracter, 2))
            print("Caracter aceptado")
            booleano = False

    mensaje_binario = msgFromServer[0].decode()
    mensaje += "".join([chr(int(binary, 2)) for binary in mensaje_binario.split(" ")])

fin_tiempo_mensaje = time.time()
fin_tiempo_mensaje = round(fin_tiempo_mensaje - inicio_tiempo_mensaje, 2)

promedio_tiempos_caracter = round(statistics.mean(lista_tiempos_caracteres), 2)
print("Mensaje del servidor: {}".format(mensaje))
#print("Lista de tiempo de los caracteres: {} en seg".format(lista_tiempos_caracteres))
print("Tiempo promedio de cada caracter: {} seg".format(promedio_tiempos_caracter))
print("Caracteres perdidos: {}".format(caracteres_perdidos))
print("Tiempo total del mensaje: {} seg".format(fin_tiempo_mensaje))
