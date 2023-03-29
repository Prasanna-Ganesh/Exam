def Celsius_Fahrenheit(c):
    f=(1.8*c)+32
    return f


exit = False
while not exit:
    print("Enter c to convert Temperature from Celsius to Fahrenheit: ")
    find=input()
    if find == 'c':
        a = int(input("Enter the Temp in Celsius to find  Fahrenheit: "))
        result = Celsius_Fahrenheit(a)
        print(result)
    else:
        print("Sorry Wrong Input!!!")
