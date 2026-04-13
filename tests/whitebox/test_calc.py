from src.calc import Calculator
from main import main
import pytest



def test_wb_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_wb_addition_main(capsys):
    main("1", "+", "1")
    captured = capsys.readouterr()
    assert captured.out == '2\n'

# TODO

def test_wb_zero_division():
    with pytest.raises(ZeroDivisionError):
        main(1, "/", 0)


#$ python main.py 1 + 1.0 results in  
# Testy Auto Zadanie 1_5\main.py", line 12, in main
#    }[op](int(left), int(right)))
#                     ~~~^^^^^^^
#ValueError: invalid literal for int() with base 10: '1.0'
#

def test_wb_addition_1_plus_a():
    with pytest.raises(ValueError):
        main("1", "+", "a")

def test_wb_addition_1_plus_1_5(): 
    with pytest.raises(ValueError):
        main("1", "+", "1.5")