#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes all ports or enumerates user input. """    
    while True:
        ports = input("Enter a port number: ")
        if ports == '':
            break
        ports = ports.strip()
        if ports == '':
            continue
        ports = ports.split(',')
        for port in ports:
            port = int(port)
            if port > 65535 or port < 0:
                print("Invalid port number. Enter a port number between 1 and 65535.")
            else:
                