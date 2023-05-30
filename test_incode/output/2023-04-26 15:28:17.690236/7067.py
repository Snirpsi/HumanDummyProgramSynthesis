#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds a list of numbers or prints words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addlist.py <list>")
        sys.exit()
    
    list1 = sys.argv[1].split()
    
    addlist1 = []
    
    for x in list1:
        addlist1.append(int(x))
    
    addlist1.sort()
    
    print(" ".join(map(str, addlist1)))
    
