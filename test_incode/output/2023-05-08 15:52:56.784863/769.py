#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that stores a port.
    
    #Create a socket and bind to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    #Accept connection and print out message
    while True:
        client, addr = sock.accept()
        print('Client connected from', addr)
        
        #Receive message from client
        data = client.recv(1024)
        print('Received message:', data.decode())
        
        #Close connection
        client.close()
        
        #Break loop
        break

