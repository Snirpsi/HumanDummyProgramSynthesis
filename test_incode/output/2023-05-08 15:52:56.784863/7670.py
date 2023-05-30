#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that returns a port.
    
    #Create a server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', port))
    server.listen(5)
    
    #Accept connections
    client, address = server.accept()
    
    #Receive the message
    message = client.recv(1024)
    
    #Send the message
    client.send(message)
    
    #Close the connection
    client.close()
    
    #Close the server
    server.close()

