#calculate the area of the circle using recursive function
'''import math
def area(radius):
    return math.pi*radius**2

r=float(input("enter the radius of the circle:"))
print(f'the area of the circle is : {area(r):.2f}')
'''

#calculate the CI and also to calculate the SI and find the differences between them and print it
'''a=float(input("enter the amount:"))
t=int(input("enter the time:"))
r=float(input("enter the rate:"))
CI=(a*((1+10/100)**t-1))
SI=(a*t*10)/100
print(CI)
print(SI)
print(CI-SI) '''


'''import math
r=float(input("enter the radius :"))
h2=float(input("enter the height for cylinder:"))
h1=(r**2-3**2)**0.5
volume=2/3*math.pi*r**2*h1+math.pi*r**2*h2
print(volume)

def volume1(r,h1,h2):
    v=2/3*math.pi*r**2*h1+math.pi*r**2*h2
    return v
print(f'Volume:{volume1(r,h1,h2)}') '''


'''#fibonacii series
def fibo(n):
    fib_series=[]
    a,b=0,1
    for _ in range(n):
        fib_series.append(a)
        a,b=b,a+b
    return fib_series
n=int(input("enter the nth term"))
if n<0:
    print("the number should be positive")
else:
    print(f'the fibonacci series:{fibo(n)}') '''

'''#reverse string
s='Prasanna'
print(s[::-1]) '''


#implement stack using python
#implement circular, doubly,singly linked list

#reverse
'''def reverse(n):
    s=0
    while n>0:
        digit=n%10
        s=s*10+digit
        n=n//10
    return s

n=int(input("Enter the number to be reversed:"))
print(f'the reversed number:{reverse(n)}')
print(int(str(abs(n))[-1])) '''

#factorial
'''def fact(n):
    s=1
    while n>0:
        s=s*n
        n=n-1
    return s


n=int(input("Enter the number:"))
print(f'answer:{fact(n)}') '''
    


'''def fact(n):
    temp=1
    while n>0:
        facto=n*temp
        n=n-1
    return facto

n=int(input('Enter a number:'))
print(f"the factorial of the number:{fact(n)}") '''

def swapx(x):
    t = x[0]
    x[0] = x[1]
    x[1] = t
    print(f"Inside swapx: x = {x[0]} y = {x[1]}")

# Main function
def main():
    values = [10, 20]  # Using a list to simulate reference behavior
    swapx(values)
    print(f"Inside main: a = {values[0]} b = {values[1]}")

main()



