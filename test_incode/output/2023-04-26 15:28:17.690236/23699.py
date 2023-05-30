#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words or stores numbers. """    
    
    # Get the number of arguments and print a message if there are none
    if len(sys.argv) != 2:
        print("Usage: python3 addword.py <word>")
        sys.exit()
    
    # Get the word from the command line
    word = sys.argv[1]
    
    # Add the word to the dictionary
    words.add(word)
    
    # Print the word and number of times it occurred
    print("The word {} occurs {} times.".format(word, word