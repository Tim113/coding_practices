## Python Coding Practises

In principle we will follow the PEP8 guidelines 

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

We will also try to follow R coding practises where relevant (unless they contradict with PEP8).

---

### Naming conventions

- All names should be short and descriptive 

- Function names should be lower-case with underscores
```python 
def my_function():
    ...
````

- Variable names should be lower-case with underscores and prefixed with a data type signifier
```python 
 a_long_name
```

- Constants should be in upper-case with underscorses
```python
A_CONSTANT
```

- Classes should be camel case
```python
MyClass
```

- Avoid camel case with underscores (eg My_Variable) and mixed case (eg myVariable).


### Comments

- Whole line commments should be complete sentences
```python
# This is a qhole line comment.
```

- Inline comments should be descriptive. They should be separated from code by four white spaces.
```python
x = x + 1    # Compensate for border
```

### Line breaks

- Line breaks within function arguments should be aligned with delimeter.
```python
def long_function_name(var_one, var_two,
                       var_three, var_four):
    ...
```

- Operands should come at the beginning of each new line
```python
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```

### Namespace

- Avoid importing whole module namespaces, eg
```python
from modu import *
```

### Other conventions

- No spaces between parameters in a function
```python
my_function(a='foo', b='bar')
```

- String hierarchy will be single quotes, then double quotes, then triple quotes.
```python
my_simple_string = 'hello'
my_complicated_string = "They said 'hello' to me."
my_very_complicated_string = '''The above statement reads "They said 'hello' to me."'''
```
