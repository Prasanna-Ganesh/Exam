n= int(input("Enter the num to find the fact: "))
fact=1
if n<0:
    print("Please enter positive number")
elif n ==0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f"The factorial of {n} is {fact}")
