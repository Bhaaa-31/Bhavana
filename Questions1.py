# 1 (Write a program to find the largest of three numbers)

a = int(input("Enter 1 Number: "))
b = int(input("Enter 2 Number: "))
c = int(input("Enter 3 Number: "))
if a > b and a > c:
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
        print(year,"is not leap year")  
else:
    if (year %4==0):
       print(year,"is leap year")
    else:
        print(year,"is not leap year")

# 3 (Write a program to check if a character is a vowel or consonant)

letter=input("enter a letter :")
letter=letter.lower()
if letter[0] in "aeiou":
   print(letter,"is a vowels")
else:
     print(letter,"is a consonants")

# 4 (Write a program to check whether a number is divisible by both 5 and 11)
numbers = int(input("Enter number: "))

if numbers % 5 == 0 and numbers % 11 == 0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")


 #5 (Write a program to calculate the sum of first N natural numbers using a while loop)
n=int(input("enter number :"))
i=1     
total =0
while i <=n:
     total=total+i
     i=i+1
print(total)

#6 (Write a program to print the multiplication table of a given number using a while loop)
multiplication=int(input("enter number :"))
i=1     
while i <=10:
     print(i,"×",multiplication,"=",multiplication*i)
     i=i+1

#7 (Print a pyramid pattern)
rows = 4
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

#8
for a in range(1, 6):
    for b in range(1, a + 1):
        print(b, end="")
    print()

