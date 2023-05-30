#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that stores a port.
    
    #Create a socket and bind it to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    
    #Listen for connections
    sock.listen(1)
    
    #Accept a connection
    client, addr = sock.accept()
    
    #Receive a message from the client
    message = client.recv(1024)
    
    #Send the message back to the client
    client.send(message)
    
    #Close the connection
    client.close()

