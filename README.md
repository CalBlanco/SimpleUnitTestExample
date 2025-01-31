# SimpleUnitTestExample

Howdy NLPeers

Here is a quick example of implementing unit tests in python.

## Why Unit Test?

Unit testing is a excellent way to ensure your code functions properly. Creating unit tests allows us to make changes to our code with out having to guess if our changes have broken anything we were not expecting.


## Python's `unittest` module

Python has an amazing unit testing module called `unittest` which can be imported into any project via `import unittest`

https://docs.python.org/3/library/unittest.html 

You can read more about the capabilities on the above link.

### Basic Operation
First we want to create a file that will run our test code.

Within that file we will need to create a class that inherits the properties of `unittest.TestCase`

```
import unittest

class MyTestClass(unittest.TestCase):
    ...
```

Within this class we will define our test cases for our operations. The main unit test operation is `self.assertEqual`. This essentially means that we expeect the values passed to this function to be equal.


```
import unittest

class MyTestClass(unittest.TestCase):
    
    def test_add(self):
        sum = 1 + 1
        self.assertEqual(sum, 2, 'One and One should make Two')
```

There are a lot of different operations inherited by the `unittest.TestCase` that we can use such as `self.assertIn` which takes a value and an iterable to determine if the value is present in that iterable

```
import unittest

class MyTestClass(unittest.TestCase):
    
    def test_in(self):
        my_val = 'carl'
        iterable = ['john', 'zaza', 'carl']
        self.assertIn(my_val, iterable, 'Carl should be in the iterable')
```

I would recommend looking at some of the docummentation for `unittest` to determine which assertion functions you need or want to call. Their functions are comprehensive and you should be able to find what you need to perform whatever test you want 

## How should one write a unit test?

When we create functions or features we want to write unit tests that cover all of our bases. Tests should be written for successful operations of the code, as well as any kind of errors we might expect from improper use of the code.


## Test Driven Development

This is a pretty interesting and generally approved method of development. You start by writing a bunch of tests for the functionality you would like out of your code. Then you develop your code until all test cases pass as expected. 

Let's say I want to make a class that has a string and a number. I want to ensure that the number is an integer, and the string has at least 5 characters. Before I write my class I could write the unit tests for the class 

```
import unittest
from .MyClass import MyClass

class MyTestClass(unittest.TestCase):
    def setUp(self): #Set up is called before each test
        self.myClass = MyClass(1, 'wordssss')
    
    def test_is_integer(self):
        self.assertIsInstance(self.myClass.val_num, integer)
    
    def test_str_is_longer_than_5(self):
        self.assertTrue( (len(self.myClass.val_str) >= 5) )

```

Now running this code would generate errors because we have not implemented the class yet.

```
class MyClass():
    def __init__(self, val_num, val_str):
        self.val_num = val_num
        self.val_str = val_str
```

After running the tests we should see a correct output that lets us know we implemented our desired class correctly.

