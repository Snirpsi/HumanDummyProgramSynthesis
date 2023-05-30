#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a port and adds user input. """    
    
    port = int(sys.argv[1])
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    while True:
        client, addr = sock.accept()
        
        message = input('Enter a message:')
        
        client.send(message)
        
        