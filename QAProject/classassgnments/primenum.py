#Write a program to verify that given number is prime or not?
#Answer:  if any number divisible by 1 and itself alone.
 
#We can exclude 1 and same given number
#Example:
#13
#Exclude 1 and 13
#2,3,4,5,6,7,8,9,10,11,12
 
num=int(input("Enter The number to Verify whether It is Prime: \n"))
 
flag=0
for i in range(2,num):
    if(num % i ==0):
        flag=flag+1
        break
if(flag==0):
    print(num," is a Prime Number")
else:
    print(num," is not a Prime Number")
 