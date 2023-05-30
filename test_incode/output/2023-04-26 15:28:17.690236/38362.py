#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words or adds numbers. """    
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    while True:
        print(words)
        
        choice = input('Do you want to add another word? [y/n] ')
        
        if choice.lower() == 'y':
            words.append('ten')
            
        elif choice.lower() == 'n':
            break
        
        else:
            print('Invalid input')
            
    print('Done')
    
