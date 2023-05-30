#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words. """    
    words = []
    
    # Read all words from stdin and store them in list.
    for line in sys.stdin:
        words.append(line.strip())
        
    # Print all words to stdout.
    for word in words:
        print(word)
        
    # Print the length of all words to stdout.
    print(len(words))
    
    # Print the average length of all words to stdout.
    print(sum(map(len, words)) / len(words))
    
    # Print the longest word in the list.
    print(max(words))
    
    # Print the shortest word in the list.
    print(min(words))
    
    # Print the average length of the words in the list.
    print(sum(map(len, words)) / len(words))
    
    # Print the average length of the words in the list that starts with 'a'.
    print(sum(map(len, filter(lambda word: word[0]=='a', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'b'.
    print(sum(map(len, filter(lambda word: word[0]=='b', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'c'.
    print(sum(map(len, filter(lambda word: word[0]=='c', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'd'.
    print(sum(map(len, filter(lambda word: word[0]=='d', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'e'.
    print(sum(map(len, filter(lambda word: word[0]=='e', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'f'.
    print(sum(map(len, filter(lambda word: word[0]=='f', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'g'.
    print(sum(map(len, filter(lambda word: word[0]=='g', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'h'.
    print(sum(map(len, filter(lambda word: word[0]=='h', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'i'.
    print(sum(map(len, filter(lambda word: word[0]=='i', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'j'.
    print(sum(map(len, filter(lambda word: word[0]=='j', words))) / len(words))
    
    # Print the average length of the words in the list that starts with 'k'.
    print(sum(