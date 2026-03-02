import math
n=int(input("ENTER THE NUMBER"))
p=n
sum = 0
while p>=1:
    digit=p%10
    sum=sum+digit**3
    p=p//10
if sum==n:
        print("NUMBER IS ARMSTRONG")
else:
        print("NUMBER IS NOT ARMSTRONG")