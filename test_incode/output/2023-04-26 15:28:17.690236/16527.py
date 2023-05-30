#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words or prints all ports. """    
    ports = find_ports()
    
    if ports:
        print("\n".join(ports))
    else:
        print("No ports found")

<|/ file source=github |>