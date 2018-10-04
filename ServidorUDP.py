#UDPserver.py
#!/usr/bin/python
import socket
import hashlib
from datetime import datetime
from threading import Thread

ClientCount = int(input("Especifique cuantos clientes quiere en simultaneo\n" ))
ConnectedClients = []
numClientes = 0
def millis(start_time):
    dt = datetime.now() - start_time
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms

class Client(Thread):
        def __init__(self, conn, addr):
            Thread.__init__(self)
            self.conn = conn
            self.addr = addr

        def run(self):
            # data received from client
            m = hashlib.sha256();
            data = self.conn.recv(2048)
            datoTamanio = data.decode('utf-8')

            # reverse the given string from client
            if datoTamanio == '250':
                with open('250.webm', 'rb') as dd:
                    contenido = dd.read()
                    m.update(contenido)
                    dig = m.digest()
                    self.conn.send(dig)
                    self.conn.send(contenido)

            else:
                with open('500.mp4', 'rb') as dd:
                    contenido = dd.read()
                    m.update(contenido)
                    dig = m.digest()
                    self.conn.send(dig)
                    self.conn.send(contenido)
            print('En Cliente recibio el archivo correctamente')
            self.conn.close()

def Main():
    global ConnectedCount
    global numClientes
    host = ''
    port = 222
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("socket is listening")

    while numClientes < ClientCount:

        # esperar a recibir "Preparado para recibir"
        resp = c.recv(1024)
        if (resp.decode("utf-8") == "Preparado para recibir"):
            # create a new thread and add it to the created list
            c = Client(c, addr)
            ConnectedClients.append(c)
            numClientes += 1

    print("Llegaron todos los clientes")
    for x in ConnectedClients:
        x.start()
    s.close()


if __name__ == '__main__':
    Main()