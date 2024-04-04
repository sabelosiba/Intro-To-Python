<details>
<summary> Week 1 </summary>
<br>

# Python Week 1 Notes  
## Variables and Types
- variable is the basic unit of a program
- integers -> whole numbers
- floats -> decimal numbers
- complex numbers
- strings -> collection of characters, plus "+" used to concatenate strings.
- Booleans -> true or false

## Data structures
- allow for the storage of a list of values in a single variable.
  ### List
  - contains any data type
  - length function used to determine the length of the list
  ``` bash
  mylist = [ 1, 'list', true, []]

  len(mylist)
  ```

  ### Set
  - Similar to list but only contains unique elements
  - declared using curly braces
  - orde of elements not important
  ``` bash
  mylist = { 1, 2, 3, 4}
  ```

  ### Tuples
  - similar to list, but cannot be modified once declared.
  - useful when storing large amount of data

  ### Dictionary
  - is a collection of key-value pairs.
  - declared using curly braces
  - accessed using keys

## Operators
- are instructions that perform operations on variables and values
  ### Arithmetic
  - Addition (+), Multiplication (*), Division (/) *returns float*, modulus or Remainder (%)
  ### comparison
  - evaluates two variables or values and returns a boolean
  ### Logical
  - "and" , "or" , "not"
    
## Control flow
- if statement allows you to execute a block of code only if certain condition is met.
- else statement will be executed if condition is false.
- for loop is used to iterate over a list or an iterable objects

## Functions
- is like a machine that takes in inputs and produce output
- 'def' used to define functions
- 'return' used to specify output
- 'None' represent the absence of a value, and it is default return value for functions that explicitly does return anything

## Classes and Objects
- CLASSES
  - help label and organize related functions and atrributes
  - we define a class with uppercase letter name
  - we create an initialisation function that get called every time an instance of a class is created.

## Factorial exercise
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

## 3. BASIC DATA TYPES
  ### Ints and Floats
  - we use int class to convert value to integer ( whole number)
  - converting from one type to another is called casting
  - Python does not round floats to integer when casting
  ``` bash
  Int(8.9) # outputs 8
  ```
  - round function can mitigate the approximation and rounding errors from floats calculations
  - The Int class
    - you can pass string and convert it to an integer
    - you can also pass a second arguments which represents a base of the first argument and the class will convert it from the given base to base 10

   ```bash
     Int('100') # outputs 100
     Int('100' , 2 ) # outputs 4
   ```
  - The Decimal class
    - you can pass in a value and decimal object will with decimal place for the given precision
    - good practise is to pass in a float as a string to prevent the float to be added all leading digits of the float. 
   ```bash
     getcontext().prec=2
     Decimal(1)/Decimal(3)  # outputs 0.33
     Decimal('3.14') # outputs 3.14
   ```

  ### Booleans
    - Integers anything except 0 is true, therefore float 0 and imaginary 0 is false
    - Strings anything other than empty string is true, therefore '' is false
    - Data structures empty list or dictionary is false,

   ### Strings
   - string slicing is taking a portion of a string and returning it e.g "My name is Iron-Man" string[0:7] *returns* My name
   - F-strings allows to insert variables and expression inside curly brackets in a string. e.g f'My Number is : {5}'
   - also with f-string we can do rounding and number formatting e.g f'Pi is: {math.pi:.2f}'    and    'Pi is: {}'.format(math.pi)

   ### Bytes
   - is a sequence of data
     ```bash
     Bytes(4) # creates empty bytes object 4b long
     smiley = Bytes('*emoji*', 'utf-8') # creates bytes object with data
     smiley.decode('utf-8') # decode function to turn a bytes object back into a string
     ```
     - Bytes objects are immutable(cannot be modified)


## 4. BASIC DATA STRUCTURES
  ### Lists
  - list slicing is same as string slicing
  - a third value can be used to control the step e.g mylist[start : end : step]
  - negative values is to step backwards through the list
  - to add item to end of list use append()
  - to insert item aat specific position use insert(*position, value*)
  - 2 ways to remove
    - remove() removes item based on value, no index
    - pop() removes and return item at the end of list
  - when we assign a list to a variable, the variable stores a reference to the list, if we modify the list through one variable, the changes will reflect in other variables that reference the same list.
  - For list changes on one list to another dont reflect we use copy() method

  ```python
  # Creating a list
  my_list = [1, 2, 3, 4, 5]
  my_list = list(range(0,6))  # using list class construtor

  # Accessing elements
  print(my_list[0])  # Output: 1
  print(my_list.get(0))  # Output: 1

  # Modifying elements
  my_list[1] = 10
  print(my_list)  # Output: [1, 10, 3, 4, 5]

  # Appending elements
  my_list.append(6)
  print(my_list)  # Output: [1, 10, 3, 4, 5, 6]
  my_list.insert(2, 3)
  print(my_list)  # Output: [1, 10, 3, 3, 4, 5, 6]

  # Removing elements
  my_list.remove(3)  
  print(my_list)  # Output: [1, 10, 3, 4, 5, 6]
  print(my_list.pop())  # Output: 6
  print(my_list)  # Output:  [1, 10, 3, 4, 5]
  ```

  ### sets
  - is defined using curly brackets
  - unordered collections of unique elements, mutable
  - also defined by passing any iterable object in the cinstructor
  - used to remove duplicates, as sets only contains unique values
  - you cannot access elements in a set using index or slicing
  - add elements using add() and remove using discard()
  ```python
  # Creating a set
  my_set = {1, 2, 3, 4, 5}  # curly brackets
  my_set = set([1, 2, 3, 4, 5]) # using constructor
  
  # Adding elements
  my_set.add(6)
  print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
  
  # Removing elements
  my_set.remove(3)
  print(my_set)  # Output: {1, 2, 4, 5, 6}
  my_set.discard(4)
  print(my_set)  # Output: {1, 2, 5, 6}
  ```

  ### Tuples
  - declared with parentheses and are ordered
  - tuples are immutable( cannot be modified) that can store multiple elements
  - more memory effecient than lists
  - Tuples are suitable where the data should not be modified once defined.
  - the elements in the tuple cannot be added or removed once created. 
  ```python
  # Creating a tuple
  my_tuple = (1, 2, 3, 4, 5)
  my_tuple = tuple([1, 2, 4, 5, 6]) # Creating a Tuple with list by construtor

  # Accessing elements
  print(my_tuple[0])  # Output: 1

  # Tuple unpacking
  a, b, c, d, e = my_tuple
  print(c)  # Output: 3
  ```

  ### Dictionary
  - stores values in key : value pairs
  - values can be any data and duplicated, whreas keys cannot be repeated and must be immutable
  - resulting object for .keys() is immutable, to change this object, you need to convert it to a list
  ```python
  # Creating a dictionary
  my_dict = {'name': 'John', 'age': 25, 'country': 'USA'}

  # Accessing values
  print(my_dict['name'])  # Output: John
  print(my_dict.get('name'))  # Output: John

  # Modifying values
  my_dict['age'] = 26
  print(my_dict)  # Output: {'name': 'John', 'age': 26, 'country': 'USA'}
 
  # Adding new key-value pairs
  my_dict['occupation'] = 'Developer'
  print(my_dict)  # Output: {'name': 'John', 'age': 26, 'country': 'USA', 'occupation': 'Developer'}

  # Removing key-value pairs
  del my_dict['country']
  print(my_dict)  # Output: {'name': 'John', 'age': 26, 'occupation': 'Developer'}
  ```


  ### List Comprehensions
  - consists of square brackets cotaining the expression, which is executed for each element along the for loop to iterate over each element, while returning a copy of the list.
  - Syntax : *newCopyList = [ expression(element) for element in oldList if condition]*
  - it enables you to filter / apply functions to every item in a list.

  ```python
  numbers = [12, 13, 14,] 
  doubled = [x *2  for x in numbers] 
  print(doubled)  # Outputs [24, 26, 28]

  # with conditions or filters and nested
  list = [i for i in range(11) if i % 2 == 0] 
  print(list)  # Outputs [0, 2, 4, 6, 8, 10]

  myString= 'My Name is Ryan Mitchell. I live in Boston'
  cleanWord = [[word for word in sentence.split()] for sentence in myString.split('.') ]
  print(cleanWord)  # Outputs [['My', 'Name', 'is', 'Ryan', 'Mitchell'], ['I', 'live', 'in', 'Boston']]
  ```

  ### Dictionary and Comprehensions
  - used to create a new dictionary from an itearble structure
  - Syntax : *dict = { key:value for (key,value) in Iterable}*

  ```python
  # dict to represent keys and values
  original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
   
  # Inverting the dictionary using dictionary comprehension
  inverted_dict = {value: key for key, value in original_dict.items()}  
    
  print (inverted_dict)  # Outputs {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

  sDict = {x.upper(): x*3 for x in 'coding '}
  print (sDict)  # Outputs {'O': 'ooo', 'N': 'nnn', 'I': 'iii', 'C': 'ccc', 'D': 'ddd', 'G': 'ggg'}
  
  # Python code to demonstrate dictionary 
  # comprehension using if.
  newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
  print(newdict)  # Outputs {0: 0, 8: 512, 2: 8, 4: 64, 6: 216}
```


