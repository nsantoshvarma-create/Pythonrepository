#Case 2: Write a program to find count of numbers in between 1 to 100 which are divisible by 9
#Example :
count=0
i=1
while(i<=100):
    if(i % 9 ==0):
        count=count+1
    i=i+1
print("Count of Numbers :",count)