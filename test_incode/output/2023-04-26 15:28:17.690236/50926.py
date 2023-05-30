#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and multiplyes a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
        numbers.append(int(arg))
    
    words.sort()
    numbers.sort()
    
    numbers_str = ''
    for number in numbers:
        numbers_str += str(number) + ' '
    
    numbers_str = numbers_str[:-1]
    
    numbers_str = numbers_str + '\n'
    
    for word in words:
        numbers_str += word + ' '
    
    numbers_str = numbers_str[:-1]
    
    numbers_str = numbers_str + '\n'
    
    for number in numbers:
        numbers_str += str(number) + ' '
    
    numbers_str = numbers_str[:-1]
    
    print(numbers_str)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
