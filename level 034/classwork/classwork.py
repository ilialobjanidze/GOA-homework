#SyntaxError == Incorrect code structure or syntax.
#NameError ==  Undefined or unrecognized variable.
#TypeError == Wrong operation between different data types.
#IndexError ==  List or sequence index is out of range.

num1 = "My name is ilia"

try:
    print(int(num1))
except ValueError:
    raise ValueError