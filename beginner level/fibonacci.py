a=int(input("enter the number: "))
b=0
c=1
i=1
while(i<=a):
    if(i<=1):
        d=i
    else:
        d=b+c
        b=c
        c=d
    print(d)
    i=i+1
