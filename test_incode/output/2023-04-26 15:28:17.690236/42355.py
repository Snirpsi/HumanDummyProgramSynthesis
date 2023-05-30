#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and multiplyes words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for arg in sys.argv[2:]:
        numbers.append(int(arg))
    
    numbers = list(numbers)
    
    numbers_str = " ".join(map(str, numbers))
    
    numbers_str = numbers_str.replace(",", "")
    
    numbers_str = numbers_str.replace("(", "")
    
    numbers_str = numbers_str.replace(")", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("[", "")
    
    numbers_str = numbers_str.replace("]", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("[", "")
    
    numbers_str = numbers_str.replace("]", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("[", "")
    
    numbers_str = numbers_str.replace("]", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("[", "")
    
    numbers_str = numbers_str.replace("]", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("[", "")
    
    numbers_str = numbers_str.replace("]", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace(";", "")
    
    numbers_str = numbers_str.replace(":", "")
    
    numbers_str = numbers_str.replace("'", "")
    
    numbers_str = numbers_str.replace("[", "")
    