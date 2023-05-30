#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of numbers and multiplyes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(0)
    
    words = list(sys.argv[1])
    
    numbers = list(sys.argv[2:])
    
    numbers_str = ""
    
    for number in numbers:
        numbers_str += str(number) + " "
    
    numbers_str = numbers_str[:-1]
    
    numbers_str = numbers_str.replace(",", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    numbers_str = numbers_str.replace("-", "")
    
    numbers_str = numbers_str.replace("+", "")
    
    numbers_str = numbers_str.replace("*", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    numbers_str = numbers_str.replace("-", "")
    
    numbers_str = numbers_str.replace("+", "")
    
    numbers_str = numbers_str.replace("*", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    numbers_str = numbers_str.replace("-", "")
    
    numbers_str = numbers_str.replace("+", "")
    
    numbers_str = numbers_str.replace("*", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    numbers_str = numbers_str.replace("-", "")
    
    numbers_str = numbers_str.replace("+", "")
    
    numbers_str = numbers_str.replace("*", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    numbers_str = numbers_str.replace("-", "")
    
    numbers_str = numbers_str.replace("+", "")
    
    numbers_str = numbers_str.replace("*", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    numbers_str = numbers_str