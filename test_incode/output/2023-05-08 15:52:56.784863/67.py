#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that prints a port.
    
    #Create a TCP socket and bind to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    
    #Start listening for connections
    sock.listen(1)
    
    #Accept a connection
    client, addr = sock.accept()
    
    #Receive a message
    message = client.recv(1024)
    
    #Send the message back to the client
    client.send(message)
    
    #Close the connection
    client.close()

