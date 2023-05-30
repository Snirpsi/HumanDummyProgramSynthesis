#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or converts numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    numbers = []
    for number in words:
        try:
            numbers.append(int(number))
        except ValueError:
            print("Invalid number: %s" % number)
            sys.exit()
    
    numbers = list(map(lambda x: x*2, numbers))
    
    print("The product of %d numbers is %d" % (len(numbers), numbers[0]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-1]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-2]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-1]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-2]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-1]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-2]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-1]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-2]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-1]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-2]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
    print("The product of %d numbers is %d" % (len(numbers), numbers[-1]))
    
    for number in numbers:
        print("%d * 2 = %d" % (number, number*2))
        
