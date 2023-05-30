#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that removes a port.
    #This program is intended to be run from the command line.
    #The program will listen for connections on port 8080 and will then
    #remove that port from the list of ports.
    
    #Create a socket to listen for connections.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #Bind the socket to the port
    sock.bind(('', port))
    
    #Listen for incoming connections
    sock.listen(1)
    
    #Now that we have an active connection,
    #we can start listening for new connections.
    while True:
        #Wait for a connection
        conn, addr = sock.accept()
        
        #Receive the message and print it back
        data = conn.recv(1024)
        print(data)
        
        #Close the connection
        conn.close()
        
        #Remove the port from the list of ports.
        sock.close()

