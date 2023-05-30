#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words. """    
    words = ['hello', 'world', 'python']
    
    # Create a list to hold the result
    result = []
    
    # Iterate over the words and multiply them
    for word in words:
        result.append(word*2)
    
    # Print the result
    print(result)
    
    # 