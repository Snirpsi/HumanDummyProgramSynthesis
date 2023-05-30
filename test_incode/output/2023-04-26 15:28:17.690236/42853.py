#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words = list(set(words))
    
    word_count = len(words)
    
    word_count_by_letter = {}
    for word in words:
        word_count_by_letter[word] = word_count_by_letter.get(word, 0) + 1
    
    letter_count_by_word = {}
    for letter in word_count_by_letter:
        letter_count_by_word[letter] = letter_count_by_word.get(letter, 0) + 1
    
    letter_count_by_letter = sorted(letter_count_by_word.items(), key=lambda item: item[1], reverse=True)
    
    letter_count_by_word = sorted(letter_count_by_letter.items(), key=lambda item: item[1], reverse=True)
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[:10]
    
    letter_count_by_word = letter_count_by_word[:10]
    
    letter_count_by_letter = letter_count_by_letter[: