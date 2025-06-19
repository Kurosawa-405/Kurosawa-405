# sum of n natural numbers
import time 
n=int(input("enter the number"))
sum=0
start_time=time.time('%H:%M:%S')
for i in range(1,n+1):
    sum=sum+i
print(sum)    
end_time=time.time('%H:%M:%S')
execution_time=end_time-start_time
print(f"the execution time is {execution_time}")

    