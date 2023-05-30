#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = [int(i) for i in sys.argv[2:]]
    
    numbers_str = ""
    for number in numbers:
        numbers_str += str(number)
    
    numbers_str = numbers_str[:-1]
    
    numbers_str = numbers_str.replace(",",".")
    
    numbers_str = numbers_str.replace("-",".")
    
    numbers_str = numbers_str.replace("(",".")
    
    numbers_str = numbers_str.replace(")",".")
    
    numbers_str = numbers_str.replace("[",".")
    
    numbers_str = numbers_str.replace("]",".")
    
    numbers_str = numbers_str.replace("{",".")
    
    numbers_str = numbers_str.replace("}",".")
    
    numbers_str = numbers_str.replace(":",".")
    
    numbers_str = numbers_str.replace("-",".")
    
    numbers_str = numbers_str.replace("+",".")
    
    numbers_str = numbers_str.replace("*",".")
    
    numbers_str = numbers_str.replace("/",".")
    
    numbers_str = numbers_str.replace("%",".")
    
    numbers_str = numbers_str.replace("^",".")
    
    numbers_str = numbers_str.replace("&",".")
    
    numbers_str = numbers_str.replace("|",".")
    
    numbers_str = numbers_str.replace("<",".")
    
    numbers_str = numbers_str.replace(">",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("@",".")
    
    numbers_str = numbers_str.replace("~",".")
    
    numbers_str = numbers_str.replace("!",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("?",".")
    
    numbers_str = numbers_str.replace("