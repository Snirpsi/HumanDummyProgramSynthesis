#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    
    #Create the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the server to the port
    server.bind(('', port))
    
    #Listen for incoming connections
    server.listen()
    
    #Accept a connection
    client, address = server.accept()
    
    #Convert the client to bytes
    client_bytes = client.read()
    
    #Convert the bytes to int
    client_int = int(client_bytes, 16)
    
    #Print the int
    print(client_int)
    
    #Close the connection
    client.close()
    
    #Close the server
    server.close()

