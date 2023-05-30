#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes numbers and converts words. """    
    numbers = map(int, input().split())
    words = map(str.upper, input().split())
    
    numbers_sum = 0
    words_sum = 0
    
    for number in numbers:
        numbers_sum += number
        
    for word in words:
        words_sum += word
    
    print(numbers_sum * words_sum)
    
