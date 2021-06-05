'''
# Here we will expand our learning on error handling more. We will use a new term called finally.
# Let's re write our previous example.
'''

while True:
    try:
        age = int(input('What is your age? '))
        10 / age
    except ValueError as err:
        print('Enter a proper value for age.')
        print(err)
        continue
    except ZeroDivisionError as err:
        print('Enter an age higher than 0.')
        print(err)
        break
    else:
        print(f'You are {age} years old. Thank you.')
        break
    finally:
        print('Ok, I am finally done.')
    print('Can anyone here me????')

'''
# finally keyword in Python - In programming, there may be some situation in which the current method ends up 
  while handling some exceptions. But the method may require some additional steps before its termination, 
  like closing a file or a network and so on.
# So, in order to handle these situations, Python provides a keyword finally, which is always executed after 
  try and except blocks. The finally block always executes after normal termination of try block or after try 
  block terminates due to some exception.

# Syntax:
    try:
       # Some Code.... 
    except:
       # optional block
       # Handling of exception (if required)
    finally:
      # Some code .....(always executed)

# Important Points –
--> finally block is always executed after leaving the try statement. In case if some exception was not handled 
    by except block, it is re-raised after execution of finally block.
--> finally block is used to deallocate the system resources.
--> One can use finally just after try without using except block, but no exception is handled in that case.

# If any Value error occurs then it's continue statement will send us back to the start of the loop.
# And at the end the final print statement will only run if we input a proper input and we don't use any break
  statement in the else block. 
'''