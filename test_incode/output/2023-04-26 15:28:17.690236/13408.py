#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port or stores user input. """    
    
    port = int(input("Enter a port number to listen on: "))
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(1)
    
    print("Listening on port {}".format(port))
    
    while True:
        connection, address = server.accept()
        print("Connected by", address)
        
        data = connection.recv(1024)
        print("Received:", data.decode())
        
        connection.close()
    
    server.close()
    
