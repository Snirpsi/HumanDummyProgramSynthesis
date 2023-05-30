#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that prints a port.
    
    #Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    sock.bind(("", port))
    
    #Listen for incoming connections
    sock.listen(1)
    
    #Accept a connection
    client, address = sock.accept()
    
    #Receive the message and print it
    message = client.recv(1024)
    print(message)
    
    #Close the connection
    client.close()
    
    #Close the socket
    sock.close()

