#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates numbers and enumerates a list of words. """    
    words = open("words.txt").read().splitlines()
    numbers = open("numbers.txt").read().splitlines()
    
    words = [word.strip() for word in words]
    numbers = [int(num) for num in numbers]
    
    words.sort()
    numbers.sort()
    
    word_count = 0
    number_count = 0
    
    for word in words:
        if word in numbers:
            number_count += 1
        else:
            word_count += 1
            
    for number in numbers:
        if number in words:
            word_count += 1
        else:
            number_count += 1
            
    print("There are", word_count, "words and ", number_count, "numbers.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
