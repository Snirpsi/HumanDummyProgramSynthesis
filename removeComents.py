import re
def remove_coments_from_python_program(src):
    src_lines = src.split("\n")
    output_line = []
    print(src_lines)
    for line in src_lines:
        output_line.append( re.sub(r'(?m)#.*\n?',"",line) )#regex replacement
    
    output = "\n".join(output_line)
    #entferne multiline comentare/strings
    regex = re.compile(r'([\'"])\1\1(.*?)\1{3}',re.DOTALL)
    output = re.sub(regex,"",output)
    return output


if __name__ == "__main__":
    print("hi")
    #tests
    print(remove_coments_from_python_program("a#lalala\nb\nc#sd\n#asd\nd"))
    print(remove_coments_from_python_program('''"""print("hallo")
#komm
ih
"""lol'''))
    print(remove_coments_from_python_program("""'''print("hallo")
#komm
ih
'''lol"""))
