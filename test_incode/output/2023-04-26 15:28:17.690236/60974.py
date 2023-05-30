#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and converts words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    words_by_letter = {}
    for word in words:
        letter = word[0]
        if letter not in words_by_letter:
            words_by_letter[letter] = []
        words_by_letter[letter].append(word)
    
    for letter in words_by_letter:
        print(letter)
        for word in words_by_letter[letter]:
            print(word)
    
