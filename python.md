## Python Coding Practises

In principle we will follow the PEP8 guidelines 

[https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)

We will also try to follow R coding practises where relevant (unless they contradict with PEP8).

---

- Functions should be all lower case with underscores separating words
```python 
def my_function():
    ...
````

- Variable names should be broken with underscores and prefixed with a data type signifier
```python 
 a_long_name
```

- Constants should be in all caps
```python
A_CONSTANT
```

- No spaces between parameters in a function
```python
my_function(a='foo', b='bar')
```

- String hierarchy will be single quotes, then double quotes, then triple quotes.
```python
my_simple_string = 'hello'
my_complicated_string = "They said 'hello' to me."
my_very_complicated_string = '''The above statement reads "They said 'hello' to me."''''
```
