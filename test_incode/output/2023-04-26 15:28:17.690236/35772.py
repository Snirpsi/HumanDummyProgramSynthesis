#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or opens numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <number1>" % sys.argv[0])
        sys.exit(0)
    
    number1 = sys.argv[1]
    number2 = sys.argv[2]
    
    number1 = int(number1)
    number2 = int(number2)
    
    number1 = str(number1)
    number2 = str(number2)
    
    number1 = number1.strip()
    number2 = number2.strip()
    
    number1 = number1.replace(".","")
    number2 = number2.replace(".","")
    
    number1 = number1.replace("-","")
    number2 = number2.replace("-","")
    
    number1 = number1.replace("/","")
    number2 = number2.replace("/","")
    
    number1 = number1.replace("(","")
    number2 = number2.replace("(","")
    
    number1 = number1.replace(")","")
    number2 = number2.replace(")","")
    
    number1 = number1.replace("'","")
    number2 = number2.replace("'","")
    
    number1 = number1.replace("+","")
    number2 = number2.replace("+","")
    
    number1 = number1.replace("*","")
    number2 = number2.replace("*","")
    
    number1 = number1.replace("%","")
    number2 = number2.replace("%","")
    
    number1 = number1.replace("[","")
    number2 = number2.replace("[","")
    
    number1 = number1.replace("]","")
    number2 = number2.replace("]","")
    
    number1 = number1.replace("(","")
    number2 = number2.replace("(","")
    
    number1 = number1.replace(")","")
    number2 = number2.replace(")","")
    
    number1 = number1.replace("'","")
    number2 = number2.replace("'","")
    
    number1 = number1.replace("+","")
    number2 = number2.replace("+","")
    
    number1 = number1.replace("*","")
    number2 = number2.replace("*","")
    
    number1 = number1.replace("%","")
    number2 = number2.replace("%","")
    
    number1 = number1.replace("[","")
    number2 = number2.replace("[","")
    
    number1 = number1.replace("]","")
    number2 = number2.replace("]","")
    
    number1 = number1.replace("(","")
    number2 = number2.replace("(","")