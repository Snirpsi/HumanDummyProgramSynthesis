#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or opens a port. """    
    
    ports = []
    
    for port in range(1,65535):
        ports.append(port)
        
    ports.reverse()
    
    for port in ports:
        print("Starting port {} on {}".format(port, HOST))
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, port))
        sock.shutdown(2)
        
        sock.send("Hello, world!")
        
        sock.close()
    
    print("Done.")
    
