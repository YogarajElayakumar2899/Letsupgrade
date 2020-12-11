#!/usr/bin/env python
# coding: utf-8

# Assignment 1 (use if else and elif to write a program is python for your report cards)

# In[1]:


print("Enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    	print("Your Grade is A+");
    elif(average>=81 and average<=90):
    	print("Your Grade is A");
    elif(average>=71 and average<=80):
    	print("Your Grade is B+");
    elif(average>=61 and average<=70):
    	print("Your Grade is B");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    elif(average>=41 and average<=50):
    	print("Your Grade is C");
    elif(average>=0 and average<=40):
    	print("Your Grade is F");
    else:
    	print("Strange Grade..!!");


# Assignment 2(use for loop for to print prime numbers between 1 to 1000 in python)

# In[15]:



for Number in range (1, 1001):
   count = 0
   for i in range(2, (Number//2 + 1)):
       if(Number % i == 0):
           count = count + 1
           break

   if (count == 0 and Number != 1):
       print(" %d" %Number, end = '  ')


# Assignment 3 (write a program for printing the table from 1,10 using nested for loop in python)

# In[55]:


print("\t\t\t\t Multiplication tables\n")

for i in range(1,11):
    print(i,end="\t")
print()
print("____________________________________________________________________________\n")
for j in range(1,11):
    for k in range (1,11):
        print(j*k,end="\t")
    print("\n")


# Assignment 3 (write a program to print x prime numbers using while loop and take the input of x from the user)

# In[58]:



Number = int(input(" Please Enter any Number: "))
count = 0

for i in range(2, (Number//2 + 1)):
    if(Number % i == 0):
        count = count + 1
        break

if (count == 0 and Number != 1):
    print(" %d is a Prime Number" %Number)
else:
    print(" %d is not a Prime Number" %Number)

