-Programming: Creating a set of instructions that tell a computer, how to perform a task.
-computer only understand 0,1 that is knows as machine code
-but human understand Source Code that is java,c++,Python. These are easy to understand for human.
-Python 
    SourceCode--compiler-->Bytecode--interpreter-->MachineCode
-easy to read,understand-beginner-friendly-conscise code-open Source-versatile:Web Development,ML,AL,Data Analytics
-to print in python Syntex: print("String") or print(variable_name)
-indentation is very neccessary.
-type(variable_name):to find datatype of variable
-input():to take input
-Formated String :print(f"") use f and write variable inside {}
-print(end=" "):use to print text in same line
-chr(integerValueORIntegerVariable): ASCII to char : print(chr(j)) here j is int variable or print(chr(97))
-ord(charValueORCharVariable): char to ASCII : print(ord(c)) here c is a char variables or print(ord('a'))
print("hello\n"*5) : To print hello 5 times without looping
Python collection: use to store collection of items
    1. Lists []:multiple items in a single variable : list=["mango","banana","orange"]
            indexed :if size of list is n
                indexing 0 to n-1
                negativeIndexing  -1 to -n
                rangeIndexing is possible as tuple[startIndex:endingIndex] (negativeIndexing also possible)
            ordered: place of every element is fixed so indexing is possibe
                append(value): add value at end
                insert(index,value): add value to given index
                extend(): list1.extend(list2):list2 to added in list1
                pop():pop(2):remove last element or if your given index
                remove(value): value will me removed
                sort():list.sort():list.sort(reverse=True)
                reverse():list.reverse()
            mutable:we can manipulate values of list 
            duplicates allowed
            any datatype
            mixed of different datatypes
            List Comprehension :When we want to make a new list from existing list.
            Nested List:
    2. Tuples (): Used to store multiple items in a variable.
        Ordered:place of every element is fixed so indexing is possibe
            indexed :if size of list is n
                indexing 0 to n-1
                negativeIndexing  -1 to -n
                rangeIndexing is possible as tuple[startIndex:endingIndex] (negativeIndexing also possible)
        Immutable:values cannot update or change
        Duplicates allow
        any datatypes
        Mix of diffrent Datatypes

    3. Set {}:Used to store multiple items in a variable.
        unordered: order not fixed every time you print set, elements can change their place
        set_name.update(list) :add list to set
        set_name.add(value)
        set_name.remove(value):if value not exist give eror
        set_name.discord(value) :if value not exist also run
        set1.union(set2)
        set1.intersection(set2)
        set1.intersection_update(set2)
        set1.symmetric_difference(set2)

        Unindexed: becoz of unorderd
        Immutable: cannot update values but can add and remove 
        duplicates not allowed
        any datatypes
        mix of different datatypes is allowed
    4. Dictionary:store Key pairs
        creating Dictionary: {
                                "name":"bhupendra",
                                "class":"MCA"
                             }
         Ordered :in fixed orderd
         changeable :can be changed
         Unindexed :
         duplicated not allowed : keys can not duplicate, but value can
         Any Datatyps:
Function:
    -   def function_name(parameters):
            statement
    -Types of arguments
        1-Default argument:
            def showValue(value="default_value"):
                print(value)
            showValue() :if we not pass any argument it print default_value
            showValue(54) 
        2-keyword argument(named arguments):
            def add(n1,n2):
                print("n1:",n1)
                print("n2:",n2)
                sum=n1+n2
                return sum
            n1=45
            n2=76
            keyword argument
            print(add(n2=45,n1=67))
        3-positional arguments:
            positional argument 
            print(add(n2,n1))
        4-arbitary arguments(variable-length arguments *args and **kwargs) :arguments treate as a *args:tuples / **kwargs:dictionary
    inner_function
    outer_function

    Pass by value: for immutable objects -string,integers,float,tuple
        pass copy of actual object to the function and changes value assigned in local variable in function. actual object value outside the function does not effect.
    Pass by reference: for mutable objects - list, dictionary : reference of the actual object is passed to the function .
        changed inside function effects the actual(original) objects.
========================================================================================
Data Types:
    Number
        Integers
        Float 
        Complex 654j,45j,etc
    Boolean
        True
        False
    String
        ""
        ''

Control Flow
    if
    if-else
    elif
    nested if-else
    break
    continue

Loops
    For i in range()/set/tuple/list:   "range() used three parametrs(startPoint,StopPoint,StepIncrement/decrement)"
        print()
    
    while condition:
        print()
        increent/decrement