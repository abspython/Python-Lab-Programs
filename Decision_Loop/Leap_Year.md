# Leap Year

Write a program to check whether a given year is a leap year or not.



## Algorithm

1. Start
2. Read the value of year in variable 'y'
3. If y%400 is 0   **else goto** step 5
4. print leap year
5. If y%4 is 0 and y%100 not 0   **else goto** step 7
6. print leap year
7. print not a leap year
8. Stop

## Code

**Easy**

------



```python
# Program to check whether a given year is leap year or not

y = int(input("Enter the year to be checked..."))

if y % 100 == 0:
    print("It is a leap year!")
elif y % 4 == 0 and y % 100 != 0:
    print("It is a leap year!")
else:
    print("It is not a leap year!")

```

**Moderate**

------

```python
# Program to check whether a given year is leap year or not

y = int(input("Enter the year to be checked..."))

if y % 100 == 0 or (y % 4 == 0 and y % 100 != 0):
    print("It is a leap year!")
else:
    print("It is not a leap year!")

```

**Hardcore**

------

```python
# Program to check whether a given year is leap year or not


```

