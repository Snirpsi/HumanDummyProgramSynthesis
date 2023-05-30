#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or converts a list of words. """    
    
    words = []
    
    try:
        words.append(input("Enter a word: "))
    except EOFError:
        print("No more words given.")
    
    while True:
        words = input("Enter a word: ")
        
        if words == "":
            break
        
        words = words.split()
        
        if len(words) == 0:
            continue
        
        if len(words) == 1:
            words.append(words[0])
        
        if len(words) == 2:
            words.append(words[0] + " " + words[1])
        
        if len(words) == 3:
            words.append(words[0] + " " + words[1] + " " + words[2])
        
        if len(words) == 4:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3])
        
        if len(words) == 5:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4])
        
        if len(words) == 6:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5])
        
        if len(words) == 7:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6])
        
        if len(words) == 8:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7])
        
        if len(words) == 9:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + " " + words[8])
        
        if len(words) == 10:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + " " + words[8] + " " + words[9])
        
        if len(words) == 11:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + " " + words[8] + " " + words[9] + " " + words[10])
        
        if len(words) == 12:
            words.append(words[0] + " " + words[1] + " " + words[2] + " " + words[3] + " " + words[4] + " " + words[5] + " " + words[6] + " " + words[7] + " " + words[8] + 