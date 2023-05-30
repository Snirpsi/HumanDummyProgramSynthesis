#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line.split(' '))
    
    words.sort()
    
    word_to_number = {}
    for word in words:
        word_to_number[word[0]] = word[1]
    
    numbers_to_word = {}
    for number in word_to_number:
        numbers_to_word[word_to_number[number]] = number
    
    words = []
    for number in numbers_to_word:
        words.append(numbers_to_word[number])
    
    sys.stdout.write(' '.join(words))
    
    