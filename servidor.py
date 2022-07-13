import socket
import random

def aceptar():
    perdida = random.randint(0,100)
    if(perdida >30):
        return True
    else:
        return False

def xor(dividendo, divisor ):
    a = int(dividendo[1:],2)^int(divisor[1:],2)
    b = '{0:0{1}b}'.format(a,len(divisor)-1)
    return b
 
def crc(data,key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    
    pick = len(key)
    tmp = data[0: pick]
 
    while pick < len(data):
        if tmp[0] == '1':
            tmp = xor(key, tmp) + data[pick]
        else:
            tmp = xor('0'*pick, tmp) + data[pick]
        pick += 1
        
    if tmp[0] == '1':
        tmp = xor(key, tmp)
    else:
        tmp = xor('0'*pick, tmp)
 
    ans = tmp
    temp = "0" * (len(key) - 1)
    if ans == temp:
        return True
    else:
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
        message = bytesAddressPair[0].decode()
        address = bytesAddressPair[1]
        clientMsg = "Mensaje del cliente:{}".format(message)
        clientIP  = "IP del cliente:{}".format(address)
        print(clientMsg)
        print(clientIP)
        
        print("Link ocupado")
        key = '1011'
        if(aceptar() and crc(message,key)):
            message = message[0:-(len(key)-1)].encode()
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
        

