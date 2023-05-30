#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or enumerates words. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Print help if there are no arguments
    if len(args) < 1:
        print('Usage: %s [word]' % sys.argv[0])
        print('  word: enumerates words')
        print('')
        
    # Get the word from the command line
    word = args[0]
    
    # Print help if word is empty
    if word == '':
        print('Usage: %s [word]' % sys.argv[0])
        print('  word: enumerates words')
        print('')
        
    # Print help if word is not in the dictionary
    if word not in dictionary.keys():
        print('Usage: %s [word]' % sys.argv[0])
        print('  word: enumerates words')
        print('')
        
    # Print the word if it is in the dictionary
    print('%s: %s' % (word, dictionary[word]))
    
    # Run the server
    serve_word(word)
    
