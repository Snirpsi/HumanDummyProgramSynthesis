#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    #It will listen for connections on port 8080 and will convert them into 
    #a port that you can use.
    
    #Start a server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    server.bind(('localhost', port))
    
    #Listen for incoming connections
    server.listen(5)
    
    #Wait for a connection
    client, address = server.accept()
    
    #Convert the client into a port number
    port = client.getsockname()[1]
    
    #Close the connection
    client.close()
    
    #Print the port number
    print(port)
    
    #Close the server
    server.close()

