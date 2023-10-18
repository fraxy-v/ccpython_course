## Basic Python Notes

1. Hello world program
1. Program flow 
   - Program draw tree
   - Python runs line by line:
   - expression - a piece of code that produces a value
   - strings
1. Variable
   - variable - temporarily store data in computer's memory.
   - when python executes $a = 5$ expression, allocates memory, stores the data into the memory, attaches the label to that memory (identifier)
   - types: integer number, floating point number, boolean values, string
   - Exercise: define and print variable for name, age, boolean flag.
1. Input from user
   - What is your name program
   - build-in functions
   - Exercise : favorite color,
1. Type conversion,
   - Program computes age
   - errors
   - `int()`, `float()`, `bool()`
   - `type()`
   - Exercise: input kg, output pounds
1. Strings:
   - ' inside string use ", " inside string use '
   - ''' for multiline strings
   - + operator, * int
   - indexing [], negative index!!
   - slicing with `:`, e.g. `[0:3]`, excludes last, start index and end index if missed
   - Question: what is the result of `[1:-1]`
   - formatted string, generates strings, better than + for complex expression, works with placeholders, e.g. `f'{var1} text {var2}'`
   - function `len` - general purpose
   - `.` operator, methods difference function <> method
   - Exercise: find method `upper`, `lower`, `title`
   - Question: does upper change the value of the variable (intellisense helps)
   - method `find`,search for occurrence of string
   - Question: what does it return on failure, is it case sensitive
   - method `replace`
   - `in` operator, very similar to find
   - Question: what is the type of the result of `in` operator?
1. Arithmetic operations and math functions
   - `int` and `float` types
   - `+/-/*` operators
   - several type of division operations: `/` floating point result, `//` whole number, `%` modulus
   - power operator `**`
   - augmented assignments
   - Exercise: compare result of augmented assignments
   - Question: `10 + 3 * 2 ** 2`. What is the precedence of the operators above?
   - built-in `round` and `abs`
   - What is a module? A separate file with reusable code. Modules are used to organize the code into files.
   - methods in the module are accessed with the `.` operator
   - Question: `math.ceil`; `math.floor`; `math.fabs` vs `abs`
   - Exercise: google "python 3 math module", spend 5 min browsing through the functions
1. `if` statement
   - code block refers to a collection of code that is in the same block or indent. This is most commonly found in classes, functions, and loops.
   - Exercise: if `is_hot` output that "It's a hot day". On new line: "Drink plenty of water." Else if its `is_cold` output "It's a called day. Wear warm clothes." Otherwise output "It's a lovely day." And finally "Enjoy your day."
   - logical and operator : combining two conditions, both have to be `true`, example `is_sunny` and `is_average_temperature`
   - logical `or`, either has to be `true`, example `is_sunny` or `is_average_temperature`
   - logical `not`, inverts the value, example `is_sunny` and `not is_windy`
   - comparison operators: boolean expression that compares values
   - Question: Guess all comparison operators? (>,<,>=,<=,==,!=)
   - Exercise: same as above but with temperature
   - Exercise: input name. `if len < 3` output invalid name, too short, `if len > 30` print invalid name, too long, otherwise valid
   - Exercise: Enter weight. Answer Question (L)bs or (K)gs? and convert to the other, should not be case sensitive.
1. While loop
   - Loops are used to execute a block of code multiple times
   - In the while loop the block is executed as long as the condition is `True`
   - Example: print `i` from 1 to 5
   - Question: what will happen if we don't increase i?
   - Exercise: Step through the loop with the debugger.
   - Exercise: Draw half of a pine tree.
   - Break and Continue statements: skip steps with `continue`, `break` loop
   - Loops can have `else`
   - Exercise: Build a guessing game. (use `random.randrange(1, 10)`)
   - Exercise: Build a car game (commands: start, stop, help, quit)
1. For loop
    - More convenient to iterate over items in a collection
    - Loop variable: holds item for the current iteration
    - Example: `for character in 'Python'`...
    - Example: `for name in ['Name 1' , 'Name 2', ...]`
    - Example: `for num in [1, 2, 3, ...]`
    - Range function: creating range of numbers. It's not a list, but it's an iteratable object. Takes also beginning of the range, and step
    - Exercise: Calculate the sum of the elements of a list
    - Exercise: Nested loops, chess board coordinates
    - Exercise: Step through the nested loops
    - Exercise: Write the letter F with numbers
1. Lists
    - Exercise: define a list of names and print it in the terminal
    - Individual elements can be accessed with indexing (remember negative indices?)
    - Slicing, selecting a range
    - Exercise: Find the largest number in a list
    - 2 dimensional lists: define a matrix
    - Exercise: use nested loops to iterate over the matrix and print each element
    - Question: remember the difference between function and method?
    - `append` method, adds an item to the end
    - `insert` method, adds an item to specified position
    - `remove` method, removes first occurrence
    - `clear` method, removes all items
    - `pop` method, removes last item
    - `index` method, checks existence of item, value error if not found
    - `in` operator, similar but boolean result
    - `count` method, counts occurrences
    - `sort`, `reverse` methods
    - Question: Assign the list to another variable and modify an element. Does it affect the list? Now try `copy` method.
    - Exercise: Collect duplicates from one list in another list
1. Tuple
    - Similar to list, storing a list of items. Defined with '()' unlike list '[]'
    - But tuples are immutable.
    - Question: Define a tuple. Check the methods of a tuple. Do we have `append`, `insert`
    - Question: What methods are there (similar to lists)? Do you remember what can we do with `count` and `index`
    - Question: can we index a tuple with []?
    - Question: can we modified a value from the tuple?
    - This is useful for defining constants.
    - Unpacking of tuple: `x,y,z = coordinates`
    - Question: Can you unpack a list?
7. Set and Dictionary
   - Set is a collection of unique values. Defined with '{}' rather than '[]' or '()'.
   - Question: What is the type of a variable defined with empty '{}'? For empty sets call `set()`.
   - Question: Define a set with three equal values. Can you unpack it to three different variables?
   - Exercise: Similar to above. Collect all unique elements from a list to into a set.
   - Similar to set. Dictionary stores information as pairs of (unique!) key and value.
   - Dictionary is a collection of data, useful because can represent real world entities.
   - Question: Can we have keys of different types?
   - Access with '[]', throws a key error if no such key.
   - '[]' can be used to define a new key value pair however.
   - `get` method doesn't throw, returns a `None` object or default value.
   - Exercise: Convert a number to words
   - Exercise: Emoji converter (use split method, converts string to list, '\U0001F642' smiling face, '\U0001F641')
1. Functions
   - We need functions to: reuse code and for readability (to break the code into manageable chunks)
   - A function is a way to contain code that performs a specific task
   - Question: which built-in functions do you remember? What is the purpose of each of these functions?
   - Example: function for saying hallo
   - `def` key word, followed by function name and () and :. Always use well chosen descriptive names
   - Best practices for formatting python code: Two lines after function end.
   - Question: Do the expression in the function body get executed if the function is not called?
   - Exercise: Use the debugger
   - Question: What will happen if we call the function before it's defined.
   - Question: What is the difference between the defined function and built-in print
   - Function parameters are used to pass information to the function. They are placeholder for receiving information.
   - Parameters act like local variables.
   - Exercise: call the defined function with two different parameters.
   - Question: What will happen if you call the function without an argument?
   - Exercise: add a second parameter
   - Positional arguments: the position or order is important
   - Exercise: reverse the order and observe the result.
   - Keyword arguments: the position doesn't matter
   - Normally we use positional arguments, sometimes keyword arguments improve readability
   - Keyword arguments always come after positional arguments.
   - Functions can also return values with `return` statement.
   - Exercise: write a function that computes the square of a number
   - Exercise: extract the emoji converter code into a function
1. Exceptions
   - Question: Write a program that asks for the age of the user and converts it to `int`. What is the exit code of the program? What if we enter invalid number?
   - We should anticipate errors and handle them, don't let the program crash
   - Use `try-except` construct to handle errors
   - In the `try` block we write the code that we expect to not be safe
   - In the `except` block we write the code that deals with a specific error
   - We can have many `except` blocks for each error type
   - Exercise: compute chance to go to Mars by a formula (1/age)
   - If no error in `except` is specified, we catch all errors.
1. Modules revisited
    - Module: A file with python code.
    - Modules are used to organize the program source code into files. Each files contains functionality that is logically grouped together
    - Also we can reuse code by importing modules in different parts of the project.
    - Exercise: write two functions for converting pounds to kg and vice versa in a module and import from another py file
    - Import specific functions from a module
    - A package is a container for multiple modules. It's basically a folder with files (modules).
    - It contains a special python file `__init__.py`
    - Exercise: add a new directory move the converter module and import from another python file.
    - Exercise: try importing the whole module, a function, a list of functions
1. Misc
   - Google: 'python 3 module index'
   - pathlib module: `absolute()`, `exist()`, `mkdir()`, `rmdir()`, `glob()` - "accepts search pattern", `open()` - reading and writing
   - `with` statement: makes sure that a file handle is closed `with open('filename') as f:`
   - Regular expressions.
1. Classes
   - Classes are used to define new types. Data + methods for handle the data
   - `class` keyword
   - `def` keyword for defining methods
   - Example: define a new Point type with 'move' and 'draw' methods
   - add attributes the objects by simply initializing them
   - Constructor: a function that is called when creating a object
   - `def __init__` to define a custom constructor
   - We are initializing attributes to the current object using `self`
   - We can inherit classes, parent class put in '()'
   - Methods and attributes of the parent are passed to the new type
