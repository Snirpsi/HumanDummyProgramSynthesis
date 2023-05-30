#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = ['hello', 'world', 'python']
    multiplied = [words[i] * words[i + 1] for i in range(len(words) - 1)]
    print(multiplied)
    
