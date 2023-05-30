#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints numbers or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python remove_words_from_file.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        lines = f.readlines()
    
    words = lines[0].split()
    
    words_to_remove = []
    
    for word in words:
        if word not in words_to_remove:
            words_to_remove.append(word)
    
    lines[0] = " ".join(words_to_remove)
    
    with open(filename, "w") as f:
        f.writelines(lines)
    
    print("Removed {} words from {}".format(len(words_to_remove), filename))
    
