#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores fruits and converts a port. """    
    
    # Create a fruit
    fruit1 = Fruit("apple")
    fruit2 = Fruit("banana")
    
    # Create a port
    port = Port("apple")
    
    # Add fruits and ports
    fruit1.add_port(port)
    fruit2.add_port(port)
    
    # Print the fruits
    print(fruit1)
    print(fruit2)
    
    # Print the ports
    print(port)
    
    # Print the fruits in the port
    print(fruit1.in_port(port))
    print(fruit2.in_port(port))
    
    # Print the ports in the fruit
    print(port.in_fruit(fruit1))
    print(port.in_fruit(fruit2))
    
    # Print the ports in the fruit that are not in the port
    print(port.not_in_fruit(fruit1))
    print(port.not_in_fruit(fruit2))
    
    # Print the ports in the fruit that are not in the port that are not in the fruit
    print(port.not_in_fru