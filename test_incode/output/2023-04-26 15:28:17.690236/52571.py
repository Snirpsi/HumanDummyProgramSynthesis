#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words. """    
    words = []
    with open('words.txt', 'r') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    word_to_number = {}
    for word in words:
        word_to_number[word] = len(words)
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 0}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 0}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 1}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 1}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 2}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 2}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 3}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 3}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 4}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 4}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 5}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 5}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 6}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 6}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 7}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 7}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 8}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 8}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 9}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 9}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 10}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 10}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 11}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v == 11}
    
    word_to_number = {k:v for k, v in word_to_number.items() if v > 12