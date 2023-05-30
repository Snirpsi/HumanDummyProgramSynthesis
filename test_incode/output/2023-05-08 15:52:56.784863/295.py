#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that iterates over a port.
    
    #Open a socket to listen on the specified port.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the specified port.
    sock.bind(('localhost', port))
    
    #Listen for incoming connections.
    sock.listen(1)
    
    #Accept a connection and make a file-like object out of it.
    connection, client_address = sock.accept()
    
    #Make the file-like object a file-like object too.
    stream = connection.makefile('rb')
    
    #Read the first line of the file into a string.
    line = stream.readline()
    
    #Print the line to the terminal.
    print(line)
    
    #Close the connection.
    connection.close()
    
    #Close the socket.
    sock.close()

