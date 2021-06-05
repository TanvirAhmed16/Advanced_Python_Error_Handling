'''
# Let's expand our understanding of error handling.
# Here we will find that we can not only handle any type of error but we also can show that error in a specified
  way.
--> Let's see our below example...
'''

def sum(num1, num2):
    try:
        return num1 + num2
    # except:
    #     print('Something is wrong.')
    except TypeError as err:
        print('Please input two numbers.')
        # We can also identify or show the error more specifically.
        print(err)


print(sum('1', '5')) #It will concatenate this two strings. Let's see what will happen for two different input type.
print(sum(5, '5'), '\n')

'''
# We can also wrap errors together like...  
'''

def div(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print('Oh no, we have an error.')
        print(err)

print(div(5, '5'))
print(div(5, 0))