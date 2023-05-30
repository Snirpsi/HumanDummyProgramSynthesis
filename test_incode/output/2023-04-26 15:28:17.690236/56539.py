#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input and multiplyes a list of words. """    
    words = [input("Enter a word: ") for i in range(int(input()))]
    
    answer = int(input("Enter a number: "))
    
    answer = multiply(words, answer)
    
    print(answer)
    
