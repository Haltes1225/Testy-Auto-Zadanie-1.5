# Calculator app

This is a simple calculator app that can add, subtract, multiply and divide.
It works only with integers.

## Usage

```
$ python3 main.py <left_number> <operation> <right_number>
```

## Examples

```bash
$ python3 main.py 1 + 3
4
$ python3 main.py 1 - 3
-2
$ python3 main.py 2 x 3
6
$ python3 main.py 6 / 3
2
```

## Running tests

```bash
$ pytest
```

## Solution information

Blackbox tests are localised in test_app.py file within blackbox folder and can be grouped for execution thanks to their descriptive names, eg. 'pytest -k bb_multiplication' will run only blackbox tests for multiplication. Whitebox tests are localised in test_calc.py file within whitebox folder and can be grouped for execution analogously. Not all tests pass due to unexpected behaviour of the app and Calculator class - if a given test fails, I have put a comment under it to describe what I think is most probably a bug in the app/class.