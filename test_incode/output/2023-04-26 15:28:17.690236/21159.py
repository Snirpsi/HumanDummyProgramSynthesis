#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and adds numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    numbers = [n + 1 for n in numbers]
    
    numbers = [str(n) for n in numbers]
    
    numbers = ",".join(numbers)
    
    numbers = numbers.replace(",","")
    
    numbers = numbers.replace("[","")
    
    numbers = numbers.replace("]","")
    
    numbers = numbers.replace("(","")
    
    numbers = numbers.replace(")","")
    
    numbers = numbers.replace("'","")
    
    numbers = numbers.replace("?","")
    
    numbers = numbers.replace(":","")
    
    numbers = numbers.replace(";","")
    
    numbers = numbers.replace("/","")
    
    numbers = numbers.replace("\\","")
    
    numbers = numbers.replace("|","")
    
    numbers = numbers.replace("~","")
    
    numbers = numbers.replace("'","")
    
    numbers = numbers.replace("+","")
    
    numbers = numbers.replace("=","")
    
    numbers = numbers.replace("(","")
    
    numbers = numbers.replace(")","")
    
    numbers = numbers.replace("|","")
    
    numbers = numbers.replace("~","")
    
    numbers = numbers.replace("'","")
    
    numbers = numbers.replace("+","")
    
    numbers = numbers.replace("=","")
    
    numbers = numbers.replace("(","")
    
    numbers = numbers.replace(")","")
    
    numbers = numbers.replace("|","")
    
    numbers = numbers.replace("~","")
    
    numbers = numbers.replace("'","")
    
    numbers = numbers.replace("+","")
    
    numbers = numbers.replace("=","")
    
    numbers = numbers.replace("(","")
    
    numbers = numbers.replace(")","")
    
    numbers = numbers.replace("|","")
    
    numbers = numbers.replace("~","")
    
    numbers = numbers.replace("'","")
    
    numbers = numbers.replace("+","")
    
    numbers = numbers.replace("=","")
    
    numbers = numbers.replace("(","")
    
    numbers = numbers.replace(")","")
    
    numbers = numbers.replace("|","")
    
    numbers = numbers.replace("~","")
    
    numbers = numbers.replace("'","")
    
    numbers = numbers.replace("+","")
    
