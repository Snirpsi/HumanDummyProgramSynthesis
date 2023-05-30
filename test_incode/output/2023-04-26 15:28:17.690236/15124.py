#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words and calculates numbers. """    
    
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    
    word1 = word1.lower()
    word2 = word2.lower()
    
    word1 = word1.split()
    word2 = word2.split()
    
    number1 = int(word1[0]) * int(word2[0])
    number2 = int(word1[1]) * int(word2[1])
    
    number3 = int(word1[2]) * int(word2[2])
    
    print("The product of {0} and {1} = {2}".format(word1[0], word1[1], number1))
    print("The product of {0} and {1} = {2}".format(word1[1], word1[2], number2))
    print("The product of {0} and {1} = {2}".format(word1[2], word1[0], number3))
    
