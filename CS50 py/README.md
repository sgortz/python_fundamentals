# Introduction to Python

Python is not only a language to write code but also a program (an interpreter) that you install globally on your computer. You can run the program passing in as input the name of your working python file ```python hello.py``` and the interpreter will handle the process of read the document, top to bottom and translating effectively to binary language.

## Interactive Mode

Python also supports __interactive mode__, where you can write code and immediately execute interactively. This is specially useful because sometimes you don't want to save lines of code, you're just looking for quick answers. To enable the interactive mode, you need to install Python locally on your computer and have access to the Terminal in order to open the Python IDE, with the command ```python```. To terminate the session, just type ```control + d```.


## Functions, arguments and side effects

  ```py
  print('Hello World')
  ```

When looking at the example above, we can see that Python comes with pre-defined ```functions``` that have a default behavior. Functions are an action or a verb that lets you do something in the program. Functions can accept ```arguments``` where the user can choose the value to pass in. An argument is an input to a function that somehow influences its behaviour.

So this ```print()``` function has the ability to take as input a string of text that hold the information the user wants to print onto the screen. As a result -- or better known as  ```side effect``` -- to invoking this function, the program then prints onto the screen the piece of text the user passed in as argument.


## Reading the Documentation

If you refer to the [official documentation](https://docs.python.org/3/library/functions.html#print) for the built-in functions in Python, you'll see the following syntax:
```print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)```\
What this tells us is that you can customize how you want information to be printed on your Terminal. If you want the separation of each argument to be a different value than the default value, all you have to do is pass in the customized instructions as arguments to the function.

   ```py
   print('Hello', 'World', sep='-', end='.') 
   # prints "Hello-World."
   
   print('Hello', end=' ')
   print('World', end='.')
   # prints "Hello World." in one line
   ```


## Variables
Variables are just a container for some value stored in memory.

  ```py
  name = input("What's your name?")
  print("Hello,", name)
  ```


## Comments and pseudocode

You can add comments in your code with the hash sign ```#```. When the program is hundreds of lines of code, you can add comments to highlight what each section is.

  ```py
  # This is a comment
  print('This is fun.')
  ```

Another great usage of the ```#``` is for pseudocoding. Pseudocode is used in plain english to express your train of thoughts. It allows you to outline your program in plain English and without code.


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



## Integers and floats

Integers, just like strings and functions, also have __built-in methods__. Floats are numbers with decimal points. It takes the name from "floating point" values.

```py
x = input("What's x?") # 1
y = input("What's y?") # 2

print(x + y) # prints 12
print(int(x) + int(y)) # prints 3

# Option 2:
x = int(input("What's x?")) # 1
y = int(input("What's y?")) # 2
print(x + y) # prints 12
```

```round(number[,ndigits])``` usually square brackets in documentations mean something optional. This means you can specify the number of digits you want to round your number to. 

```py
x = int(input("What's x?")) # 999
y = int(input("What's y?")) # 1
z = x + y

print(z) # prints 1000
print(f"{z:,}") # prints 1,000
```
This is the way to tell python to add commas to long numbers. You can switch to dots depending on the country you're in. 

```py
x = float(input("What's x?")) # 2
y = float(input("What's y?")) # 3

z = x / y
print(z) # prints 0.6666666666...

z = round(x / y, 2) # specifying 2 digits after the floating point
print(z) # prints prints 0.67

z = x / y
print(f"{z:.2f}") # also prints 0.67
```

## Function definition
```py
def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name?")
hello(name)
```

Scope is the location where a variable's value is valid or where it's available for you to use.


## Conditionals
Python comes with built-in syntax previously introduced to us by Math that allows for the program to have conditionals of truthness or falsiness.

```py
>  # greater than
>= # greater than or equal to
<  # less than
<= # less than or equal to
== # equal to
!= # not equal to

print(1 < 2) # prints True
print(10 == 20) # prints False

and # conjuction of conditionals
or  # choice between one of the conditionals

if 
elif
else

```

## Loops

### ```while``` Loop
This loop allows me to repeat an action while the loop conditional still evaluates to ```True```.\

   ```py
   i = 0

   while i < 4:
       print("Meow")
       i += 1
       # note how in Python i++ or i-- doesn't exist like in JS, C, or C++

   ```

__Note:__ If you find yourself in an infinite loop, ```control + c``` for _cancel_, or _interrupt_ should terminate the session.

### ```for``` Loop
This loop is commonly used to iterate through collections, such as Lists and Dictionaries.

   ```py
   for i in [0, 1, 2]:
       print("Meow")
   ```

__Note:__ There's a convention in Python where if you need a variable just because the built-in feature requires it to do some sort of counting that is useless to the program, a pyhtonic refactoring would be to rename the useless variable with ```_```.

   ```py
   for _ in range(3)
      print("meow")

   # Alternately, you can also perform math expressions to repeat strings
   print("meow" * 3)

   # Printing "meow" as many times as the user wants:
   while True:
      n = int(input("What's n? "))
      if n > 0:
          break

   for _ in range(n):
        print ("meow")
   ```

## Lists
It's another data type in Python, to contain multiple values in one place.

## Debugging
You can always use ```print()``` to see in the terminal window your variables. But this option isn't always the best one. Some IDE comes with __built-in debuggers tools__ to help you solve your bugs, including VS Code.
1. __breakpoints__: A mechanism that allows us to specify on what line(s) you want to pause or break in your code to get a better look. It slows down the execution of the program.
2. When adding breakpoints in VS Code, you need to run the debugger. Click __Run and Debug__ or ```command + shift + d``` \
   a. The __continue__ button, is for the code to continue on to the end of the program.\
   b. Next, is the __step over__ button, this would allow me to step over the current line executing it, but not going inside the function.\
   c. The __step into__ steps inside the function and continue step-by-step, line-by-line of the code.\
   d. The __step out__ button steps out of the function the thread of execution is currently in.
3. You can see the variable environment of your program in the local and global tabs.

## Style Guide
Mostly all Python programmers adhere to (or are expected to adhere to) the PEP 8 style of code. __Python Enhancement Proposal__ (or PEP) is a set of proposal that the community comes up to codify certain standards. PEP 8 tries to standardize what our code should look like. 
Sometimes your code might not have bugs, but it's harder to maintain or it is prone to bugs down the line. So it's a good thing that your code is properly formatted. For more details, visit [PEP 8 Official Documentation](peps.python.org/pep-0008/).
How do you go about styling your code?
- Indentation
- Tabs or spaces?
- Maximum Line Length
- Blank Lines
- Imports

In the Python world, there is no tabs, and the indentation is 4 spaces. White spaces are encouraged for better visualization of blocks of code.

The most common linter for Python is called [_pylint_](https://pypi.org/project/pylint/) and can be install with the command ```pip install pylint```. A little less noisy program is called [_pycodestyle_](pycodestyle.pycqa.org) which follows the de facto standard within the python community for formatting your code. It takes care of reformatting your code for you. Another alternative that is gaining more popularity is [_black_](black.readthedocs.io). This is a program that you can install with pip as well: ```pip install black```, and it is a little more opinionated than the previous options.