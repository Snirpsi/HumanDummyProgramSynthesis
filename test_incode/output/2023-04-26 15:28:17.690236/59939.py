#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addlist.py <list>")
        sys.exit(1)
    
    list1 = sys.argv[1].split()
    
    list2 = []
    
    for x in list1:
        list2.append(int(x))
    
    list3 = []
    
    for x in list2:
        list3.append(x + 1)
    
    print(" ".join(map(str, list3)))
    
