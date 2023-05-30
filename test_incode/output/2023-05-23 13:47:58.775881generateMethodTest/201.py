#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A endless loop that iterates over all ports.
    while True:
        for port in ports:
            #Create a TCP socket and bind to port 8000.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            #Accept a connection and print out the IP address and port number.
            conn, addr = sock.accept()
            print('Connected by', addr)
            
            #Receive a message from the client.
            data = conn.recv(1024)
            print('Received', repr(data))
            
            #Send a message back to the client.
            conn.sendall('Hello, world!\n')
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to connect.
            conn.recv(1024)
            
            #Close the connection.
            conn.close()
            
            #Wait for another client to 