## 5. Basic Control Flow
  ### If and Else
  - are conditional statements, which decide the direction of the flow of program execution
  - if-statement is used to decide whether a certain block will be executed or not
  ```bash
      # if statement Syntax
      if condition:
        # Statements to execute if
        # condition is true

      # if-else statement Syntax
      if (condition):
        # Executes this block if
        # condition is true
      else:
        # Executes this block if
        # condition is false

      # if-elif-else Syntax
      if (condition):
        statement
      elif (condition):
        statement
      .
      .
      else:
        statement
  ```

   ### While
   - is used to execute a block of statements repeatedly until the condition is meet.
   - when the condition becomes false, the line immediately after the loop is executed
   ```bash
      # Syntax of While loop
       while expression:
          statement(s)
   ```
   - break statement will exit the loop and move to next line of code outside the loop
   
   ```bash
      # break statement     
      # break the loop as soon it sees 'e'
      i = 0
      a = 'geek'
  
      while i < len(a): 
        if a[i] == 'e' : 
          i += 1
          break
          
        print('Current Letter :', a[i]) 
        i += 1

   ```
   - *Outputs* -> Current Letter : g
     
   - continue statement will skip over any lines within the loop that comes after it and jump back to loop to start the next iteration
  ```bash
      # continue statement           
      # Prints all letters except 'e' 
      i = 0
      a = 'geek' 
      while i < len(a): 
        if a[i] == 'e': 
          i += 1
          continue
          
        print('Current Letter :', a[i]) 
        i += 1
   ```
   - *Outputs* -> Current Letter : g
                  Current Letter : k

  ### For Loop
  - it is used for iterating over an iterable like String, Tuple, List, Set, or Dictionary
  ```bash
   # for loop syntax
   for var in iterable:
    # statements
  ```
</details>


<details>
<summary> Week 2 </summary>
<br>

# Python Week 2 Notes - Fundamentals
## 1. Basic Functions
  ### Functions
  - is a block of statements to return a specific task.
  - composed of a name and parameters, denoted by def keyword
  - Function Syntax - *def function_name(parameters):*
  - types of function arguments
    - named parameters ( Default arguments), positional arguments and *args and **kwargs

  ### Name parameters
  - is parameter that assumes a default value if value is not provided in then function call for that argument.
  - Onced a function has default argument, all the arguments to its right must also have default values.

  ### *args
  - is used to pass a variable number of arguments to a function.
  - uses the asterisk symbol(*) before the argument name to create a pointer to the inputted variables.
  - Syntax : def function_name( *args ):

  ### **kwargs
  - is used to pass through keyword arguments
  - a keyword argument is where you provide a name to the variable as you pass it into function.
  - printing kwargs to see that the keyword arguments are stored in a dictionary, because keyword arguments have keys and values passed in any order.
  - 

  ### Variable and scope
  - locals function
    - allows us to access all varibles within a python function returns a dictionary.
    - cannot reference a variable outside its scope and cannot modify the data of variable
  - globals function
    - returns the dictionary of all gloabal variables
    - we can also change the value of global variables using globals function.

  ### Functions as variables

