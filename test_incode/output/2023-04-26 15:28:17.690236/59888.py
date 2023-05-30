#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port and stores words. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(5)
    
    while True:
        client, addr = sock.accept()
        
        data = client.recv(1024)
        
        words.append(data)
        
        client.close()
    
    sock.close()
    
    print(words)
    
