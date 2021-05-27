#!/usr/bin/env python
# coding: utf-8

# In[39]:


palabra = input('Introduce una palabra: ').upper().replace(" ", "")


# In[40]:


print ((palabra)[::-1])


# In[41]:


if palabra == (palabra)[::-1]:
    print ('Si es palindromo')
else:
    print ('No es palindromo')

