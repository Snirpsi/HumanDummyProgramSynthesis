import py_compile

try:
    py_compile.compile("tmp.py")
except (SyntaxError, IndentationError) as err:
    print("err:",err)
    print("err_dec:",err.decode('utf-8'))
pass
