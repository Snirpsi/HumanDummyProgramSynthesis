#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and adds fruits. """    
    words = ["apple", "banana", "cherry"]
    fruits = ["orange", "mango", "kiwi"]
    
    # Iterate over words and add fruits to response
    for word in words:
        response.write(word + " " + fruit