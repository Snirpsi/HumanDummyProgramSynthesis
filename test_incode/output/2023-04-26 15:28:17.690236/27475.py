#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports or calculates numbers. """    
    while True:
        ports = open('/proc/net/tcp').read().splitlines()
        for port in ports:
            port = int(port)
            if port > 0 and port < 65535:
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is closed')
        time.sleep(1)
