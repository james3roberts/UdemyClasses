##This class claims to take me from zero to hero.
# I skipped the 1st section to get to the actual programming
# s2-c1 Data types Print statements. Vapriables 1,2,3, naming, values, comments input str(), operators, real worls 1-6
# print('This is how you print a string')
# #this is how you set a variable
# x = 1
# #this is how you print a variable
# print(x)
# #this is wrong
# print('x')
# #this is how you combine them dont know it its part of the learning proccess
# print ('string',x)
# #also can  do this
# print('string'+'also')#have to watch spaces here. 
#Ctrl+k+c comments out a block of code
#Ctrl+k+u uncomments out a block of code
#Naming variables
# car_speed = 100
# room_temp = 30
# age = 34
# print('My Age is', age, 'years old.')# commas add spaces in strings automatically
# score = 89
# score = 90
# print(score)
#if you use the same variable name it will only use the last one written
# now we are going to learn how to comment! The more I do the more I am learning why this is so important
#We are now are s2ch14
#now we are going to learn about inputs
# x=input('please enter x value ')
# print(x)
# age = input('What is your age? ')
# print('I am',age,'years old')
#I have learnd this a few time and just waiting to see if i have missed something. 
#you can add int or float to an input to make sure that the input is what you want however you will have to write error codes
# #how to make a string
# x = 4.4
# str(x)
# print(x)
# y= x+3
# print(y)
# x=x+3
# print(x)
# #Dont know why we are learning how to change variable in a section about strings. 
#now time to learn about operators in python 
#section2 chapter 17
 #a new thing is double division signs does not give a float but a whole number.
# e=5//2
# print(e)
##Tie to start real world examples.
##The goal is to give a price of an item with a 50% discount.
# discount_rate= 50/100
# original = int(input("what is the original prince of the item"))
# sales_price=original*discount_rate
# print("The price after 50 % discounnt is $",sales_price)
# ##Well this worked to give a discount. 
#real world problem to figure out grades. 
#add the formatting option to only have 2 decimal places.Line 63 works great
# numberOfExams = 3
# exam1 = int(input('First test score: '))
# exam2 = int(input('Second test score: '))
# exam3 = int(input('Third test score: '))
# ave =(exam1 + exam2+ exam3 )/numberOfExams
# print('the average test score is',format (ave,'.2f'))
# real world problem to find percent that pass a class and percent that failed
# passed = int(input('Number of students that passed: '))
# failed = int(input('Number of students that failed: '))
# total = passed + failed
# passPerc = passed/total
# failPer = failed/total
# print(format(passPerc,'.0%'), 'OF students that passes')
# print(format(failPer,'.0%'),'of students that failed')
# #this works but leaves a decimal place
# #the format fixxes the decimal. add .0 before % sign to have no decimal
#Time to start if statements
