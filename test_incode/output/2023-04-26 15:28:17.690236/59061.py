#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or returns a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        
        if number > 0 and number < 10:
            print(str(number))
        else:
            words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            
            for word in words:
                print(word)
    else:
        print("Usage: python number_words.py <number>")
        
