#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


random.randint(1,6)


# In[3]:


random.randint(1,6)


# In[4]:


i = 0
while i !=3:
    i =random.randint(1,6)
    print(i)


# In[5]:


dice= [1,2,3,4,5,6]
random.choice(dice)
random.choice(dice)


# In[6]:


random.choice(dice)


# In[7]:


i = 2
j = 5
while i<=32 or j >=1:
    print(i,j)
    i *= 2
    j -= 1


# In[9]:


x = int(input())
while x >= 1350:
    x -= 1350
    print(x)


# In[ ]:




