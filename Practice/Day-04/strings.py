# strings [There are two ways declare a string.]
# single line string variable assign
string_one = 'bangladesh'
string_two = "islam"
# output
print(string_one)
print(string_two)
print('--------------------')

# multi-line string variable assign
string_three = """
Hello World,
I'm Abdullah.
Nice to see you.
"""
print(string_three)
print('--------------------')

# string is a chacter array.
name = 'Abdullah'
print(name[0]) # it will print first character of the string.
print('--------------------')

# looping through a string
country_name = 'Bangladesh'
for i in country_name:
    print(i) # it will print all the character of the string.
print('--------------------')

# string length check
mothers_name = 'shilpi'
print(len(mothers_name))
print('--------------------')

# find any word in the string
sentence = "I live in kishoregonj."
print('live' in sentence) # it will print true. because 'live' is present in the sentence.
print('you' in sentence) # it will print false. because 'you' isn't present in the sentence.
print('--------------------')

# string check
another_sentence = "I love my country."
if 'love' in another_sentence:
    print("love is present in the sentence.")
else:
    print("love isn't present in the sentence.")

if "you" in another_sentence:
    print("you is present is the sentence.")
else:
    print("you isn't present in the sentence.")
    
print('--------------------')
