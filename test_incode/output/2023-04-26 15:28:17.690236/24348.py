#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and adds a list of numbers. """    
    words = open('words.txt').read().splitlines()
    numbers = open('numbers.txt').read().splitlines()
    
    numbers_words = [int(n) for n in numbers]
    words_numbers = [words[n] for n in numbers_words]
    
    words_numbers_pairs = [words_numbers, numbers_words]
    
    words_numbers_pairs_sorted = sorted(words_numbers_pairs, key=lambda x: x[0])
    
    words_numbers_pairs_sorted.reverse()
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][1])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][0])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][2])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][3])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][4])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][5])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][6])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][7])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][8])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][9])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][10])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][11])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][12])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][13])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][14])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][15])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][16])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][17])
    
    words_numbers_pairs_sorted.insert(0,words_numbers_pairs_sorted[0][18])
    
    words_