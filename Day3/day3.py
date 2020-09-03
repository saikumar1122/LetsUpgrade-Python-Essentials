#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Day 3 Assignment Question1


# In[3]:


height=int(input("Enter the altitude: "))

if(height<=1000 and height>0):
    print("Safe to land")
elif(height>1000 and height<5000):
    print("Bring down to 1000")
elif(height>=5000):
    print("Turn Around")
else:
    print("Enter positive altitude")


# In[4]:



# Day 3 Assignment Question2

lower = 1
upper = 200

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:





# In[ ]:




