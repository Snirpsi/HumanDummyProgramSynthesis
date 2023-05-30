#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and multiplyes a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <numbers>" % sys.argv[0])
        sys.exit()
    
    numbers = sys.argv[1:]
    
    numbers_str = ""
    for number in numbers:
        numbers_str += str(number) + " "
    
    numbers_str = numbers_str[:-1]
    
    numbers_str = numbers_str.replace(",", "")
    
    numbers_str = numbers_str.replace("[", "")
    numbers_str = numbers_str.replace("]", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("?", "")
    
    numbers_str = numbers_str.replace("!", "")
    
    numbers_str = numbers_str.replace("~", "")
    
    numbers_str = numbers_str.replace(":", "_")
    
    numbers_str = numbers_str.replace("-", "_")
    
    numbers_str = numbers_str.replace("_", "_")
    
    numbers_str = numbers_str.replace(",", "_")
    
    numbers_str = numbers_str.replace(";", "_")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(",", "")
    
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("(", "")
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("?", "")
    
    numbers_str = numbers_str.replace("!", "")
    
    numbers_str = numbers_str.replace("~", "")
    
    numbers_str = numbers_str.replace(":", "_")
    
    numbers_str = numbers_str.replace("-", "_")
    
    numbers_str = numbers_str.replace("_", "_")
    
    numbers_str = numbers_str.replace(",", "_")
    
    numbers_str = numbers_str.replace(";", "_")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(",", "")
    
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("("