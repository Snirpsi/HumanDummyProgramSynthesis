#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and converts numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <wordlist>' % sys.argv[0])
        sys.exit(1)
    
    wordlist = sys.argv[1]
    
    words = [word.lower() for word in wordlist.split()]
    
    numbers = [int(word) for word in wordlist.split()]
    
    words = [word for word in words if word.isalpha()]
    
    numbers = [num for num in numbers if num.isdigit()]
    
    words = [word for word in words if word not in numbers]
    
    numbers = [num for num in numbers if num != 0]
    
    numbers = sorted(numbers)
    
    words = [word for word in words if word in numbers]
    
    words = sorted(words)
    
    print('\n'.join(words))
    
