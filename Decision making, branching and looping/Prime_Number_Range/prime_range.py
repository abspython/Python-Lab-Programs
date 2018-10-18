# Program to print all the prime numbers in a given range

l = int(input("Enter the uppper limit.."))
for num in range(1,l+1):
	if num>1:
		for i in range(2,num//2+1):
				if num%i == 0:
					break
		else:
			print(num)
