'''

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)                                '''

'''

# Pandas package can be referred to as pd instead of pandas.

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)                                   '''

'''

#Checking Pandas Version:

import pandas as pd

#The version string is stored under __version__ attribute.
print(pd.__version__)                             '''

'''

#Pandas Series: Create a simple Pandas Series from a list:
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)           '''


#Pandas Series:-     Labels

'''
#Return the 1st vlue of the series:

import pandas as pd

fruits = ["Apple", "Banana", "Amrud"]

myvar = pd.Series(fruits)

print(myvar[0])        '''

'''

#Create your own labels:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)                       '''

'''

#can access an item by referring to the label
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])                     '''


#Key/Value Objects as Series:

'''
#Create a simple Pandas Series from a dictionary

import pandas as pd

mydata = {'Name': 'Deepak', 'Age': 27, 'Address': 'Sarangpur 465697'}

myvar = pd.Series(mydata)

print(myvar)                        '''

'''
#Create a Series using only data from "day1" and "day2":

import pandas as pd

mydata = {'Name': 'Deepak', 'Age': 27, 'Address': 'Sarangpur 465697'}

myvar = pd.Series(mydata, index=['Name', 'Age'])

print(myvar)                 '''


#DataFrames:

'''
#Create a dataFrame: Create a DataFrame from two Series:

import pandas as pd

Mydata = {
  "Subject": ["Engineering Graphics", "DBMS", "Mathematics"],
  "Lecture_Timing": ["9:30 AM", "11:30 AM", "1:00 PM"]
}

myvar = pd.DataFrame(Mydata)

print(myvar)           '''

'''

#Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)                         '''

'''

#Locate Row:-

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

# use the loc attribute to return one or more specified row(s)
print(df.loc[0])
                             '''

'''

#Return Row 0, 1.
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

#use a list of indexes:
print(df.loc[[0, 1]])                '''

'''

#Named Indexes:-   Add a list of names to give each row a name:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)                            '''

'''

#Named Indexes:-   Locate Named Indexes

#Return  "day2"and "day3:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1","day2", "day3"])
#refer to the named index:
print(df.loc[["day2", "day3"]])        '''

'''

#Load Files Into a DataFrame:-

#Load a comma separated file (CSV file) into a DataFrame:

import pandas as pd

df = pd.read_csv("C:\\Users\\Deepak Mewada\\Downloads\\data.csv")

print(df)                                    '''

'''

#Pandas Read CSV:-  Read CSV Files


#Load the CSV into a DataFrame:

import pandas as pd

df = pd.read_csv("C:\\Users\\Deepak Mewada\\Downloads\\data.csv")

print(df.to_string())                           '''

'''
#max_rows:-
#Increase the maximum number of rows to display the entire DataFrame:

import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv("C:\\Users\\Deepak Mewada\\Downloads\\data.csv")

print(df)             '''



#Pandas Read JSON:

'''
#Load the JSON file into a DataFrame:

import pandas as pd


df = pd.read_csv("C:\\Users\\Deepak Mewada\\Downloads\\JSON.csv")

#use to_string() to print the entire DataFrame.
print(df.to_string())               '''


'''

#Dictionary as JSON:-

#Load a Python Dictionary into a DataFrame:

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)                '''


#Pandas - Analyzing DataFrames:

'''
#Viewing the Data:    Get a quick overview by printing the first 10 rows of the DataFrame:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

#The head() method returns the headers and a specified number of rows, starting from the to
print(df.head(10))        '''

'''

# if the number of rows is not specified, the head() method will return the top:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')
print(df.head())                                                       '''

'''

#tail() method for viewing the last rows of the DataFrame

#Print the last 5 rows of the DataFrame:
import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

#tail() method returns the headers and a specified number of rows, starting from the bottom
print(df.tail())               '''

'''

#Info About the Data:  using info() method

import pandas as pd

df= pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

print(df.info())        '''


#Pandas :- Cleaning Data:   Cleaning Empty Cells

'''

#Return a new Data Frame with no empty cells:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

new_df = df.dropna()

print(new_df.to_string())              '''

'''

#If you want to change the original DataFrame, use the inplace = True argument:

#Remove all rows with NULL values:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

df.dropna(inplace = True)

print(df.to_string())                      '''

'''

#Replace Empty Values:-
#Replace NULL values with the number 130:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

#Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).
df.fillna(130, inplace = True)           '''


'''

#Replace Only For Specified Columns:-

#Replace NULL values in the "Calories" columns with the number 130:
import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).
df["Calories"].fillna(130, inplace = True)

print(df.to_string())                              '''

'''

#Replace Using Mean(), Median(), or Mode() methods:

#Calculate the MEAN, and replace any empty values with it:
import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')


x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68
print(df.to_string())                          '''

'''

#Calculate the MEDIAN, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())                        '''


'''

#Calculate the MODE, and replace any empty values with it:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())          '''

'''
#Pandas - Cleaning Data of Wrong Format:-

#Convert to date:

import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())               '''

