# Prime number in a given range

Program to print all the prime number in a given range

## Algorithm

I'm too lazy to write it now and will update it later...

## Code

**Easy**

------

```python
# Program to print all prime number within a given range

l = 100
for num in range(1,l+1):
	if num>1:
		for i in range(2,num//2+1):
				if num%i == 0:
					break
		else:
			print(num)

```

**Moderate**

------

```python
# Program to print all prime number within a given range

def is_prime(n):
	if n<1:
		return False
	else:
		for x in range(2,n//2+1):
			if n%x == 0:
				return False
	return True

l = 100
for i in  range(2,l+1):
	if is_prime(i):
		print(i,end=" ")

```

**Hardcore**

------

```python
# Program to print all prime number within a given range

import math
def is_prime_v3(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n>2 and n%2 == 0:
		return False
	for x in range(3,int(math.sqrt(n))+1):
		if n%x == 0:
			return False
	return True

for n in range(1,100):
	if is_prime_v3(n):
		print(n)
```

**Pythonic Way**

------

```python
import math
#Efficiency level - 1
for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
       print num
    
#Efficiency level - 2
'''
No need to check upto n but to sqrt(n) or n//2.
'''
for num in range(2, 101):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        print(num)
        
#Efficiency level - 3
'''
Odd numbers are not prime.Tweak the code according to it.
'''
print 2
for num in range(3,101,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        print num
```

