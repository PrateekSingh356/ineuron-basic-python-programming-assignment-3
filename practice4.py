#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
primelist=[]
for num in range(1, 1000 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           primelist.append(num)
print(primelist)