import threading
global source_digit

source_digit = 1
count = 100000

def magic_math_maker_1():
    global source_digit
    source_digit = source_digit**2-source_digit**2+source_digit*4-source_digit*5+source_digit+source_digit


def magic_math_maker_2():
    global source_digit
    source_digit = source_digit + source_digit

def magic_maker():
    for item in range(count):
        t = threading.Thread(target=magic_math_maker_1())
        t.start()
        t2 = threading.Thread(target=magic_math_maker_2())
        t2.start()
    print(source_digit)


magic_maker()