def findGrade(test1,test2,test3):
    avg=(test1+test2+test3)/3
    if avg>=90:
        print(f"Average Score = {avg}")
        print("Letter Grade = A")
    if avg >= 80 and avg<90:
        print(f"Average Score = {avg}")
        print("Letter Grade = B")
    if avg >= 70 and avg<80:
        print(f"Average Score = {avg}")
        print("Letter Grade = C")
    if avg >= 60 and avg<70:
        print(f"Average Score = {avg}")
        print("Letter Grade = D")
    if avg < 60:
        print(f"Average Score = {avg}")
        print("Letter Grade = E")

test1=int(input("Enter score for test 1: "))
test2=int(input("Enter score for test 2: "))
test3=int(input("Enter score for test 3: "))
#All the inputs of each subject has been given inti "findGrade() function"
findGrade(test1,test2,test3)

