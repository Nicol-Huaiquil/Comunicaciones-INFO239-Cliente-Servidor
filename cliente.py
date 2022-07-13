import socket
import time
import statistics

def xor(dividendo, divisor ):
    a = int(dividendo[1:], 2) ^ int(divisor[1:], 2)
    b = '{0:0{1}b}'.format(a, len(divisor) - 1)
    return b

def crc(dato):
    dato = ' '.join(format(ord(x), 'b') for x in dato)
    key = '1011'
    bits = (len(key)-1) * '0'
    dato_mas_bits = dato + bits
    
    tmp = dato_mas_bits[0 : len(key)]
    contador =  len(key)

    while contador < len(dato_mas_bits):
        if tmp[0] == '1':
            tmp = xor(key, tmp) + dato_mas_bits[contador]
        else: 
            tmp = xor('0'*contador, tmp) + dato_mas_bits[contador]
        contador += 1
 
    if tmp[0] == '1':
        tmp = xor(key, tmp)
    else:
        tmp = xor('0'*contador, tmp)
    resto = tmp
    crc = dato + resto
    return crc


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
    bytesToSend = crc(msgFromClient[i])
    bytesToSend = bytesToSend.encode()
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
