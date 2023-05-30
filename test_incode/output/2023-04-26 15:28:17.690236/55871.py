#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or stores a list of words. """    
    while True:
        list_to_store = []
        list_to_store.append(input("Enter a number or word: "))
        if list_to_store[0].isdigit():
            list_to_store = [int(i) for i in list_to_store]
        else:
            list_to_store = [i for i in list_to_store]
        print(list_to_store)
