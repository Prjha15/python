a=float(input("ENTER THE NUMBER"))
b=float(input("ENTER THE NUMBER"))
operator=(input("ENTER THE OPERATOR: +,-,*,/"))
if(operator=='+'):
    print("RESULT is ",a+b)
elif(operator=='-'):
    print("RESULT is ",a-b)
elif(operator=='*'):
    print("RESULT is ",a*b) 
elif(operator=='/'):
    print("RESULT is ",a/b)    
else:
    print("INVALID SELECTION")
