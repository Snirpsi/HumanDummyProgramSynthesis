#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    
    # Get the command line arguments.
    args = sys.argv[1:]
    
    # Get the file name.
    filename = args[0]
    
    # Open the file.
    file = open(filename, 'r')
    
    # Get the list of words.
    words = file.read().splitlines()
    
    # Close the file.
    file.close()
    
    # Print the list of words.
    print(words)
    
    # Calculate the word length.
    word_length = len(words)
    
    # Print the word length.
    print(word_length)
    
    # Calculate the average word length.
    word_length_average = word_length / len(words)
    
    # Print the average word length.
    print(word_length_average)
    
    # Calculate the word length.
    word_length_median = word_length / 2
    
    # Print the word length.
    print(word_length_median)
    
    # Calculate the word length.
    word_length_mode = word_length
    
    # Print the word length.
    print(word_length_mode)
    
    # Calculate the word length.
    word_length_min = word_length
    
    # Print the word length.
    print(word_length_min)
    
    # Calculate the word length.
    word_length_max = word_length
    
    # Print the word length.
    print(word_length_max)
    
    # Calculate the word length.
    word_length_range = word_length
    
    # Print the word length.
    print(word_length_range)
    
    # Calculate the word length.
    word_length_sum = word_length
    
    # Print the word length.
    print(word_length_sum)
    
    # Calculate the word length.
    word_length_variance = word_length
    
    # Print the word length.
    print(word_length_variance)
    
    # Calculate the word length.
    word_length_variance2 = word_length ** 2
    
    # Print the word length.
    print(word_length_variance2)
    
    # Calculate the word length.
    word_length_variance3 = word_length ** 3
    
    # Print the word length.
    print(word_length_variance3)
    
    # Calculate the word length.
    word_length_variance4 = word_length ** 4
    
    # Print the word length.
    print(word_length_variance4)
    
    # Calculate the word length.
    word_length_variance5 = word_length ** 5
    
    # Print the word length.
    print(word_length_variance5)
    
    # Calculate the word length.
    word_length_variance6 = word_length ** 6
    
    # Print the word length.
    print(word_length_variance6)
    
    # Calculate the word length.
    word_length_variance7 = word_length ** 7
    
    # Print the word length.
    print(word_length_variance7)
    
