#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and opens a port. """    
    import sys
    
    port = int(sys.argv[1])
    
    ports = [port]
    
    for arg in sys.argv[2:]:
        ports.append(int(arg))
    
    ports.sort()
    
    for port in ports:
        
        print("Opening port {}".format(port))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("", port))
            
            print("Port {} opened".format(port))
            
            sock.close()
            
        except socket.error:
            print("Port {} not opened".format(port))
            
