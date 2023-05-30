#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of numbers or iterates over words. """    
    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        number = input('Enter a number: ')
        
        if number.isdigit():
            number = int(number)
            
            if number > len(words):
                print('Sorry, I can\'t go higher than the length of my words.')
                
            else:
                print(words[number])
                
        else:
            print('Sorry, I don\'t understand that number.')
            
