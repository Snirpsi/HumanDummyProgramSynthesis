#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words and enumerates a list of numbers. """    
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    
    words_and_numbers = zip(words, numbers)
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now:")
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by number:")
    
    words_and_numbers.sort(key=lambda x: x[1])
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by word:")
    
    words_and_numbers.sort(key=lambda x: x[0])
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by number:")
    
    words_and_numbers.sort(reverse=True)
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by word:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x))
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by number:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x[0]))
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by word:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x[0]))
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by number:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x[0]))
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by word:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x[0]))
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by number:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x[0]))
    
    for word, number in words_and_numbers:
        print(word, number)
    
    print("\nThe words and numbers are now sorted by word:")
    
    words_and_numbers.sort(key=lambda x: (len(x), x[0]))
    
    for 