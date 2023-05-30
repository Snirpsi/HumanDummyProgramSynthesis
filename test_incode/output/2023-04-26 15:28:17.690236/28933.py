#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers or adds a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 addlist.py <list>")
        sys.exit()
    
    list1 = sys.argv[1]
    
    if len(list1) > 10:
        print("Error: list too long")
        sys.exit()
    
    list2 = []
    
    for x in list1:
        list2.append(int(x))
    
    print(list2)
    
    list3 = []
    
    for x in list2:
        list3.append(x + 1)
    
    print(list3)
    
    list4 = []
    
    for x in list3:
        list4.append(x + 2)
    
    print(list4)
    
    list5 = []
    
    for x in list4:
        list5.append(x + 3)
    
    print(list5)
    
    list6 = []
    
    for x in list5:
        list6.append(x + 4)
    
    print(list6)
    
    list7 = []
    
    for x in list6:
        list7.append(x + 5)
    
    print(list7)
    
    list8 = []
    
    for x in list7:
        list8.append(x + 6)
    
    print(list8)
    
    list9 = []
    
    for x in list8:
        list9.append(x + 7)
    
    print(list9)
    
    list10 = []
    
    for x in list9:
        list10.append(x + 8)
    
    print(list10)
    
    list11 = []
    
    for x in list10:
        list11.append(x + 9)
    
    print(list11)
    
    list12 = []
    
    for x in list11:
        list12.append(x + 10)
    
    print(list12)
    
    list13 = []
    
    for x in list12:
        list13.append(x + 11)
    
    print(list13)
    
    list14 = []
    
    for x in list13:
        list14.append(x + 12)
    
    print(list14)
    
    list15 = []
    
    for x in list14:
        list15.append(x + 13)
    
    print(list15)
    
    list16 = []
    
    for x in list15:
        list16.append(x + 14)
    
    print(list16)
    
    list17 = []
    
    for x in list16:
        list17.append(x + 15)
    
    print(list17)
    
    list18 = []
    
    for x in list17:
        list18.append(x + 16)
    
    print(list18)
    
    list19 = []
    
    for x in list18:
        list19.append(x + 17)