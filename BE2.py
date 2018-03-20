"""
Write a program that will ask the user for three integer numbers and then multiply the first two together before dividing the result by the third number. 
The input and output should be user friendly.
"""

num1 = int(input("Please enter number 1: "))
num2 = int(input("Please enter number 2: "))
num3 = int(input("Please enter number 3: "))
#num4 = int(input("Please enter number 4: "))

result = int((num1 + num2) / num3)
print("result of {0} + {1} / {2} is {3}".format(num1, num2, num3, result))
#print("Sum of {1} + {2} + {3} + {4} is {5}".format(num1, num2, num3, num4, sum))