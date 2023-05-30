#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that iterates over a port.
    
    #Open a socket and listen on port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
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

