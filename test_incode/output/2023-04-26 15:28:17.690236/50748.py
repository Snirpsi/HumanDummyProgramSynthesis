#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port or returns user input. """    
    port = None
    while True:
        port = input("Enter a port number: ")
        if port == 'exit':
            break
        else:
            try:
                port = int(port)
                break
            except ValueError:
                print("Invalid port number. Try again.")
                continue
    
    return port
