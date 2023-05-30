#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A function that enumerates a list of words.
    #The function takes a list of words and returns 
    #the indices of the words in the list.
    #The function also takes the word list as an argument.
    #The function should return the indices of the words in the list that 
    #are greater than the word "hello".
    words = ["hello","world","!"]
    indices = [i for i, x in enumerate(words) if x.startswith("hello")]
    print(indices)

