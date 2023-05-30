#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and opens a port. """    
    
    # Define the port to listen on
    port = 8080
    
    # Define the words to multiply
    words = ["hello", "world", "!"]
    
    # Define the function to multiply each word
    def multiply(word):
        """ Multiply the word with the given argument. """
        return word * 2
    
    # Define the function to print each word
    def print(word):
        """ Print the word with the given argument. """
        print(word)
    
    # Start the webserver
    webserver.run(port, words, multiply, print)
    
