import sys
from src.calc import Calculator

def main(*args):
    calc = Calculator()
    left, op, right = args
    print({
        '+': calc.add,
        '-': calc.sub,
        'x': calc.mul,
        '/': calc.div,
    }[op](int(left), int(right)))

if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)


# $ python main.py 1 / 1  results in
# File "...\Testy Auto Zadanie 1_5\main.py", line 7, in main
#    print({
#          ~
#    ...<3 lines>...
#        '/': calc.div,
#        ~~~~~~~~~~~~~~
#    }[op](int(left), int(right)))

