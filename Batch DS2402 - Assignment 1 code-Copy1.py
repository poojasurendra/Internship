#!/usr/bin/env python
# coding: utf-8

# In[2]:


def func(a, b):
 return b if a == 0 else func(b % a, a)
print(func(30, 75))


# In[3]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))


# In[4]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3={99,22,17}
print(len(set1 + set2 + set3))


# In[5]:


print(4**3 + (7 + 5)**(1 + 1))


# In[22]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
}


# In[24]:


for ship, captain in captains.items():
 print(ship, captain)


# In[8]:


captains = {dict}


# In[9]:


captains


# In[10]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
}


# In[11]:


captains


# In[13]:


for ship, captain in captains.items():
 print(f"The {ship} is captained by {captain}.")


# In[16]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
 "Discovery": "unknown",
}


# In[17]:


captains


# In[18]:


for ship, captain in captains.items():
 print(f"The {ship} is captained by {captain}.")


# In[20]:


del captains["Discovery"]


# In[21]:


captains


# In[ ]:




