# Introduction to Python

Python is not only a language to write code but also a program (an interpreter) that you install globally on your computer. You can run the program passing in as input the name of your working python file ```python hello.py``` and the interpreter will handle the process of read the document, top to bottom and translating effectively to binary language.


## Functions, arguments and side effects
  ```py
  print('Hello World')
  ```

When looking at the example above, we can see that Python comes with pre-defined ```functions``` that have a default behavior. Functions are an action or a verb that lets you do something in the program. Functions can accept ```arguments``` where the user can choose the value to pass in. An argument is an input to a function that somehow influences its behaviour.

So this ```print()``` function has the ability to take as input a string of text that hold the information the user wants to print onto the screen. As a result -- or better known as  ```side effect``` -- to invoking this function, the program then prints onto the screen the piece of text the user passed in as argument.
\

## Variables
Variables are just a container for some value stored in memory.

  ```py
  name = input("What's your name?")
  print("Hello,", name)
  ```
\

## Comments and pseudocode
You can add comments in your code with the hash sign ```#```. When the program is hundreds of lines of code, you can add comments to highlight what each section is.

  ```py
  # This is a comment
  print('This is fun.')
  ```

Another great usage of the ```#``` is for pseudocoding. Pseudocode is used in plain english to express your train of thoughts. It allows you to outline your program in plain English and without code.
\

## Reading the Documentation
If you refer to the [official documentation](https://docs.python.org/3/library/functions.html#print) for the built-in functions in Python, you'll see the following syntax:
```print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)```
What this tells us is that you can customize how you want information to be printed on your Terminal. If you want the separation of each argument to be a different value than the default value, all you have to do is pass in the customized instructions as arguments to the function.
   ```py
   print('Hello', 'World', sep='-', end='.') 
   # prints "Hello-World."
   
   print('Hello', end=' ')
   print('World', end='.')
   # prints "Hello World." in one line
   ```


##  Printing strings

If you wish to print quotes:
   ```py
   print('Hello, "friend"') # prints Hello, "friend"
   print("Hello, \"friend\"") # also prints Hello, "friend"
   ```

Format strings or f-string tells the language to format variables with a special syntax. To enable the f-string, just add a lower case ```f``` to have your string formatted for f-string.
   ```py
   name = input("What's your name?")
   print("hello, {name}") # prints hello, {name}
   print(f"hello, {name}") # prints hello, Sabrina
   ```

Strings also have built-in functions, called ```methods```. Referencing the official documentation, we can find many methods that have different functionalities. You can access that functionality by using the name of a string(or a variable) and invoking it with parens.
   ```py
   # Ask user for their name
   name = input("What's your name?")

   # Remove whitespace from string
   name = name.strip() # this is the same as "Sabrina".strip()

   # Capitalize first letter of the input string
   name = name.capitalize()
   
   # Capitalizes first letters of all words in the input string
   name = name.title()

   # Say hello to user
   print(f"hello, {name}")
   ```

Instead of having several lines of code in order to modify the state of your input value, we can also __chain methods__ to have a cleaner and drier code.

   ```py
   name = input("What's your name?").strip().title()
   print(f"hello, {name}")
   ```
