#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
def longest_string(arr):
    strings=[s for s in arr if len(s)>5]
    if strings:
        return max(strings,key=len)
    else:
        return min(arr,key=len)
    sample_array=np.array(["apple","banana","orange","pineapple","grapes","melons"])
    longest_string_output=longest_string(sample_array)
    print("Longest string with more than 5 characters:")
    print(longest_string_output)
    





# In[ ]:





# In[ ]:




