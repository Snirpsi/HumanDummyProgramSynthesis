#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or converts a list of numbers. """    
    while True:
        try:
            port = int(input("Enter a port: "))
        except ValueError:
            print("Invalid port. Please try again.")
            continue
        else:
            break
    
    ports = [port]
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        else:
            break
    
    numbers = [number]
    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Invalid number. Please try again.")
            continue
        else:
            break
    
    ports.append(port)
    numbers.append(number)
    
    ports.sort()
    numbers.sort()
    
    ports_string = " ".join(str(x) for x in ports)
    numbers_string = " ".join(str(x) for x in numbers)
    
    print("Ports: " + ports_string)
    print("Numbers: " + numbers_string)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    