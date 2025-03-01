a=float(input("ENTER THE FIRST NUMBER"))
b=float(input("ENTER THE SECOND NUMBER"))
x=input("ENTER THE OPERATION YOU WANT TO EXECUTE")
match x:
    case "+":
        print("THE SUM OF a and b IS ",a+b)
    case "-":
        print("THE SUBTRACTION  OF a and b IS ",a-b)
    case "/":
       print("THE DIVISION OF a and b IS ",a/b)
    case "*":
        print("THE MULTIPLICATION OF a and b IS",a*b)
