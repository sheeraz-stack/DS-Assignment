#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q - Scenario: A company wants to analyze the sales performance of its products in different regions. They have collected the
    following data:
    Calculate the mean sales for each region.


# In[58]:


import statistics
RegionA : [10, 15, 12, 8, 14]
RegionB : [18, 20, 16, 22, 25]

print("Mean of RegionA is %s"%statistics.mean(RegionA))
print("Mean of RegionB is %s"%statistics.mean(RegionB))


# In[ ]:


Q - A survey is conducted to measure customer satisfaction on a scale of 1 to 5. The data collected is as follows:
    Calculate the mode of the survey responses.


# In[30]:


import statistics
data= [4, 5, 2, 3, 5, 4, 3, 2, 4, 5]
print(statistics.mode(data))


# In[ ]:


Q -  A company wants to compare the salaries of two departments. The salary data for Department A and Department B
     Calculate the median salary for each department.


# In[65]:


import statistics
DepartmentA = [5000, 6000, 5500, 7000]
DepartmentB = [4500, 5500, 5800, 6000, 5200]
print(statistics.median(DepartmentA))
print(statistics.median(DepartmentB))


# In[ ]:


Q -  A data analyst wants to determine the variability in the daily stock prices of a company.


# In[1]:


data = [25.5, 24.8, 26.1, 25.3, 24.9]
Q1 = 24.8
Q3 = 26.1
Range = Q3 - Q1
print(Range)


# In[ ]:


Q - A study is conducted to compare the performance of two different teaching methods


# In[3]:


import statistics
ls1 = [85, 90, 92, 88, 91]
ls2 = [82, 88, 90, 86, 87]
print("Mean of ls1 is %s"%statistics.mean(ls1))
print("Mean of ls2 is %s"%statistics.mean(ls2))


# In[ ]:


Q - A company wants to analyze the relationship between advertising expenditure and sales.


# In[8]:


import numpy as np
x = [10, 15, 12, 8, 14]
y = [25, 30, 28, 20, 26]
pearsons_coefficient = np.corrcoef(x, y)
print("The pearson's coeffient of the x and y inputs are: \n" ,pearsons_coefficient)


# In[ ]:


Q - A survey is conducted to measure the heights of a group of people. The data collected is as follows:
   [160, 170, 165, 155, 175, 180, 170]
   Calculate the standard deviation of the heights.


# In[10]:


import statistics
data = [160, 170, 165, 155, 175, 180, 170]

sample_std = statistics.stdev(data)
population_std = statistics.pstdev(data)
print('standard deviation: ', sample_std)