## Classes and Objects Fundamentals
  - An Object is an instance of a class, A class is a blueprint while an instance is a copy of a class with actual values.
  ```python
  class Dog:
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)

  Rodger = Dog()
  print(Rodger.attr1) # Outputs mammal
  Rodger.fun()  # Outputs I'm a mammal
                #         I'm a dog
  ```  
  ### Static Attributes
  - also called class variable

  ### Python Inheritance
  - allows us to define a class to inherit all the methods and properties from another class
  - the inheritance process happens automatically when child class is created.
  - if the child class defines an attribute/method the same as parent class, the child will overwrite the parent's version.



## 3. Error Handling Fundamentals
  ### Handling errors and Exceptions
  - Try and except statements are used to catch and handle exceptions in python.
  - Syntax
  ```python
  try:
      # Some Code....  
  except:
      # Handling of exception (if required)
  else:
      # execute if no exception
  finally:
      # Some code .....(always executed)
  ```
  - Catching Exceptions by Type, eg ZeroDividionError, TypeError, SyntaxError and IOError
  - 

## 4. Threads and Prosses
  ### Fundamentals of Threads and Processes
  - computers have both memory and file storage
  - The OS is responsible for allocating memomry to wach process, so it puts walls between processes for them not to access each other's memory.
  - A process can have multiple threads and execute code at the same time in parallel.
  - A process is an instance of a computer program that is beigng executed.
  - A thread is an entity within a process that is scheduled for execution.
  - multiple threads can be scheduled in one process
  - Multithreading is the ability of a processor to execute multiple threads concurrently, In single core CPU its achieved by context switching.
  ```python
  #import 
  import threading
  # calculate cube of a number
  def cubef(num):
    print(f'Cube of {num} is {num*num*num}')

  # creating a thread
  t1 = threading.Thread(target=cubef, args=(5,))
  t2 = threading.Thread(target=cubef, args=(25,))

  #starting a thread
  t1.start()
  t2.start()

  # join to check if thread finished running
  t1.join()
  t2.join()

  # Output
  # Cube of 5 is 125
  # Cube of 2 is 8
  ```
  - start function to start the thread and join function checks to see if the thread has completed execution yet and wait until execution is complete.
```python
  # importing the multiprocessing module 
  import multiprocessing 
  # calculate cube of a number
  def squaref(num):
    print(f'Square of {num} is {num*num}')
  # calculate cube of a number
  def cubef(num):
    print(f'Cube of {num} is {num*num*num}')

  # creating a thread
  p1 = multiprocessing.Process(target=squaref, args=(10,))
  p2 = multiprocessing.Process(target=cubef, args=(10,))

  # starting p1 and p2 processes
  p1.start()
  2.start()

  # join to check if process finished running or wait
  p1.join()
  p2.join()

  # Output
  # Square of 10 is 100
  # Cube of 10 is 1000
  ```

## 5. Fundamentals of Files
  ### Opening, Reading and Writing
</details>

<details>
<summary> Week 3 </summary>
<br>
  
# Python week 3 - Module focus
- Finding Inspiration for Python projects.
- Planning your Python Projects
- Create and implement User stories and Use cases
- Define and collate project requirements and program architecture
- Designing a project Graphical User Interface (GUI)
- Packaging and publishing Python projects
## 1. Project planning
  - project ideas
    - myTeams - sports updates and stats on my favourate teams and also teams will facing next
    - gamingHub - gives me updates on new games realeses, new packages upload and upcoming games
    - Music - updates me when my fav. artist drops new project
  ### User stories 
  - As a [role] , i want [goal] , so that [reason]
  - As a user, i want guess the number so that i can win.
  - As a user, i want to check score table so that i know what score to get.

  ### Use cases
  - title [goal?] , Actor [who desires it?] , scenario [how is it accomplished?]

  ### Project Requirments
  - functional requirements describe what the application should or should not do, and written a sentences starting with "the application must/shall"
  - non-functional requirements describe how the application should accomplish its tasks. e.g maintainability, reliability and usability.

  ### Architecture
  - 
## 2. Content Retrieval
## 3. Digest email
## 4. Nuilding a GUI
## 5. Design Iterarion
## 6. Project Packaging and Distribution


</details>
