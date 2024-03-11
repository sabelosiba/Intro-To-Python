# Python-week1
notes

# Variables and Types
- variable is the basic unit of a program
- integers -> whole numbers
- floats -> decimal numbers
- complex numbers
- strings -> collection of characters, plus "+" used to concatenate strings.
- Booleans -> true or false

# Data structures
- allow for the storage of a list of values in a single variable.
  # List
  - contains any data type
  - length function used to determine the length of the list
  ``` bash
  mylist = [ 1, 'list', true, []]

  len(mylist)
  ```

  # Set
  - Similar to list but only contains unique elements
  - declared using curly braces
  - orde of elements not important
  ``` bash
  mylist = { 1, 2, 3, 4}
  ```

  # Tuples
  - similar to list, but cannot be modified once declared.
  - useful when storing large amount of data

  # Dictionary
  - is a collection of key-value pairs.
  - declared using curly braces
  - accessed using keys

# Operators
- are instructions that perform operations on variables and values
  # Arithmetic
  - Addition (+), Multiplication (*), Division (/) *returns float*, modulus or Remainder (%)
  # comparison
  - evaluates two variables or values and returns a boolean
  # Logical
  - "and" , "or" , "not"
    
# Control flow
- if statement allows you to execute a block of code only if certain condition is met.
- else statement will be executed if condition is false.
- for loop is used to iterate over a list or an iterable objects

# Functions
- is like a machine that takes in inputs and produce output
- 'def' used to define functions
- 'return' used to specify output
- 'None' represent the absence of a value, and it is default return value for functions that explicitly does return anything

# Classes and Objects
- CLASSES -> help label and organize related functions and atrributes
          -> we define a class with uppercase letter name
          -> we create an initialisation function that get called every time an instance of a class is created.  
