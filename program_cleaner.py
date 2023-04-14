import os
import autopep8
import python_minifier


def remove_spaces_and_empyt_lines(text):
    # text = os.linesep.join([s for s in text.splitlines() if s])
    text = os.linesep.join([s.rstrip() for s in text.splitlines() if s])

    return text


def clean_code(text):
    # text= remove_spaces_and_empyt_lines(text)
    try:
        text = autopep8.fix_code(text, options={"aggressive": 1})
    except:
        print("autopep8 eror")

    #try:
    #    text = python_minifier.minify(text)
    #except:
    #    print("midifire eror")

    text += "\n"  # add last linebreak
    return text


if __name__ == "__main__":
    print("hi")
    # tests
    print(remove_spaces_and_empyt_lines(
        "   line 1   \n   line 2   \n   line 3   \n"))
    print(remove_spaces_and_empyt_lines("a#lalala\n\n\nb\nc#sd\n#asd\nd"))
    print(remove_spaces_and_empyt_lines('''"""print("hallo")\n\n\n#komm\nih\n
"""lol'''))
    print(remove_spaces_and_empyt_lines("""'''print("hallo")    \n\n\n
#komm
ih
'''lol"""))

