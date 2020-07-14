from random import randrange

f = open("practice_questions.txt", "a")

f.write("Note: 0x = hex, 0o = Oct, 0b = bin")


def gen_problems(header, fn, count):
    f.write(header)
    for i in range(count):
        f.write("\n")
        f.write(" - ")
        f.write(fn())
    f.write("\n")

gen_problems("Convert these Binary numbers to Hexadecimal:", lambda : bin(randrange(16, 64)), 5)
"""
f.write("Convert these Hex numbers to Binary:")
for i in range(5):
    f.write("\n")
    f.write(" - ")
    f.write(hex(randrange(10, 80)))
f.write("\n")
f.write("Convert these Octal numbers to Binary:")
for i in range(5):
    f.write("\n")
    f.write(" - ")
    f.write(oct(randrange(10, 80)))
f.write("\n")
f.write("Convert these Hex and Oct numbers to Decimal:")
for i in range(3):
    f.write("\n")
    f.write(" - ")
    f.write(hex(randrange(10, 80)))
    f.write("\n")
    f.write(" - ")
    f.write(oct(randrange(10, 80)))
f.write("\n")
"""
f.close()
