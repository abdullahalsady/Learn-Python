# booleans represent one of two values: True of False.
# is 10 is bigger than 9.
print(10 > 9)
print('--------------------')

# is 10 is equal 9.
print(10 == 9)
print('--------------------')

# is 10 is less than nine.
print(10 < 9)
print('--------------------')

# conditions
first_number = 10
second_number = 20
if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
else:
    print(f"{second_number} is greater than {first_number}")
print('--------------------')

# bool method
print(bool("Bangladesh"))
print('--------------------')

# return false
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(""))