'''
#Result/output:-

   Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130     409.1
1         60 2020-12-02    117       145     479.0
2         60 2020-12-03    103       135     340.0
3         45 2020-12-04    109       175     282.4
4         45 2020-12-05    117       148     406.0
5         60 2020-12-06    102       127     300.0
6         60 2020-12-07    110       136     374.0
7        450 2020-12-08    104       134     253.3
8         30 2020-12-09    109       133     195.1
9         60 2020-12-10     98       124     269.0
10        60 2020-12-11    103       147     329.3
11        60 2020-12-12    100       120     250.7
12        60 2020-12-12    100       120     250.7
13        60 2020-12-13    106       128     345.3
14        60 2020-12-14    104       132     379.3
15        60 2020-12-15     98       123     275.0
16        60 2020-12-16     98       120     215.2
17        60 2020-12-17    100       120     300.0
18        45 2020-12-18     90       112       NaN
19        60 2020-12-19    103       123     323.0
20        45 2020-12-20     97       125     243.0
21        60 2020-12-21    108       131     364.2
22        45        NaT    100       119     282.0
23        60 2020-12-23    130       101     300.0
24        45 2020-12-24    105       132     246.0
25        60 2020-12-25    102       126     334.5
26        60 2020-12-26    100       120     250.0
27        60 2020-12-27     92       118     241.0
28        60 2020-12-28    103       132       NaN
29        60 2020-12-29    100       132     280.0
30        60 2020-12-30    102       129     380.3
31        60 2020-12-31     92       115     243.0                      '''


'''
#Removing Rows:-    Remove rows with a NULL value in the "Date" column:

import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.dropna(subset=['Date'], inplace = True)

print(df.to_string())  '''


'''

Result/output:-

    Duration       Date  Pulse  Maxpulse  Calories
0         60 2020-12-01    110       130     409.1
1         60 2020-12-02    117       145     479.0
2         60 2020-12-03    103       135     340.0
3         45 2020-12-04    109       175     282.4
4         45 2020-12-05    117       148     406.0
5         60 2020-12-06    102       127     300.0
6         60 2020-12-07    110       136     374.0
7        450 2020-12-08    104       134     253.3
8         30 2020-12-09    109       133     195.1
9         60 2020-12-10     98       124     269.0
10        60 2020-12-11    103       147     329.3
11        60 2020-12-12    100       120     250.7
12        60 2020-12-12    100       120     250.7
13        60 2020-12-13    106       128     345.3
14        60 2020-12-14    104       132     379.3
15        60 2020-12-15     98       123     275.0
16        60 2020-12-16     98       120     215.2
17        60 2020-12-17    100       120     300.0
18        45 2020-12-18     90       112       NaN
19        60 2020-12-19    103       123     323.0
20        45 2020-12-20     97       125     243.0
21        60 2020-12-21    108       131     364.2
23        60 2020-12-23    130       101     300.0
24        45 2020-12-24    105       132     246.0
25        60 2020-12-25    102       126     334.5
26        60 2020-12-26    100       120     250.0
27        60 2020-12-27     92       118     241.0
28        60 2020-12-28    103       132       NaN
29        60 2020-12-29    100       132     280.0
30        60 2020-12-30    102       129     380.3
31        60 2020-12-31     92       115     243.0               '''



#Pandas - Fixing Wrong Data:-  Wrong Data
#Replacing Values:-

'''

# Set "Duration" = 45 instead of 450 in row 7

import pandas as pd

df= read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

df.loc[7,'Duration'] = 45
print(df.to_string())             '''


'''

#Loop through all values in the "Duration" column
#If the value is higher than 120, set it to 120:
import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())                         '''

'''

#Removing Rows:  remove the rows that contains wrong data

#Delete rows where "Duration" is higher than 120:
import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

# include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy

print(df.to_string())                '''

'''

#Discovering Duplicate:

# Returns True for every row that is a duplicate, otherwise False:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

print(df.duplicated())                      '''

'''
#Removing Duplicates:-

#Remove all dup
import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\dataset.csv')

#Notice that row 12 has been removed from the result
df.drop_duplicates(inplace = True)

print(df.to_string())                       '''

'''

#Pandas - Data Correlation:

#Show the relationship between the columns:

import pandas as pd

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

print(df.corr())                            '''


#Pandas - Plotting:-

'''
#Import pyplot from Matplotlib and visualize our DataFrame:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

df.plot()

plt.show()                      '''


#Scatter Plot:-

'''
# "Duration" for the x-axis and "Calories" for the y-axis.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()                            '''

'''

#create another scatterplot, where there is a bad relationship between the columns, like "Duration" and "Maxpulse", with the correlation 0.009403:

#A scatterplot where there are no relationship between the columns:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()                               '''



#Plot Hostogram:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Deepak Mewada\\Downloads\\data.csv')

df["Duration"].plot(kind = 'hist')

plt.show()










