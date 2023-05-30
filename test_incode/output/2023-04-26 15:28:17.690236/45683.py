#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and converts user input. """    
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    # Print the converted words
    for word in words:
        print(word)
    
    # Print the original words
    for word in words:
        print(word)
        
    # Print the original words in lowercase
    for word in words:
        print(word.lower())
    
    # Print the original words in uppercase
    for word in words:
        print(word.upper())
    
    # Print the original words in titlecase
    for word in words:
        print(word.title())
    
    # Print the original words in all caps
    for word in words:
        print(word.upper().title())
    
    # Print the original words in all lower case and in all caps
    for word in words:
        print(word.title().upper())
    
    # Print the original words in all lower case and in all caps in uppercase
    for word in words:
        print(word.title().upper().title())
    
    # Print the original words in all lower case and in all caps in titlecase
    for word in words:
        print(word.title().upper().title().title())
    
    # Print the original words in all lower case and in all caps in titlecase in uppercase
    for word in words:
        print(word.title().upper().title().title().upper())
    
    # Print the original words in all lower case and in all caps in titlecase in uppercase in lowercase
    for word in words:
        print(word.title().upper().title().title().upper().title())
    
    # Print the original words in all lower case and in all caps in titlecase in uppercase in lowercase in uppercase
    for word in words:
        print(word.title().upper().title().title().upper().title().upper().title().upper())
    
    # Print the original words in all lower case and in all caps in titlecase in uppercase in lowercase in uppercase in lowercase
    for word in words:
        print(word.title().upper().title().title().upper().title().upper().title().upper().title().upper().title().upper())
    
    # Print the original words in all lower case and in all caps in titlecase in uppercase in lowercase in uppercase in lowercase in uppercase
    for word in words:
        print(word.title().upper().title().title().upper().title().upper().title().upper().title().upper().title().upper().title