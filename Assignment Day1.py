#!/usr/bin/env python
# coding: utf-8

# Assignment 1 ( different functions of the string in python )

# In[3]:


#format()

print("My Name is {0}".format("Pankaj"))
print("I like {0} and {1}".format("Java", "Python"))
# same as above
print("I like {} and {}".format("Java", "Python"))

# index can be in any order
print("I like {1} and {0}".format("Java", "Python"))


# In[5]:


#replace()

s = 'Java is Nice'

# simple string replace 
str_new = s.replace('Java', 'Python')
print(str_new)

# replace character in string
s = 'post'
str_new = s.replace('p', 't')
print(str_new)


# In[6]:


#find()

s = 'abcd1234dcba'
print(s.find('a'))  
print(s.find('cd'))  
print(s.find('1', 0, 5))  
print(s.find('1', 0, 2)) 


# In[7]:


#translate()

s = 'ABCDBCA'

translation = s.maketrans({ord('A'): 'a', ord('B'): ord('b')})  
print(s.translate(translation))


# In[8]:


#lowercase()

s = '987abcDEF%$'

print('Lowercase String =', s.lower())
print('Original String =', s)


# Assignment 2 (different functions of the list object in python)

# In[9]:


# sort()

prices = [238.11, 237.81, 238.91]
prices.sort()
print(prices)


# In[12]:


#append()

months = ['January', 'February', 'March']
months.append('April')
print(months)


# In[11]:


#extend()

x = [1, 2, 3]
x.extend([4, 5])
x


# In[13]:


#max()

prices = [159.54, 37.13, 71.17]
price_max = max(prices)
print(price_max)


# In[15]:


#len()

stock_price_1 = [50.23]
stock_price_2 = [75.14, 85.64, 11.28]

print('stock_price_1 length is ', len(stock_price_1))
print('stock_price_2 length is ', len(stock_price_2))


# Assignment 3 (default functions of dictionary)

# In[51]:


#len(dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Length : %d" % len (Dict))


# In[52]:


#str(dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("printable string:%s" % str (Dict))


# In[57]:


#items(dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))


# In[58]:


#type(dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("variable Type: %s" %type (Dict))


# In[62]:


#update(dict)

Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)

