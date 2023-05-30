#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that prints a port.
    #The port is then used to open a socket to listen for connections.
    
    #Create a socket to listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    sock.bind(('0.0.0.0', port))
    
    #Listen for connections
    sock.listen(1)
    
    #Accept a connection
    connection, address = sock.accept()
    
    #Receive the message and print it
    data = connection.recv(1024)
    print(data)
    
    #Close the connection
    connection.close()
    
    #Close the socket
    sock.close()

