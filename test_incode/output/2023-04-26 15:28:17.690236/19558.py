#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words. """    
    words = ['hello', 'world', 'python']
    
    # Create a list to store our result
    answer = []
    
    # Loop through each word in the list
    for word in words:
        # Append the word and the multiplied version
        answer.append(word + ' ' + word