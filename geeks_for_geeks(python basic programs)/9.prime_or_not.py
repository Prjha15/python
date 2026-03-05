n=int(input("ENTER THE NUMBER"))
prime=0
for i in range(1,n+1):
    if n%i==0:
        prime=prime+1
if prime==2:
    print("Number is prime:",n)
else:
    print("Number is not prime")            
        