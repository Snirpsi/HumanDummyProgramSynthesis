#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A function that opens a port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    #A function that accepts a connection and prints it.
    while True:
        connection, address = sock.accept()
        print('Connected by', address)
        
        #A function that reads a line from the connection.
        while True:
            data = connection.recv(1024)
            if not data:
                break
            
            #A function that prints the data.
            print(data.decode())
        
        #A function that closes the connection.
        connection.close()
        
        #A function that closes the port.
        sock.close()
        
        #A function that closes the socket.
        sock.close()

