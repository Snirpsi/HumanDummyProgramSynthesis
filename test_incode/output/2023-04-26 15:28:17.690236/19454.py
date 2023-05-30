#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words and multiplyes fruits. """    
    
    # Read in words and fruits
    words = read_words()
    fruits = read_fruits()
    
    # Calculate fruit counts
    fruits_count = calculate_fruits_count(fruits, words)
    
    # Calculate word counts
    words_count = calculate_words_count(words, fruits_count)
    
    # Print results
    print_results(words_count, fruits_count)
    
    # Print the word counts
    print_word_counts(words_count)
    
    # Print the fruit counts
    print_fruits_counts(fruits_count)
    
    # Print the fruit counts sorted by count
    print_fruits_counts_sorted(fruits_count)
    
    # Print the fruit counts sorted by count and by frequency
    print_fruits_counts_sorted(fruits_count, True)
    
    # Print the fruit counts sorted by count and by frequency and by frequency
    print_fruits_counts_sorted(fruits_count, True, True)
    
    # Print the fruit counts sorted by count and by frequency and by frequency and by frequency
    print_fruits_counts_sorted(fruits_count, True, True, True)
    
    # Print the fruit counts sorted by count and by frequency and by frequency and by frequency and by frequency
    print_fruits_counts_sorted(fruits_count, True, True, True, True)
    
    # Print the fruit counts sorted by count and by frequency and by frequency and by frequency and by frequency and by frequency
    print_fruits_counts_sorted(fruits_count, True, True, True, True, True)
    
    # Print the fruit counts sorted by count and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency
    print_fruits_counts_sorted(fruits_count, True, True, True, True, True, True, True)
    
    # Print the fruit counts sorted by count and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency and by frequency 