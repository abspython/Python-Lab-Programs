# Armstrong Number

#### Write a program to check whether a given number is Armstrong number or not.

#### What is Armstrong number??

A [Armstrong number or Narcissistic number](https://en.wikipedia.org/wiki/Narcissistic_number) is a number that us the sum of its digits each raised to the power of the number of the digits.

## Algorithm

1. Start
2. Input number in n. Declare sum = 0,copy =n
3. sum = sum + (n%10)^3
4. n = n/10
5. Repeat steps 3 to 4 until n > 0
6. If sum == copy   **else goto** step 8
7. print Armstrong number
8. print not a Armstrong number
9. Stop

## Code

**Easy**

------

```python
# Program to check whether a given number is an amstrong number or not [for order 3]
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

```

**Moderate**

------

```python
# Program to check whether a given number is an amstrong number or not [for order of n]
order = len(str(num))  # calculate the order of num

num = int(input("Enter th number"))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

```

**Hardcore**

------

```python
# Code inspired by Martin Ueding from Stackoverflow
# https://stackoverflow.com/users/653152/martin-ueding


def is_armstrong(number):
    digits = [int(letter) for letter in str(number)]
    score = sum(digit**len(digits) for digit in digits)
    return score == number

n = int(input("Enter the number.."))

if is_armstrong(n):
    print("It is Amstrong number!")
else:
    print("It is not Amstrong number!")

```

