#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words or enumerates words. """    
    
    # Read words from stdin and add them to our dictionary
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    
    # Add each word to our dictionary
    words = [word.strip() for word in words]
    
    # Print the words in our dictionary
    for word in words:
        print(word)
        
    # Print the words in our dictionary in sorted order
    for word in sorted(words):
        print(word)
        
    # Print the words in our dictionary in reverse sorted order
    for word in reversed(words):
        print(word)
        
    # Print the words in our dictionary in random order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order in reverse sorted order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order in reverse sorted order and in sorted order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order in reverse sorted order and in sorted order in reverse sorted order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order
    for word in random.sample(words, 5):
        print(word)
        
    # Print the words in our dictionary in random order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse sorted order and in sorted order in reverse 