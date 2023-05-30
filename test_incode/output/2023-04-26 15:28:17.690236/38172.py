#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or multiplyes all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 0:
        ports = range(1,65535)
    
    for port in ports:
        print("Opening port {}".format(port))
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("", port))
            
            sock.send("*\n")
            
            while True:
                data = sock.recv(1024)
                
                if data:
                    print(data.decode("utf-8"))
                else:
                    break
            
            sock.close()
        except socket.error as e:
            print("Socket error: {}".format(e))
    
    print("Done")
    
    
