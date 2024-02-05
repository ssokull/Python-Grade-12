#file name quiz_app.py
total_point = 0
# name = input ("what is your name? ")
# print ("Hello", name)

#file name
question = input ("2 + 2? ")

if question == "22": 
    total_point = total_point + 1
    print ('Correct')
else:
    print ('Incorrect')

question_two = input ("1 + 1? ")

if question_two == "11": 
    total_point = total_point + 1
    print ('Correct')
else:
    print ('Incorrect')

question_three = input ("4 + 4? ")

if question_three == "44": 
    total_point = total_point + 1
    print ('Correct')
else:
    print ('Incorrect')

question_four = input ("5 + 5? ")

if question_four == "55": 
    total_point = total_point + 1
    print ('Correct')
else:
    print ('Incorrect')

question_five = input ("5 + 7? ")

if question_five == "57": 
    total_point = total_point + 1
    print ('Correct')
else:
    print ('Incorrect')

print ( f" Your total point is: {int (total_point/5*100)}%")