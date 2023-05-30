#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens numbers or converts words. """    
    
    numbers = open('numbers.txt', 'r')
    words = open('words.txt', 'r')
    
    numbers = numbers.readlines()
    words = words.readlines()
    
    numbers = filter(None, numbers)
    words = filter(None, words)
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, numbers))
    words = map(str.strip, words)
    
    numbers.sort()
    words.sort()
    
    numbers = ''.join(numbers)
    words = ''.join(words)
    
    numbers.close()
    words.close()
    
    numbers = numbers.split('\n')
    words = words.split('\n')
    
    numbers = list(map(int, number