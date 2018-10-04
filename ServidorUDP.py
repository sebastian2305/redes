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
            # data = self.conn.recv(2048)
            # data1 = data.decode('utf-8')

            # if data1 != 'Preparado para recibir':
            # print('El Cliente no esta preparado para recibir')
            # print_lock.release()
            # elif data1 == 'Preparado para recibir':
            # print('Cliente preparado para recibir')

            # s.acquire()

            # Tamanio del archivo
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

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 222
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    # while True:
    # print("socket binded to post", port)

    # put the socket into listening mode

    print("socket is listening")

    # a forever loop until client wants to exit

    while numClientes < ClientCount:

        # establish connection with client
        c, addr = s.accept()
        # lock acquired by client
        # print_lock.acquire()
        # print('Connected to :', addr[0], ':', addr[1])

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