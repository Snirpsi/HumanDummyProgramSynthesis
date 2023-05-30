#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that iterates over a port.
    
    #Open a socket to listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    sock.bind(('', port))
    
    #Listen for incoming connections
    sock.listen(10)
    
    #Accept a connection and make a file-like object out of it.
    connection, client_address = sock.accept()
    
    #Make the file-like object into a readable file-like object.
    stream = connection.makefile('rb')
    
    #Print the server address and port number.
    print('Server address:', client_address)
    print('Server port:', port)
    
    #Read a line from the file-like object until we get EOF.
    while True:
        line = stream.readline()
        if not line:
            break
        
        #Print the line to the terminal.
        print(line)
    
    #Close the connection and print a message to the terminal.
    connection.close()
    print('Bye.')

