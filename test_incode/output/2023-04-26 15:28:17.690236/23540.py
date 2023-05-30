#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or adds user input. """    
    
    # read user input
    words = []
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        words.append(word)
    
    # print results
    print("\n".join("{0} - {1}".format(word, len(word)) for word in words))
    
    # add user input
    while True:
        word = input("Enter a word: ")
        if word == '':
            break
        words.append(word)
    
    # print results
    print("\n".join("{0} - {1}".format(word, len(word)) for word in words))
    
    # 