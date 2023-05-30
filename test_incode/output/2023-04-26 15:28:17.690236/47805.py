#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports or opens numbers. """    
    ports = []
    numbers = []
    
    try:
        ports = open('/proc/net/tcp').read().splitlines()
        numbers = open('/proc/net/udp').read().splitlines()
    except FileNotFoundError:
        print('No TCP ports found')
    except PermissionError:
        print('No UDP ports found')
        
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', int(port)))
            sock.listen(1)
            sock.settimeout(1)
            sock, addr = sock.accept()
            sock.settimeout(1)
            sock.close()
            
        except socket.timeout:
            print('Timeout on port {}'.format(port))
        except socket.error:
            print('Error on port {}'.format(port))
        
    for number in numbers:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(number, ('127.0.0.1', int(number)))
            sock.close()
        except socket.error:
            print('Error on port {}'.format(number))
        
    print('Done')
<|/ file source=github ext=.py |>