#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or iterates over a list of numbers. """    
    
    words = ['hello', 'world', 'python', 'is', 'a', 'test']
    
    for word in words:
        print(word)
    
    number = 1
    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 1:
            print('Invalid number, try again')
            continue
        
        if number > len(words):
            print('Invalid number, try again')
            continue
        
        if number % 2 == 0:
            print(words[number])
        else:
            print(words[number - 1])
        
