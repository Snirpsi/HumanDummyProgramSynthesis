#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a list of numbers or opens a port. """    
    
    port = None
    
    try:
        port = int(sys.argv[1])
    except:
        print("Usage: python %s <port>" % sys.argv[0])
        
    if port != None:
        
        ports = [port]
        
    else:
        
        ports = range(1,65535)
        
    for port in ports:
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', port))
        sock.listen(1)
        
        print("Listening on port %s" % port)
        
        while True:
            
            client, addr = sock.accept()
            
            data = client.recv(1024)
            
            client.close()
            
            if data:
                
                client.send(data)
                
            else:
                
                client.close()
                
                break
                
        sock.close()
        
        print("Closing socket")
        
    
