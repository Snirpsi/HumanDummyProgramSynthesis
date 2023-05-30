#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that opens ports.
    
    #Open ports
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        print('Listening on port ' + str(port))
        
    #Accept connections
    while True:
        connection, address = sock.accept()
        print('Connected by', address)
        
        #Receive message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection
        connection.close()
        
        #Wait for next message
        message = connection.recv(1024)
        
        #Send message
        connection.sendall(message)
        
        #Close connection