# Introduction to Python

Python is not only a language to write code but also a program (an interpreter) that you install globally on your computer. You can run the program passing in as input the name of your working python file ```python hello.py``` and the interpreter will handle the process of read the document, top to bottom and translating effectively to binary language.


## Functions, arguments and side effects
  ```py
  print('Hello World')
  ```

When looking at the example above, we can see that Python comes with pre-defined ```functions``` that have a default behavior. Functions are an action or a verb that lets you do something in the program. Functions can accept ```arguments``` where the user can choose the value to pass in. An argument is an input to a function that somehow influences its behaviour.

So this ```print()``` function has the ability to take as input a string of text that hold the information the user wants to print onto the screen. As a result -- or better known as  ```side effect``` -- to invoking this function, the program then prints onto the screen the piece of text the user passed in as argument.


## Variables
Variables re just a container for some value stored in memory.

  ```py
  name = input("What's your name?")
  print("Hello, ", name)
  ```

## Comments
You can add comments in your code with the hash sign ```#```.
  ```py
  # This is a comment
  print("This is fun.")
  ```
