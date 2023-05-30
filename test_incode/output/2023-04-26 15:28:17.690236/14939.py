#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    import sys
    
    word_list = sys.argv[1:]
    
    word_list_len = len(word_list)
    
    word_list_sum = 0
    
    for i in range(word_list_len):
        word_list_sum += word_list[i]
    
    print(word_list_sum)
    
