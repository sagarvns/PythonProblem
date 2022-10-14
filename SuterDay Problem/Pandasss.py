import pandas as pd
l1=[1,2,3,4,5]
data1=pd.DataFrame(l1)
print(data1)
dt1={'fruit':['apple','mango','orange'], 'count':[12,24,36]}
print(pd.DataFrame(dt1))


iris=pd.read_csv('iris.csv')
iris.head()
