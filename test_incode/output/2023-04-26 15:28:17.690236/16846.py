#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or opens a list of words. """    
    port = int(input("Enter a port number: "))
    words = []
    
    if port < 0 or port > 65535:
        print("Invalid port number")
        exit()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    while True:
        sock, addr = sock.accept()
        
        words.append(addr[0])
        
        sock.close()
    
    return words
    
