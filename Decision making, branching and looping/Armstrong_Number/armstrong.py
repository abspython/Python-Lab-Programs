# Program to check whether a given number is an amstrong number or not
n = int(input("Enter the number to be checked..."))
sm = 0
copy = n

while n > 0:  # for find sum of cubes of digits of n
    sm = sm + (n % 10)**3
    n = n // 10  # Integer division

if sm == copy:
    print("The given number is amstrong number!")
else:
    print("The given number is not amstrong number!")
