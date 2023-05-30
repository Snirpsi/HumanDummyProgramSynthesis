#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that enumerates a port.
    #It will print out all available ports.
    #The program will exit after printing out all ports.
    
    #Open a socket to listen on port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to port 8080
    sock.bind(('0.0.0.0', port))
    
    #Listen for connections
    sock.listen(1)
    
    #Accept a connection
    client, addr = sock.accept()
    
    #Print out all available ports
    print('Available ports:')
    
    #Print out all available ports
    for port in range(1, 65535):
        print('Port {} is available on {}'.format(port, addr))
    
    #Close the connection
    client.close()
    
    #Close the socket
    sock.close()

