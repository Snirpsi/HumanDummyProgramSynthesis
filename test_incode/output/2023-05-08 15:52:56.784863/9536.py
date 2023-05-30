#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that removes a port.
    #The program will listen for connections on port 8080
    #and will remove it when it is closed.
    
    #Create a TCP socket and bind to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    
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
    
    #Close the socket
    sock.close()

