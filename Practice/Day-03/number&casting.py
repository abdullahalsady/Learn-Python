# There are three numeric types in Python. [integer, floating-point, complex]
# integer number
integer_num = 10
print(integer_num)
print(type(integer_num))
print('--------------------')

# floating-point number
floating_point_num = 10.4
print(floating_point_num)
print(type(floating_point_num))
print('--------------------')

# complex number
complex_num = 10j
print(complex_num)
print(type(complex_num))
print('--------------------')
 
'''
Python type() is a built-in function that is used to return the type of data stored in the objects or variables in the program.
'''


# Type casting
x = 10
y = 20.5
z = 30j

# Convert integet to float
a = float(x)
print(a)
print(type(a))
print('--------------------')


# Convert float to integer
b = int(y)
print(b)
print(type(b))
print('--------------------')

# Convert float to complex
c = complex(z)
print(c)
print(type(c))
print('--------------------')

# Convert to complex to integer
'''
d = int(z)
print(d)
print(type(d)) #** It through an error. Becauese its not possible to convert complex to integer. 
print('--------------------')
'''

# Convert number to string
e = str(a)
print(e)
print(type(e))
print('--------------------')

