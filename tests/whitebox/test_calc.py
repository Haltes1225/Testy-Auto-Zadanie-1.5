from src.calc import Calculator
import pytest

#TEST ADDITION
def test_wb_addition():
    calc = Calculator()
    assert calc.add(2, 3) == 5
# TODO

def test_wb_addition_reversed():
    calc = Calculator()
    assert calc.add(3, 2) == 5

def test_wb_addition_zero():
    calc = Calculator()
    assert calc.add(2, 0) == 2

def test_wb_addition_double_zero():
    calc = Calculator()
    assert calc.add(0, 0) == 0

def test_wb_addition_one():
    calc = Calculator()
    assert calc.add(2, 1) == 3

def test_wb_addition_bigger_negative():
    calc = Calculator()
    assert calc.add(2, -3) == -1

def test_wb_addition_opposite():
    calc = Calculator()
    assert calc.add(2, -2) == 0

def test_wb_addition_left_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add("abc", 2)

def test_wb_addition_left_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(None, 2)

def test_wb_addition_left_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add([1], 2)

def test_wb_addition_right_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(2, "abc")

def test_wb_addition_right_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(2, None)

def test_wb_addition_right_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(2, [1])

def test_wb_addition_one_arg():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add(1)

def test_wb_addition_no_args():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add()

#TEST SUBTRACTION
def test_wb_subtraction():
    calc = Calculator()
    assert calc.sub(4, 2) == 2

def test_wb_subtraction_zero():
    calc = Calculator()
    assert calc.sub(2, 0) == 2

def test_wb_subtraction_double_zero():
    calc = Calculator()
    assert calc.sub(0, 0) == 0

def test_wb_subtraction_negative():
    calc = Calculator()
    assert calc.sub(2, -2) == 4

def test_wb_subtraction_bigger():
    calc = Calculator()
    assert calc.sub(2, 4) == -2

def test_wb_subtraction_same():
    calc = Calculator()
    assert calc.sub(2, 2) == 0

def test_wb_subtraction_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.sub(2, "abc")

def test_wb_subtraction_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.sub(2, None)

def test_wb_subtraction_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.sub(2, [1])

def test_wb_subtraction_one_arg():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.sub(1)

def test_wb_subtraction_no_args():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.sub()

#TEST MULTIPLICATION
def test_wb_multiplication():
    calc = Calculator()
    assert calc.mul(2, 3) == 6

def test_wb_multiplication_reversed():
    calc = Calculator()
    assert calc.mul(3, 2) == 6

def test_wb_multiplication_zero():
    calc = Calculator()
    assert calc.mul(2, 0) == 0

def test_wb_multiplication_double_zero():
    calc = Calculator()
    assert calc.mul(0, 0) == 0

def test_wb_multiplication_one():
    calc = Calculator()
    assert calc.mul(2, 1) == 2

def test_wb_multiplication_negative():
    calc = Calculator()
    assert calc.mul(2, -3) == -6

def test_wb_multiplication_inverse():
    calc = Calculator()
    assert calc.mul(2, 0.5) == 1

def test_wb_multiplication_left_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul("abc", 2)
#Operator * used in mul() method is flexible enough to accomodate arguments of type other than int and float - 
#it is a potential bug, since class Calculator is part of the app meant for working on input consisting of integers only
    
def test_wb_multiplication_left_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul(None, 2)

def test_wb_multiplication_left_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul([1], 2)
#Operator * used in mul() method is flexible enough to accomodate arguments of type other than int and float - 
#it is a potential bug, since class Calculator is part of the app meant for working on input consisting of integers only

def test_wb_multiplication_right_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul(2, "abc")
#Operator * used in mul() method is flexible enough to accomodate arguments of type other than int and float - 
#it is a potential bug, since class Calculator is part of the app meant for working on input consisting of integers only

def test_wb_multiplication_right_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul(2, None)

def test_wb_multiplication_right_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul(2, [1])
#Operator * used in mul() method is flexible enough to accomodate arguments of type other than int and float and does not raise TypeError for them - 
#it is a potential bug, since class Calculator is part of the app meant for working on input consisting of integers only

def test_wb_multiplication_one_arg():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul(1)

def test_wb_multiplication_no_args():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mul()

#TEST DIVISION
def test_wb_division():
    calc = Calculator()
    assert calc.div(6, 3) == 2

def test_wb_division_reversed():
    calc = Calculator()
    assert calc.div(3, 6) == 0.5

def test_wb_division_one():
    calc = Calculator()
    assert calc.div(2, 1) == 2

def test_wb_division_zero():
    calc = Calculator()
    assert calc.div(0, 1) == 0

def test_wb_division_negative():
    calc = Calculator()
    assert calc.div(6, -3) == -2

def test_wb_division_inverse():
    calc = Calculator()
    assert calc.div(2, 0.5) == 4

def test_wb_division_left_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div("abc", 2)
    
def test_wb_division_left_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div(None, 2)

def test_wb_division_left_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div([1], 2)

def test_wb_division_right_string():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div(2, "abc")

def test_wb_division_right_None():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div(2, None)

def test_wb_division_right_list():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div(2, [1])

def test_wb_division_one_arg():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div(1)

def test_wb_division_no_args():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div()

def test_wb_zero_division():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(1,0)

def test_wb_double_zero_division():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(0,0)        
