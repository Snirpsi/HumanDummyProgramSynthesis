#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that opens ports.
    
    #Open ports
    for port in ports:
        
        #Open port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        
        #Wait for connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info
        print('Connected by', addr)
        
        #Receive data
        data = conn.recv(1024)
        
        #Send data
        conn.sendall(data)
        
        #Close connection
        conn.close()
        
        #Wait for next connection
        conn, addr = sock.accept()
        
        #Print connection info


