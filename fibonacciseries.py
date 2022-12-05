#fibonacci series
n=int(input("enter number ="))
a=0
b=1
sum=0
c=1

while(c<=n):
    print(sum)

    a=b
    b=sum
    c+=1
    sum=a+b
