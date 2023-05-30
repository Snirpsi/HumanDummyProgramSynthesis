#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that removes all ports.
    while True:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('',port))
            sock.listen(1)
            sock.close()
        ports = ports[:]
        
    #A loop that reads data from all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A loop that reads data from all ports and writes data to all ports.
    while True:
        sock, addr = sock.accept()
        data = sock.recv(1024)
        sock.sendall(data)
        sock.close()
        
    #A 