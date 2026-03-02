#   A=P(1+R/100)^t
#   CI=A-P
P=int(input("ENTER THE PRINCIPAL:"))
R=int(input("ENTER THE RATE:"))
t=int(input("ENTER THE YEARS:"))
A=P*(1+R/100)**t
CI=A-P
print("COMPOUND INTEREST IS:",CI)