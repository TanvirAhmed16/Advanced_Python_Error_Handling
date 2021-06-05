'''
# Error Handling - We have explored basic python till now from Set 1 to 4 (Set 1 | Set 2 | Set 3 | Set 4).
  Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a program
  due to which the program will stop the execution. On the other hand, exceptions are raised when some internal
  events occur which changes the normal flow of the program.

--> The difference between Syntax Error and Exceptions
# Syntax Error: As the name suggest this error is caused by wrong syntax in the code. It leads to the termination
  of the program.
# Exceptions: Exceptions are raised when the program is syntactically correct but the code resulted in an error.
  This error does not stop the execution of the program, however, it changes the normal flow of the program.
'''

'''
Let's assume some scenario where we want to take input of an age from an user. Let's see some errors/exceptions. 
'''

while 1:
    try:
        age = int(input('What is your age? '))
        100 / age
        print(f'You are {age} years old.')
    except:
        print('Please enter a number')
    else:
        break
'''
In the above example everything looks fine except we input age as 0. Though 0 is a number, but still it will show 
that please enter a number which is not appropriate. So to handle this type of exception we need to do define the 
specific errors.
'''

while 1:
    try:
        age1 = int(input('Enter your age please - '))
        100 / age1
        print(f'You are {age1} years old.')
    except ValueError:
        print('Please enter a number.')
    except ZeroDivisionError:
        print('Please enter a number higher than 0.')
    else:
        print('Thank you...')
        break
