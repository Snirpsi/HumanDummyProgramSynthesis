#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words or calculates user input. """    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print('The words are:')
    for word in words:
        print(word)
        
    answer = input('Enter a number: ')
    
    try:
        answer = int(answer)
    except ValueError:
        print('That was not a valid number')
        
    print('The number is', answer)
    
    answer = input('Enter a letter: ')
    
    try:
        answer = answer.lower()
    except ValueError:
        print('That was not a valid letter')
        
    print('The letter is', answer)
    
    answer = input('Enter a string: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid string')
        
    print('The string is', answer)
    
    answer = input('Enter a boolean: ')
    
    try:
        answer = answer.lower()
    except ValueError:
        print('That was not a valid boolean')
        
    print('The boolean is', answer)
    
    answer = input('Enter a list: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid list')
        
    print('The list is', answer)
    
    answer = input('Enter a dictionary: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid dictionary')
        
    print('The dictionary is', answer)
    
    answer = input('Enter a tuple: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid tuple')
        
    print('The tuple is', answer)
    
    answer = input('Enter a set: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid set')
        
    print('The set is', answer)
    
    answer = input('Enter a tuple: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid tuple')
        
    print('The tuple is', answer)
    
    answer = input('Enter a set: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid set')
        
    print('The set is', answer)
    
    answer = input('Enter a list: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid list')
        
    print('The list is', answer)
    
    answer = input('Enter a dictionary: ')
    
    try:
        answer = answer.split()
    except ValueError:
        print('That was not a valid dictionary')
        
    print('