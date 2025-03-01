a=float(input("ENTER THE FIRST NUMBER"))
match a:
    case _ if a>0:
        print("NUMBER IS POSITIVE")
    case _ if a<0 :
        print("NUMBER IS NEGATIVE")
    case _ :
        print("NUMBER IS 0")
  