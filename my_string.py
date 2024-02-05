my_str = " Hello, World! "

my_longer_str = '''
this is my multiline string
i want to show how the len() function work for the long string one 
'''

my_multiline_str = '''
this is my new line
this is another new line
this is also another new line
'''

print(my_str[1])
# this is a for loop this will
#loop through each character in a string
#and printing it out
for u in my_str:
    print(u)
# the len function will show the number of character in a string
print(len(my_str))

# checking if the word "or" is inside the phrase "Hello, World!"

print ("or" in my_str)

print(my_str.upper())
print(my_str.lower())

#remove the spaces in front and behind my string
print (my_str.strip())

#replace the original word with the new one
print (my_str.replace("Hello" , "Bye"))

#split my string
print (my_str.split("o"))

str_one = "Hello"
str_two = "World"

#add two string tgt
print (str_one + " " + str_two)

#format string
print (f"Hello, {str_two}")

# \ is to escape character
print ('my name is name I\'m here')