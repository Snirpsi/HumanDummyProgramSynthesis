#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts fruits and converts a port. """    
    fruits = ["apple", "banana", "cherry"]
    fruits_port = {}
    for fruit in fruits:
        fruits_port[fruit] = int(input("Enter a port for " + fruit + ": "))
    
    ports_fruits = {}
    for fruit, port in fruits_port.items():
        ports_fruits[port] = fruit
    
    fruits_port = {}
    for fruit in fruits:
        fruits_port[fruit] = ports_fruits[fruit]
    
    print("\nThe ports available for " + fruits[0] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[1] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[2] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[3] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[4] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[5] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[6] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[7] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[8] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[9] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + fruits[10] + ":")
    for port in ports_fruits.keys():
        print(port + ": " + ports_fruits[port])
    
    print("\nThe ports available for " + 