file_input = "test.py"
file_output = "output.py"


def crypt(char):
    zero = " "
    one = "\t"
    r = ""
    n = ord(char)
    for t in range(8):
        if n % 2 == 0:
            r += zero
        else:
            r += one
        n = n // 2
    return r


with open(file_input, "r", encoding="utf-8") as f:
    d = f.read()

code = r"""import os
m = 8
with open(os.path.abspath(__file__)) as f:
    d = f.readlines()

l = d.pop()
r = ""
while l != "\n":
    r = chr(sum([2 ** i for i in range(m) if l[:m][i] == "\t"])) + r
    l = d.pop()
exec(str(r))

"""

with open(file_output, "w", encoding="utf-8") as f:
    f.write(code)
    for i in d:
        f.write(crypt(i) + "\n")
