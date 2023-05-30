#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores fruits and enumerates a port. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    # enumerate all possible ports
    ports = list(itertools.permutations(fruits, 2))
    
    # enumerate all possible fruits
    fruits = list(itertools.product(*fruits))
    
    # print all possible fruits
    for fruit in fruits:
        print(''.join(fruit))
    
    # print all possible ports
    for port in ports:
        print(''.join(port))
        
    # print all possible fruits with two ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
    
    # print all possible fruits with three ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
    
    # print all possible fruits with four ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        
    # print all possible fruits with five ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        
    # print all possible fruits with six ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        
    # print all possible fruits with seven ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        
    # print all possible fruits with eight ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        
    # print all possible fruits with nine ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        print(''.join(port))
        
    # print all possible fruits with ten ports
    for fruit in fruits:
        print(''.join(fruit))
        print(''.join(port))
        print(''.join(