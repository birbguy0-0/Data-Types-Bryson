# # x = 3.14159265
# # y = float(3)
# # print(x,y)
# values = [1,2.23,5,7,2,30,15]
# # print(values)
# # for i in values:
# #     print(i)
# print(values[0])
# print(values[6])

# x = "this is a thing"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)


#Question: Using the "input" method in Python, ask a user to input a sentence. Then develop a function that accepts a the user input and will tell you how many words are in that string. First write out your plan in Pseudo-code using comments. Then craft the function.

# count = 0
# #Asks the question
# sentence = input("Type a Sentence: ")
# print(sentence)
# #Breaks it up
# word = sentence.split()
# print(word)
# #Counts the words
# for i in word:
#     count += 1
# print(count)

#Mad Lib Project

# noun = input("Type a noun: ")
# verb = input("Type a verb with a ing in the end: ")
# adjective = input("Type an adjective: ")
# noun2 = input("Type another noun: ")
# sentence = f"Once opon a time, a {noun} came {verb} down a hill holding a {adjective} {noun2}."
# print(sentence)


# day_of_week = input("What day is it? ")
# day_of_week = day_of_week.upper()
# if day_of_week == "TUESDAY":
#     print("correct")
# else:
#     print("incorrect")


# x = "test"
# print(f"hello {x}")



# temp = 68
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')


#Even or Odd

# number = int(input("Type a number: "))
# if (number % 2 == 0):
#     print("Even")
# else:
#     print("Odd")

#Tipping System

# bill = float(input("How much is the bill: "))
# service = input("How was the service? (Bad, Okay, Good, or Great): ")
# service = service.upper()
# if (service == "BAD"):
#     zero = f"You tip 0% ... Your bill is {bill} dollars."
#     print(zero)
# if (service == "OKAY"):
#     fifteen_bill = float(bill * 1.15) 
#     fifteen = f"You tip 15% ... Your bill is {fifteen_bill} dollars."
#     print(fifteen)
# if (service == "GOOD"):
#     twenty_bill = float(bill * 1.20) 
#     twenty = f"You tip 20% ... Your bill is {twenty_bill} dollars."
#     print(twenty)
# if (service == "GREAT"):
#     twofive_bill = float(bill * 1.25) 
#     twofive = f"You tip 25% ... Your bill is {twofive_bill} dollars."
#     print(twofive)
# else:
#     print("You either didn't type right or you trolling :/")

#Number Factor

# number = int(input("Type a number: "))
# if number <= 0:
#     print("Please enter a positive integer.")
# else:
#     for n in range(1, number + 1):
#         if number % n == 0:
#             print(n)

#Greatest Common Factor

number = int(input("Type a number: "))
number2 = int(input("Type another number: "))
if number < number2:
    for n in range(1, number2 + 1):
          if number % n  == 0 and number2 % n == 0:
                store = n

elif number2 < number:
     for n in range(1, number + 1):
            if number % n  == 0 and number2 % n == 0:
                store = n
print(store)