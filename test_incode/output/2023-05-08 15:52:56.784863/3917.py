#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that calculates a port.
    
    #Create a socket and bind to port 8080
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    #Accept connections from clients
    while True:
        conn, addr = sock.accept()
        print('Connected by', addr)
        
        #Receive data from client
        data = conn.recv(1024)
        if not data:
            break
        
        #Send data to client
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
    #Close socket
    sock.close()

