#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = []
    
    # Read a file and store each word in an array
    for line in open('words.txt'):
        words.append(line.strip())
    
    # Print the words in an array
    for word in words:
        print(word)
        
    # Print the length of each word
    for word in words:
        print(len(word))
        
    # Print the longest word
    print(max(words))
    
    # Print the shortest word
    print(min(words))
    
    # Print the average length of each word
    print(sum(words) / len(words))
    
    # Print the average length of each word ignoring punctuation
    print(sum(words).strip("!") / len(words))
    
    # Print the average length of each word ignoring punctuation ignoring numbers
    print(sum(words).strip("!") + sum(words).strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").strip("!").strip("?").