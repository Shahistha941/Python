#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # Dataframe

# ### Creating a dataframe

# In[176]:


#Using csv
df=pd.read_csv("weather_data.csv")


# In[178]:


df


# In[11]:


# using excel
df=pd.read_excel("weather_data.xlsx","Sheet1")
df


# In[12]:


#Using a dictionary
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
df


# In[15]:


#Using a list 
weather_data = [
    ['1/1/2017',32,6,'Rain'],
    ['1/2/2017',35,7,'Sunny'],
    ['1/3/2017',28,2,'Snow']
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


# In[16]:


# Using a tuple
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


# In[17]:


#Using a list of dictionaries
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
df


# ### Examining data frame

# In[127]:


# Display top rows
df.head()


# In[42]:


#Display bottom rows
df.tail()


# In[128]:


#Display specified number of rows
df.head(3)


# In[44]:


#Display specific rows
df[2:5]


# In[28]:


#Information about the dataframe
df.info()


# In[65]:


#Names of the columns
df.columns


# In[30]:


#Display the number of rows and columns
df.shape


# In[31]:


#Display statistical properties of all the numerical columns in the dataframe
df.describe()


# In[39]:


#Display unique values in a column
df['event'].unique


# In[40]:


df.to_string()


# In[48]:


#Display rows where a condition is satisfied
df[df['temperature']==32]


# In[129]:


df['temperature']==32


# In[199]:


df[['temperature','event']]


# In[201]:


df[df['event'].isin(['Snow','Sunny'])]


# In[52]:


#Display index
df.index


# In[54]:


#Setting index
df.set_index('temperature')


# In[55]:


df


# In[56]:


df.set_index('temperature',inplace=True)


# In[57]:


df


# In[59]:


df.loc[32]


# ### Read write excel csv

# In[84]:


#Reading csv as it is
df=pd.read_csv("stock_data.csv")
df


# In[89]:


#reading csv leaving few rows
df=pd.read_csv("stock_data.csv",skiprows=2)
df


# In[93]:


#Reading from a specified row as header
df=pd.read_csv("stock_data.csv",header=3)
df


# In[95]:


#When we dont have column names, we can use this to give names to columns
df=pd.read_csv("stock_data.csv",skiprows=0,header=None,names=["col1","col2","col3","col4","col5"])
df


# Skiprows will skip few rows, header will tell which row to select as header. When we dont have column names, we can give header as none and give column names

# In[98]:


#Read specified number of rows
df=pd.read_csv("stock_data.csv",nrows=3)
df


# In[97]:


df=pd.read_csv("stock_data.csv")
df


# We can see that there are invalid values in the data. We can change the null values while importing

# In[99]:


df = pd.read_csv("stock_data.csv", na_values=["n.a.", "not available"])
df


# In[101]:


#Replace invalid values with NaN for entire dataframe
df = pd.read_csv("stock_data.csv", na_values=["n.a.", "not available",-1])
df


# In[102]:


#Replace invalid values as per customisation
df = pd.read_csv("stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'people': ['not available','n.a.']
    })
df


# In[108]:


#Write to csv along with index
df.to_csv("new.csv")


# In[114]:


#Write to csv without index
df.to_csv("new.csv",index=False)


# In[109]:


#Write only specific columns into csv
df.to_csv("new.csv", columns=["tickers","price"], index=False)


# In[113]:


#Write without header and index
df.to_csv("new.csv",header=False, index=False)


# #### From excel

# In[115]:


df = pd.read_excel("stock_data.xlsx","Sheet1")
df


# In[116]:


#leaves two columns and 1 row in excel sheet 
df.to_excel("new.xlsx", sheet_name="stocks", index=False, startrow=2, startcol=1)


# Writing multiple dataframes to a excel

# In[122]:


df=pd.read_csv("weather_data.csv")
df1=df=pd.read_csv("stock_data.csv")


# In[123]:


with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df1.to_excel(writer, sheet_name="stocks")
    df.to_excel(writer, sheet_name="weather")


# ## Null Value Interpretation

# In[134]:


dfNull=pd.read_csv("weather_data_null.csv") 
dfNull


# In[137]:


type(dfNull['day'][0])


# In[142]:


dfNull = pd.read_csv("weather_data_null.csv",parse_dates=['day'])
dfNull


# In[143]:


type(dfNull.day[0])


# In[144]:


#Changing the index
dfNull.set_index('day',inplace=True)
dfNull


# ###### Drop rows with null values

# In[145]:


dfNull.dropna()


# ###### Fill all NaN with one specific value

# In[148]:


new_df = dfNull.fillna(0)
new_df


# ###### Fill na using column names and dict

# In[150]:


new_df = dfNull.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'No Event'
    })
new_df


# ###### Use method to determine how to fill na values forwardfill or backward fill

# In[157]:


# new_df = df.fillna(method="ffill")
new_df=dfNull.ffill()
new_df


# In[159]:


new_df = df.fillna(method="bfill")
# new_df=dfNull.bfill()
new_df


# ###### Use of axis to fill 

# In[160]:


new_df = dfNull.fillna(method="bfill", axis="columns") # axis is either "index" or "columns"
new_df


# In[164]:


new_df = dfNull.fillna(method="ffill", axis="columns") # axis is either "index" or "columns"
new_df


# In[165]:


#limit Parameter
new_df = dfNull.fillna(method="ffill",limit=1)
new_df


# In[169]:


df=pd.read_csv("stock_data.csv")
df


# ###### Replace

# In[170]:


#Replacing a single valie
#
new_df = df.replace('not available', value=np.NaN)
new_df


# In[172]:


#Replacing a set of values
# 
new_df = df.replace(to_replace=['not available','n.a.'], value=np.NaN)
new_df


# In[175]:


#Replace per column basis
new_df = df.replace({
        'eps': 'not available',
        'price': 'n.a.',
        'people': 'n.a.'
    }, np.nan)
new_df


# ###### Group By function

# In[47]:


df = pd.read_csv("weather_by_cities.csv")
df


# In[48]:


#Groupby will create a object 
g = df.groupby("city")
g


# In[50]:


g.get_group('mumbai')


# In[14]:


#Accessing a group
g.get_group('new york')['temperature']


# In[11]:


g.sum()


# In[56]:


g.get_group('mumbai').index


# In[61]:


#Using statistics on group
g.mean()


# In[73]:


g.get_group('mumbai').describe()


# # Series
# 

# In[74]:


#Creating an empty Series
s=pd.Series()
print(s)


# In[80]:


#Creating using an array
a=np.array([1,2,3,4])
s1=pd.Series(a)
print(s1)


# In[79]:


#Creating Series using an array with custom index
s2=pd.Series(a,index=['a','b','c','d'])
print(s2)


# In[86]:


#Creating Series from a List
b=["Hello","Numpy","Ninja"]
s3=pd.Series(b)
print(s3)


# In[87]:


dict1= {'a':0,'b':1,'c':2}
s4=pd.Series(dict1)
print(s4)


# In[88]:


# Creating from a scalar value

g = pd.Series(10, index =[0, 1, 2, 3,4,5])
print(g)


# In[108]:


#Creating using functions
h=pd.Series(np.arange(1,10,2))
print(h)


# In[97]:


#Accesing the Series
l1=list("NumpyNinja")
l1
ser=pd.Series(l1)
print(ser)


# In[118]:


#Accessing Using location
ser[:5]


# In[119]:


# Access using Index
print(ser[7])


# In[104]:


ser1 = pd.Series(l1,index=np.arange(11,21))


# In[105]:


ser1


# In[106]:


ser1.head()


# In[115]:


h.index=['a','b','c','d','e']
print(h)


# In[113]:


h.reset_index()


# In[117]:


h.reset_index(drop=True)


# In[129]:


print(s2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             -
print("\n",s2.loc['c'])
print("\n",s2.iloc[3])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[107]:


df.index


# In[114]:


ser1=pd.Series(data=data['EMPID'])


# In[115]:


ser1


# In[113]:


data['EMPID']


# # NUMPY

# In[46]:


#creating a numpy array from a list
arr=np.array([1,2,3])
arr


# In[93]:


#creating array from tuple
arrTup=np.array(('x','y','z'))
arrTup


# In[39]:


#creating array of zeros
a=np.zeros((2,3))
a


# In[44]:


#creating array of 1's
b=np.ones((3,2))
b


# In[45]:


#creating array with a single value
c=np.full((3,3),5)
c


# In[100]:


#creating array with random values
d=np.random.random((2,3))
d


# In[38]:


#creating using random integer values in given range
d1=np.random.randint(1,10,(2,4))
print(d1)


# In[3]:


#creating array with step size arange(start,end,step)
e=np.arange(1,10,2)
e


# In[33]:


#creating array with equal spacing
f=np.linspace(1,10,5)
f


# In[37]:


len(f)


# In[38]:


# Reshaping 3X4 array to 2X2X3 array
arr1 = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
 
newarr = arr1.reshape(3,2,2)
newarr


# In[119]:


#Get Dimension
newarr.ndim


# In[123]:


# Getting shape
a.shape


# In[127]:


# Get Type
arr1.dtype


# In[39]:


#Getting number of elements
newarr.size


# In[40]:


len(newarr)


# # Array Slicing
# 

# In[33]:


array = np.array([['a1','b1','c1','d1','e1'],
                 ['a2','b2','c2','d2','e2'],
                 ['a3','b3','c3','d3','e3'],
                 ['a4','b4','c4','d4','e4']]
                 
                )


# In[74]:


array


# In[17]:


# Get a specific element [r,c]
array[0,1]


# In[20]:


array[-1,-2]


# In[133]:


#Get a specific row
array[3,:]


# In[134]:


#Get a specific Column
array[:,2]


# In[135]:


#Get using [startindex:stopindex:stepsize]
array[::2,::3]


# In[132]:


array[:,2:]


# In[116]:


array[::2, ::3]


# In[27]:


array[-3:-1,:]


# # Basic operations on Numpy

# In[51]:


oArr=np.array([[1,2,3],
     [4,5,6],
     [7,8,9]])


# In[52]:


np.sum(oArr,axis=0)


# In[7]:


#Addition in array
oArr+1


# In[8]:


#Multiplication
oArr*2


# In[9]:


# Dividing with 2
oArr/2


# In[10]:


# Sum along axis down the rows
np.sum([[1,2],[3,4]], axis=0)


# In[11]:


# Sum along axis down the columns
np.sum([[1,2],[3,4]], axis=1)


# In[15]:


#Adding 2 arrays
a=np.arange(1,6).reshape(1,5)
print(a)
b=np.linspace(1,15,15).reshape(3,5)
print(b)


# In[16]:


np.add(a,b)


# In[32]:


a1=np.random.randint(1,10,(2,5))
print(a1)
b1=np.random.randint(11,30,(2,5))
print(b1)
print(np.add(a1,b1))


# In[12]:


# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])


# In[13]:


a


# In[14]:


print(a.T)


# In[30]:


#Maximum element in an array
print ("Largest element is:", a.max())
print ("Row-wise maximum elements:",
                    a.max(axis = 1))
print ("Column-wise maximum elements:",
                    a.max(axis = 0))


# In[32]:


#Minimum element in an array
print ("Smallest element is:", a.min())
print ("Row-wise Minimum elements:",
                    a.min(axis = 1))
print ("Column-wise Minimum elements:",
                    a.min(axis = 0))


# In[12]:


#Sorting of Array
a = np.array([[1, 4, 2],
                 [3, 4, 6],
              [0, -1, 5]])
print("Array\n",a)
print ("Array elements in sorted order:\n",np.sort(a, axis = None))
print("Sorted array\n" , np.sort(a))
# sort array row-wise
print ("Column-wise sorted array:\n",
                np.sort(a, axis = 0))


# Be careful when copying array

# In[47]:


abcd=([1,2,3])
print(abcd)


# In[44]:


dcba=abcd
print(dcba)


# In[46]:


dcba[2]=30
print(dcba)
print(abcd)


# In[49]:


dcba=abcd.copy()
print(dcba)
print(abcd)
dcba[2]=20
print(dcba)
print(abcd)


# # Stacking and Splitting 

# In[13]:


a = np.array([[1, 2],
              [3, 4]])
  
b = np.array([[5, 6],
              [7, 8]])


# In[16]:


#Vertical Stacking stacks one above other
print('Vertical Stacking',np.vstack((a,b)))


# In[20]:


#Horizontal Stacking, stacks one beside other
print('Horizontal Stacking',np.hstack((a,b)))


# In[22]:


#Column Stacking
c=np.array([9,10])
print('Column Stacking',np.column_stack((a,c)))


# In[24]:


#Concatenate
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))
print("\nConcatenating to 1st axis:\n", np.concatenate((a, b), 0))


# In[41]:


# Splitting 
a=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(a)


# In[46]:


# horizontal splitting
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2))


# In[43]:


#Horizontal splitting on specified position
np.hsplit(a,np.array([2,3,5]))


# In[34]:


#Vertical Split
print("Splitting along Vertical axis into 2 parts:\n", np.vsplit(a, 2))


# In[44]:


#Horizontal splitting on specified position
np.vsplit(a,np.array([2,3,5]))


# In[35]:


# Splitting along axis
print("Splitting along specified axis into 2 parts:\n", np.split(a, 2))


# In[40]:


print("Splitting along specified axis into 2 parts:\n", np.array_split(a, 3,axis=1))

