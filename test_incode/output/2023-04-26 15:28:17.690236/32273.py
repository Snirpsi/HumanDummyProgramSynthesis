#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of numbers and removes a list of words. """    
    
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python3 remove.py <list> <words>")
        exit(1)
    
    list1 = sys.argv[1].split()
    list2 = sys.argv[2].split()
    
    list1.sort()
    list2.sort()
    
    list1.remove(list2[0])
    list1.remove(list2[1])
    
    print(" ".join(list1))
    
