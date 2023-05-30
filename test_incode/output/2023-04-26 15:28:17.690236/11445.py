#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or iterates over a list of numbers. """    
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('port', nargs='?', type=int, help='The port to iterate over')
    args = parser.parse_args()
    port = args.port
    
    ports = [port]
    
    while True:
        ports.append(port)
        port += 1
        
        if port == len(ports):
            break
    
    for port in ports:
        print(port)
    
