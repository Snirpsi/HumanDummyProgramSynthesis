#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    
    #Create a socket to listen on port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    sock.bind(('', port))
    
    #Listen for incoming connections
    sock.listen(1)
    
    #Accept a connection
    client, address = sock.accept()
    
    #Receive the message from the client
    message = client.recv(1024)
    
    #Send the message back to the client
    client.send(message)
    
    #Close the connection
    client.close()
    
    #Close the socket
    sock.close()

