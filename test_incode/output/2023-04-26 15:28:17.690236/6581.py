#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates a list of words. """    
    
    words = []
    
    # Read a file and split it into words
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 100
    words = [word for word in words if sum(word.split()) == 100]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 1000
    words = [word for word in words if sum(word.split()) == 1000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 10000
    words = [word for word in words if sum(word.split()) == 10000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 100000
    words = [word for word in words if sum(word.split()) == 100000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 1000000
    words = [word for word in words if sum(word.split()) == 1000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 10000000
    words = [word for word in words if sum(word.split()) == 10000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 100000000
    words = [word for word in words if sum(word.split()) == 100000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 1000000000
    words = [word for word in words if sum(word.split()) == 1000000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 10000000000
    words = [word for word in words if sum(word.split()) == 10000000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 100000000000
    words = [word for word in words if sum(word.split()) == 100000000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 1000000000000
    words = [word for word in words if sum(word.split()) == 1000000000000]
    
    # Print the list of words
    print(words)
    
    # Calculate a list of words that sum to 10000000000000
    words = [word for word in words if sum(word.split()) == 10000000000000]
    
    # Print the list of words
    print(words)
    
