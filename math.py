'''def tripletsfind(n):
    triplets=[]
    for c in range(1,n):
        for b in range(1,c):
            for a in range(1,b):
                if a**2+b**2==c**2:
                    triplets.append((a,b,c))
    return triplets
    


n=int(input("Enter a  number:"))
triplets=tripletsfind(n)
print(f"Pythogorean triplets upto{n}")
for t in triplets:
      print(t)
'''





#C(n,k) without using built in function
'''n=int(input("enter the value of n "))
k=int(input("enter the value of k "))
b=n-k

def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
        

ans=fact(n)/(fact(k)*fact(b))
print(ans)
'''

'''import math
a=int(input("enter the value of a "))
b=int(input("enter the value of b "))
c=int(input("enter the value of c"))

def quadratic_function(a,b,c):
    if a==0:
        print("Invalid entry")
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        discriminant1 = abs(discriminant)
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(discriminant1) / (2 * a)
        x = f"{real_part} + {imaginary_part}i"
        y = f"{real_part} - {imaginary_part}i"
        return x, y
        

    else:
        x=(-b+math.sqrt(discriminant))/(2*a)
        y=(-b-math.sqrt(discriminant))/(2*a)
        return x,y
    
print(f"the roots of the equation is {quadratic_function(a,b,c)}")

'''
e=0.001
def func(x):
    return x**3-x-11


while func(x1)*func(x2)>0:
    x1=int(input("enter the value of x1:"))
    x2=int(input("enter the value of x2:"))

while(abs(x2-x1)>e):
    x0=(x1+x2)/2
    if(func(x1)*func(x0)<0):
        x2=x0
    else:
        x1=x0

print(f"Root={x0}")


