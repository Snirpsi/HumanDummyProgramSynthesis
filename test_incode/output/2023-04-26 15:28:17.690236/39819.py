#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or iterates over numbers. """    
    
    ports = range(1023)
    
    for port in ports:
        print("Opening port {}".format(port))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            
            print("Port {} is open!".format(port))
            
            conn, addr = sock.accept()
            
            print("Connected by", addr)
            
            conn.send("Hello, World!".encode())
            conn.close()
            
        except socket.error:
            print("Port {} is closed!".format(port))
            
    
