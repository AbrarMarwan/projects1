import pandas as pd
# ls=["abrar","Ghaida","haifa","haya","aml","rahf"]
# ser=pd.Series(ls)
# print(ser)
# #ترتب ك جدول
# ser=pd.Series(ls,index=['a','b','c','d','e','f'])
# print(ser)
# print(ser.values)
# print(ser.index)
# ser=pd.Series(ls)
# print(ser.index)
lst=[1000,2000,3000,4000,5000,6000]
ser=pd.Series(lst)
print(ser.describe())
#####
frame=pd.DataFrame(lst,index=['a', 'b', 'c', 'd', 'e', 'f'],columns=["frist"])
print(frame)




