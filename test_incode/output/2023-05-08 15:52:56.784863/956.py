#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that calculates a port.
    
    #Create a socket and bind it to the port number.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    
    #Start listening for connections.
    sock.listen(1)
    
    #Accept a connection from the client.
    client, addr = sock.accept()
    
    #Receive a message from the client.
    message = client.recv(1024)
    
    #Send the message back to the client.
    client.send(message)
    
    #Close the connection.
    client.close()
    
    #Close the socket.
    sock.close()

