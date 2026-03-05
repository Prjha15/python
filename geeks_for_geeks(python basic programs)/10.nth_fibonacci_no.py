n=int(input("ENTER THE NUMBER:"))
first_no=0
second_no=1
for i in range(1,n+1):
    p=first_no
    x=first_no+second_no
    first_no=second_no
    second_no=x
print( " ",p)