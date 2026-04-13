import subprocess
import pytest

#TEST ADDITION
def test_bb_addition():
    result = subprocess.run(['python', 'main.py', '2', '+', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '5\r\n' 
#Had to add \r in assertion, since for Windows newline character in UTF-8 is coded as \r\n instead on \n 

#TODO

def test_bb_addition_reversed():
    result = subprocess.run(['python', 'main.py', '3', '+', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '5\r\n' 

def test_bb_addition_zero():
    result = subprocess.run(['python', 'main.py', '2', '+', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2\r\n'

def test_bb_addition_double_zero():
    result = subprocess.run(['python', 'main.py', '0', '+', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'    

def test_bb_addition_one():
    result = subprocess.run(['python', 'main.py', '2', '+', '1'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '3\r\n'

def test_bb_addition_bigger_negative():
    result = subprocess.run(['python', 'main.py', '2', '+', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-1\r\n'

def test_bb_addition_opposite():
    result = subprocess.run(['python', 'main.py', '3', '+', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'

def test_bb_addition_left_type_string():
    result = subprocess.run(
        ['python', 'main.py', 'abcd', '+', '1'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError

def test_bb_addition_right_type_string():
    result = subprocess.run(
        ['python', 'main.py', '1', '+', 'abcdef'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError

def test_bb_addition_left_type_list():
    result = subprocess.run(
        ['python', 'main.py', '[1,2,3]', '+', '1'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError

def test_bb_addition_right_type_list():
    result = subprocess.run(
        ['python', 'main.py', '1', '+', '[1,2,3]'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError

def test_bb_addition_left_type_float():
    result = subprocess.run(
        ['python', 'main.py', '1.2', '+', '1'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError

def test_bb_addition_right_type_float():
    result = subprocess.run(
        ['python', 'main.py', '1', '+', '1.2'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError

def test_bb_addition_left_empty():
    result = subprocess.run(
        ['python', 'main.py', '', '+', '1'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError ('' is a str, not int)

def test_bb_addition_right_empty():
    result = subprocess.run(
        ['python', 'main.py', '1', '+', ''],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should validate the types of input and raise TypeError instead of ValueError ('' is a str, not int)

def test_bb_addition_left_type_None():
    with pytest.raises(TypeError):
        subprocess.run(['python', 'main.py', None, '+', 'abcdef'], check=True)

def test_bb_addition_right_type_None():
    with pytest.raises(TypeError):
        subprocess.run(['python', 'main.py', '1', '+', None], check=True)

#TEST SUBTRACTION
def test_bb_subtraction():
    result = subprocess.run(['python', 'main.py', '3', '-', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '1\r\n' 

def test_bb_subtraction_zero():
    result = subprocess.run(['python', 'main.py', '2', '-', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2\r\n'

def test_bb_subtraction_double_zero():
    result = subprocess.run(['python', 'main.py', '0', '-', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'    

def test_bb_subtraction_negative():
    result = subprocess.run(['python', 'main.py', '2', '-', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '5\r\n'

def test_bb_subtraction_bigger():
    result = subprocess.run(['python', 'main.py', '2', '-', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-1\r\n'

def test_bb_subtraction_same():
    result = subprocess.run(['python', 'main.py', '-3', '-', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'

#TEST MULTIPLICATION
def test_bb_multiplication():
    result = subprocess.run(['python', 'main.py', '3', 'x', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '6\r\n' 

def test_bb_multiplication_reversed():
    result = subprocess.run(['python', 'main.py', '2', 'x', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '6\r\n'

def test_bb_multiplication_zero():
    result = subprocess.run(['python', 'main.py', '2', 'x', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'

def test_bb_multiplication_double_zero():
    result = subprocess.run(['python', 'main.py', '0', 'x', '0'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'

def test_bb_multiplication_negative():
    result = subprocess.run(['python', 'main.py', '2', 'x', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-6\r\n'

def test_bb_multiplication_one():
    result = subprocess.run(['python', 'main.py', '2', 'x', '1'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2\r\n'

def test_bb_multiplication_double_negative():
    result = subprocess.run(['python', 'main.py', '-3', 'x', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '9\r\n'

#TEST DIVISION
def test_bb_division():
    result = subprocess.run(['python', 'main.py', '6', '/', '3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2.0\r\n'
#Test fails, because result of division is in float type even for integer result values - it could be or not be a bug depending on the requirements. Example 6 / 3 = 2 (and not 2.0) in README suggests that it is
#E       AssertionError: assert '2.0\r\n' == '2\r\n'
#E
#E         - 2
#E         + 2.0
#E         ?  ++

def test_bb_division_reversed():
    result = subprocess.run(['python', 'main.py', '3', '/', '6'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0.5\r\n'

def test_bb_division_zero_over():
    result = subprocess.run(['python', 'main.py', '0', '/', '2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0\r\n'
#Test fails, because result of division is in float type even for integer result values - it could be or not be a bug depending on the requirements. Example 6 / 3 = 2 (and not 2.0) in README suggests that it is

def test_bb_division_negative():
    result = subprocess.run(['python', 'main.py', '4', '/', '-2'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '-2\r\n'
#Test fails, because result of division is in float type even for integer result values - it could be or not be a bug depending on the requirements. Example 6 / 3 = 2 (and not 2.0) in README suggests that it is

def test_bb_division_one():
    result = subprocess.run(['python', 'main.py', '2', '/', '1'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2\r\n'
#Test fails, because result of division is in float type even for integer result values - it could be or not be a bug depending on the requirements. Example 6 / 3 = 2 (and not 2.0) in README suggests that it is

def test_bb_division_double_negative():
    result = subprocess.run(['python', 'main.py', '-6', '/', '-3'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '2\r\n'
#Test fails, because result of division is in float type even for integer result values - it could be or not be a bug depending on the requirements. Example 6 / 3 = 2 (and not 2.0) in README suggests that it is

def test_bb_division_same():
    result = subprocess.run(['python', 'main.py', '6', '/', '6'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '1\r\n'
#Test fails, because result of division is in float type even for integer result values - it could be or not be a bug depending on the requirements. Example 6 / 3 = 2 (and not 2.0) in README suggests that it is

def test_bb_division_pi_approx():
    result = subprocess.run(['python', 'main.py', '7', '/', '22'], stdout=subprocess.PIPE)
    assert result.stdout.decode('utf-8') == '0.3181818181818182\r\n'

def test_bb_division_zero():
    result = subprocess.run(
        ['python', 'main.py', '1', '/', '0'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode != 0
    assert "ZeroDivisionError" in result.stderr

def test_bb_division_double_zero():
    result = subprocess.run(
        ['python', 'main.py', '0', '/', '0'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode != 0
    assert "ZeroDivisionError" in result.stderr


#TEST OPERATION (OP) Validations
def test_bb_op_type_list():
    result = subprocess.run(
        ['python', 'main.py', '1', '[+]', '1'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "TypeError" in result.stderr
#I think main() should check if the op value is a string and, if not, raise TypeError instead of the KeyError

def test_bb_op_empty():
    result = subprocess.run(
        ['python', 'main.py', '1', '', '1'],
        capture_output=True,
        text=True
    )
    assert result.returncode != 0
    assert "ValueError" in result.stderr
#I think main() should check if the op value is in set {+,-,x,/} and return ValueError instead of the KeyError

def test_bb_op_type_None():
    with pytest.raises(TypeError):
        subprocess.run(['python', 'main.py', '1', None, 'abcdef'], check=True)
 
