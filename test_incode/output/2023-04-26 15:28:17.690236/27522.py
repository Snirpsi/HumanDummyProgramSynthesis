#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports and removes a port. """    
    ports = open('/proc/net/tcp').read().splitlines()
    for port in ports:
        if port.startswith('tcp'):
            subprocess.call(['sudo', 'tcpdump', '-i', 'eth0', '-n', '-p', port, '-s', '