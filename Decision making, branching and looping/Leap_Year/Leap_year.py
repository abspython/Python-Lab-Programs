# Program to check whether a given year is leap year or not

y = int(input("Enter the year to be checked..."))

if y % 100 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("It is a leap year!")
else:
    print("It is not a leap year!")
