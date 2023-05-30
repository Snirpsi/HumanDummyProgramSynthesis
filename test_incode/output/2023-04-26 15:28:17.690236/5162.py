#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers and iterates over a list of words. """    
    words = ['cat', 'dog', 'bird', 'cat', 'dog', 'bird']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Remove all numbers from words and iterate over them
    numbers_removed = [i for i in numbers if i not in words]
    
    # Print the result
    print('Numbers removed: {}'.format(numbers_removed))
    
    # Iterate over words and print each word and its corresponding number
    for word in words:
        print('{}: {}'.format(word, numbers_removed))
    
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        print('{}: {}'.format(number, words[number]))
    
    # Iterate over words and print each word and its corresponding number
    for word in words:
        for number in numbers_removed:
            print('{}: {}'.format(word, number))
        
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        for word in words:
            print('{}: {}'.format(number, word))
        
    # Iterate over words and print each word and its corresponding number
    for word in words:
        for number in numbers_removed:
            print('{}: {}'.format(word, number))
        
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        for word in words:
            print('{}: {}'.format(number, word))
        
    # Iterate over words and print each word and its corresponding number
    for word in words:
        for number in numbers_removed:
            print('{}: {}'.format(word, number))
        
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        for word in words:
            print('{}: {}'.format(number, word))
        
    # Iterate over words and print each word and its corresponding number
    for word in words:
        for number in numbers_removed:
            print('{}: {}'.format(word, number))
        
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        for word in words:
            print('{}: {}'.format(number, word))
        
    # Iterate over words and print each word and its corresponding number
    for word in words:
        for number in numbers_removed:
            print('{}: {}'.format(word, number))
        
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        for word in words:
            print('{}: {}'.format(number, word))
        
    # Iterate over words and print each word and its corresponding number
    for word in words:
        for number in numbers_removed:
            print('{}: {}'.format(word, number))
        
    # Iterate over numbers and print each number and its corresponding word
    for number in numbers:
        for word in words:
            print('{}: {}'.format(number, word))
        
    # 