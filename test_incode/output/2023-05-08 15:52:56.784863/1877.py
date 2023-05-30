#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that prints a port.
    
    #Create a socket and bind to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    
    #Listen for connections
    sock.listen(1)
    
    #Accept a connection
    client, addr = sock.accept()
    
    #Print the client address
    print('Connected by', addr)
    
    #Receive a message
    while True:
        data = client.recv(1024)
        if not data:
            break
        
        #Send the message back to the client
        client.send(data)
    
    #Close the connection
    client.close()

