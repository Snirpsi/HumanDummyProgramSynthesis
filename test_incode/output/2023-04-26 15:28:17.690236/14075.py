#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers and opens a port. """    
    port = int(input("Enter the port number: "))
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(1)
    
    sock, addr = sock.accept()
    
    numbers = []
    
    while True:
        data = sock.recv(1024)
        numbers.append(data)
        
        if data:
            sock.send(data)
        else:
            break
    
    sock.close()
    
    return numbers

