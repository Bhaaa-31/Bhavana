# 1 (Write a program to find the largest of three numbers)

a = int(input("Enter 1 Number: "))
b = int(input("Enter 2 Number: "))
c = int(input("Enter 3 Number: "))

if a == b and b == c:
    print("All three numbers are equal")

elif a == b:
    if a > c:
        print("First and second numbers are equal and greater")
    else:
        print("Third number is greater")

elif b == c:
    if b > a:
        print("Second and third numbers are equal and greater")
    else:
        print("First number is greater")

elif a == c:
    if a > b:
        print("First and third numbers are equal and greater")
    else:
        print("Second number is greater")

elif a > b and a > c:
    print("First number is greater")

elif b > a and b > c:
    print("Second number is greater")

else:
    print("Third number is greater")


# 2 (Write a program to check whether a given year is a leap year)

year = int(input("Enter year : "))
if (year %100 ==0 ):
    if(year %400== 0):
        print(year,"is leap year")
    else:
        print(year,"is not not leap year")  
else:
    if (year %4==0):
       print(year,"is leap year")
    else:
        print(year,"is not not leap year")

# 3 (Write a program to check if a character is a vowel or consonant)

word=input("enter a letter :")
word.lower()
if word[0] in "a e i o u":
   print(word,"is vowels")
else:
     print(word,"is consonants")

# 4 (Write a program to check whether a number is divisible by both 5 and 11)

numbers = int(input("Enter number "))
if(numbers%5==0 and numbers%11==0):
    print("the number is divisible by 5 and 11")
elif(numbers%5==0):
   print("the number is divisible by 5")
elif(numbers%11==0):
     print("the number is divisible by 11")
else:
    print("try another number")

# 5 (Write a program to calculate the sum of first N natural numbers using a while loop)

multiplication=int(input("enter number :"))
i=1     
while i <=10:
     print(i,"×",multiplication,"=",multiplication*i)
     i=i+1

#6 (Print a pyramid pattern)
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

#7 
for a in range(0,6):
    for b in range(1, a + 1):
        print(b, end="")
    print()
