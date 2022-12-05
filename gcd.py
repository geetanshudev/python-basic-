#gcd
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

a=int(input("enter number a="))
b=int(input("enter number b ="))
c=gcd(a,b)
print("gcd of two number are = ",c)
