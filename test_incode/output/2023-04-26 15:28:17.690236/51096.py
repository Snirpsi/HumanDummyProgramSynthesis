#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits and multiplyes a list of words. """    
    fruits = ['apple', 'banana', 'cherry']
    words = ['apples', 'bananas', 'cherries']
    
    while True:
        fruits_open = fruits.pop(0)
        words_open = words.pop(0)
        
        print('Opening fruit ' + fruits_open)
        print('Opening word ' + words_open)
        
        fruits.append(fruits_open)
        words.append(words_open)
        
        print('Fruit ' + fruits_open + ' is now ' + fruits)
        print('Word ' + words_open + ' is now ' + words)
        
        time.sleep(1)
        
