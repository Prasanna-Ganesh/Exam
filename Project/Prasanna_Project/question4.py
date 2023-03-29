def hexa(num):
    k=num-1
    for i in range(0,num):
        for j in range(0,k):
            print(end="")
            k=k-1
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
ch=int(input("Enter the num of stars to print: "))
hexa(ch)

#it is printing right angle triangle