#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and stores numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python word.py <word>')
        exit(1)
    
    word = sys.argv[1]
    
    wordlist = list(word)
    
    wordlist.sort()
    
    numbers = []
    
    for word in wordlist:
        
        number = word
        
        if word[-1] == 's':
            number = number[:-1]
        
        numbers.append(number)
    
    print('\n'.join(numbers))
    
