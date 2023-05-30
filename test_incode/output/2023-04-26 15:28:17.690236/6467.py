#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    
    ports = range(1,65535)
    
    while True:
        for port in ports:
            print("Starting port {} ...".format(port))
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('localhost', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.send("Hello World!")
            conn.close()
            
            print("Port {} closed".format(port))
            
        time.sleep(1)
        
