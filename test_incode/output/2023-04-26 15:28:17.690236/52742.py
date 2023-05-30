#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports and multiplyes user input. """    
    ports = []
    
    while True:
        port = input("Enter a port number: ")
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        ports.append(port)
        
        if len(ports) == 3:
            break
    
    ports = ports * 3
    
    for port in ports:
        print(port)
    
    print("\nDone")
    
