# 1(Write a function that takes the radius of a circle and returns its area)
def Area(radius):   
   return 3.15*radius*radius
radius=float(input("Enter radius :"))
print("area of the circle",Area(radius))

# 2(Write a function that accepts three numbers and returns the largest one)
def largest(a,b,c):
    if a>b and a>c:
       return a
    elif b>a and b>c:
        return b
    else:
        return c
        
a= int(input("Enter number :"))   
b= int(input("Enter number :"))   
c= int(input("Enter number :"))   

print("the larger number is",largest(a,b,c))

# 3(Write a function that takes a string and returns its length without using built-in length functions)
def length(text):
    count = 0
    for character in text:
        count = count + 1
    return count
text = input("Enter a string: ")
print("Length of the string:", length(text))

# 4(Write a function that checks whether a number is prime)

def prime(number):
    i=2
    while i<number:
        if number %i==0:
            return("not a prime number")
            i=i+1
        return("prime number")
            
number= int(input("Enter number :"))     
print(prime(number))       
