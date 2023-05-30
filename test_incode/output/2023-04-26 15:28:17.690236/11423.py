#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits and prints all ports. """    
    
    fruits = ['apple', 'orange', 'banana', 'cherry']
    
    while True:
        fruits.append(input('Enter fruit name: ').title())
        
        print('Fruit added: ', fruits[-1])
        
        print('Ports left: ', len(fruits))
        
        print('Press enter to exit')
        
        input()
        
