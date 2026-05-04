#Write a program to display first 10 Fibonacci numbers?
#0 1 1 2 3 5 8 13 21 34 55
 
#addition of first number+ second number
fn=0
sn=1
print(fn, end=" ")
print(sn, end=" ")
 
for i in range(1,9):
    tn=fn+sn
    fn=sn
    sn=tn
    print(tn, end=" ")