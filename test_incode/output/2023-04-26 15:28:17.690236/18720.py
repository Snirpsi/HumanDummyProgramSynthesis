#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of words and stores fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = []
    
    while True:
        fruits.append(random.choice(words))
        
        print('The fruit is:', fruits[-1])
        
        time.sleep(1)
        
