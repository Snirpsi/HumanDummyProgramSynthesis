#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or removes a list of numbers. """    
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'exit':
            break
        
        if word in ['exit', 'quit']:
            break
        
        if word.isdigit():
            number = int(word)
            
            if number > 0 and number <= 10:
                print(number)
            else:
                print('Invalid number')
        else:
            print('Invalid word')
            
    print('Goodbye!')
