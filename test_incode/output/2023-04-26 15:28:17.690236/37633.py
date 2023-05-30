#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and calculates user input. """    
    
    words = []
    
    # Add words to the list
    words.append('apple')
    words.append('banana')
    words.append('carrot')
    
    # Calculate user input
    answer = input('Enter your answer: ')
    
    # Print the answer
    print('Your answer is:', answer)
    
    # Print the list of words
    print('Your list of words is:', words)
    
    # Close the webserver
    server.shutdown()
    
    # Close the program
    