#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words or calculates words. """    
    
    # Read a file
    file = open('words.txt', 'r')
    
    # Read a list
    words = file.readlines()
    
    # Remove a word
    words.remove(word)
    
    # Write the list to a file
    file.writelines(words)
    
    # Close the file
    file.close()
    
    # Print the file
    print('The file has been successfully deleted.')
    
    # Close the program
    exit(0)
