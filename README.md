# Python Week 1 Notes


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

# Factorial exercise
```bash
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0 :
        return None
    if num == 0:
        return 1
    if num%2 == 0:
        return num * factorial(num-1)
```

# 3. BASIC DATA TYPES
  # Ints and Floats
  - we use int class to convert value to integer ( whole number)
  - converting from one type to another is called casting
  - Python does not round floats to integer when casting
  ``` bash
  Int(8.9) # outputs 8
  ```
  - round function can mitigate the approximation and rounding errors from floats calculations
  - The Int class -> you can pass string and convert it to an integer
                  -> you can also pass a second arguments which represents a base of the first argument and the class will convert it from the given base to base 10

    ```bash
   Int('100') # outputs 100
   Int('100' , 2 ) # outputs 4
   ```
  - The Decimal class -> you can pass in a value and decimal object will with decimal place for the given precision
                      -> good practise is to pass in a float as a string to prevent the float to be added all leading digits of the float. 
   ```bash
   getcontext().prec=2
   Decimal(1)/Decimal(3)  # outputs 0.33
   Decimal('3.14') # outputs 3.14
   ```

    # Booleans
    - Integers anything except 0 is true, therefore float 0 and imaginary 0 is false
    - Strings anything other than empty string is true, therefore '' is false
    - Data structures empty list or dictionary is false,

   # Strings
   - string slicing is taking a portion of a string and returning it e.g "My name is Iron-Man" string[0:7] *returns* My name
   - F-strings allows to insert variables and expression inside curly brackets in a string. e.g f'My Number is : {5}'
   - also with f-string we can do rounding and number formatting e.g f'Pi is: {math.pi:.2f}'    and    'Pi is: {}'.format(math.pi)

   # Bytes
   - is a sequence of data
     ```bash
     Bytes(4) # creates empty bytes object 4b long
     smiley = Bytes('*emoji*', 'utf-8') # creates bytes object with data
     smiley.decode('utf-8') # decode function to turn a bytes object back into a string
     ```
     - Bytes objects are immutable(cannot be modified)


# 4. BASIC DATA STRUCTURES
  # Lists
  - list slicing is same as string slicing
  - a third value can be used to control the step e.g mylist[start : end : step]
  - negative values is to step backwards through the list
  - to add item to end of list use append()
  - to insert item aat specific position use insert(*position, value*)
  - 2 ways to remove -> remove() removes item based on value, no index
                     -> pop() removes and return item at the end of list
  - when we assign a list to a variable, the variable stores a reference to the list, if we modify the list through one variable, the changes will reflect in other variables that reference the same list.
  - For list changes on one list to another dont reflect we use copy() method

  # sets
  - is defined using curly brackets
  - also defined by passing any iterable object in the cinstructor
  ```bash
  myset = { 'a', 'b', 'c'}  # curly brackets
  myset = set(('a', 'b', 'c')) # constructor
  ```
  - used to remove duplicates, as sets only contains unique values
  - you cannot access elements in a set using index or slicing
  - add elements using add() and remove using discard()
  # Tuples
  - declared with parenteses and are ordered
  - tuples are immutable( cannot be modified)
  - more memory effecient than lists


  # Dictionary
  - stores values in key : value pairs
  - values can be any data and duplicated, whreas keys cannot be repeated and must be immutable
  - resulting object for .keys() is immutable, to change this object, you need to convert it to a list
  ```bash
  
  ```


  # List Comprehensions
  -  
