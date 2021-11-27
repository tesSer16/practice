#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

data = pd.read_csv('test.csv', header = None)


# In[2]:


lotto_list = [] 
for row in range(data.shape[0]):
    for game in range(int(data.iloc[row, 3])):
        try:
            lotto_list.append(data.iloc[row, 0])
        except:
            print(data.iloc[row, : ])


# In[44]:


def lotto(lotto_list, size, print_out = True):
    win_num = np.random.choice(range(0, len(lotto_list)), size = size, replace = False)
        
    wins = []
    for i in win_num:
        wins.append(lotto_list[i])
        
    if print_out == True: 
        for i in wins:
            print(i)
            
        print('\n')
    return wins


# In[ ]:





# In[45]:


def display(lotto_list = lotto_list):    
    print("에어팟 : "), lotto(lotto_list, 1)
    
    print("버즈 :"), lotto(lotto_list, 1)
    
    print("스피커 : "), lotto(lotto_list, 1)
    
    print("축하드립니다!")
    
    


# In[48]:


display(lotto_list)

