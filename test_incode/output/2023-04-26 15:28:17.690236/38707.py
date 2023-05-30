#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits. """    
    fruits = ['apple', 'banana', 'orange', 'kiwi']
    
    while True:
        fruits.remove('apple')
        fruits.remove('banana')
        fruits.remove('orange')
        fruits.remove('kiwi')
        
        print('Fruits:', fruits)
        
        time.sleep(1)
        
