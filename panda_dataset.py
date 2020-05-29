
#https://blog.faradars.org/pandas-from-zero-to-hero/



import numpy as np
import pandas as pd

#############################  data or array ####################################

data = np.array(['a', 'b', 'c', 'd'])
#pandas.Series( data, index, dtype, copy)
s2 = pd.Series(data)
print(s2)
print("--------------------------------------------------")
s3 = pd.Series(data, index=[100, 101, 102, 103])
print(s3)
print("--------------------------------------------------")
s4 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s4[0])
print("--------------------------------------------------")


######################## DataFrame or 2d array #####################################

#pandas.DataFrame( data, index, columns, dtype, copy)
data2 = [['Alex',10],['Bob',12],['Clarke',13]]
print(data2)
df = pd.DataFrame(data2,columns=['Name','Age'],dtype=float)
print(df)
print("--------------------------------------------------")

df = pd.DataFrame({
    "Column1": [1, 4, 8, 7, 9],
    "Column2": ['a', 'column', 'with', 'a', 'string'],
    "Column3": [1.23, 23.5, 45.6, 32.1234, 89.453],
    "Column4": [True, False, True, False, True]
})
print(df)
print("--------------------------------------------------")

items = [['Phone', 2000], ['TV', 1500], ['Radio', 800]]
df = pd.DataFrame(items, columns=['Item', 'Price'], dtype=float)
print(df)
print("خلاصه داده‌های َامل کم ترین بیشترین درصد های متفاوت اماری 25%")
print(df.describe())
print("--------------------------------------------------")

print("وارد کردن فایل با فرمتcsv ")
data = pd.read_csv('cars.csv')
print(data)
print("نمایش چند خط اول هر فایل ورودی برای مواقعی که فیل ها زیاد هستند ")
print(data.head())
print("نمایش چند سطر معین ")
print (data.loc[[0, 4, 7], ['Type']])
print (data.loc[:, ['Type', 'Capacity']])
print("--------------------------------------------------")

print("ادغام کردن چند فایل و یا ارایه ")
print("توجه ادغام به معنای کوئری است و می شود اشتراک اختلاف اجتماع و غیره گرفت ")
d = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'student_name': ['John', 'Emily', 'Kate', 'Joseph', 'Dennis']
}
df1 = pd.DataFrame(d, columns=['subject_id', 'student_name'])
print(df1)

data = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'student_name': ['Brian', 'William', 'Lilian', 'Grace', 'Caleb']
}
df2 = pd.DataFrame(data, columns=['subject_id', 'student_name'])
print(df2)
print("ادغام اشتراک گیری ")
print(pd.merge(df1, df2, on='subject_id'))
print("--------------------------------------------------")

print("گروه بندی داده ها بر اساس موضوع خاص و از چند منبع مختلف ")


url = 'https://gist.githubusercontent.com/alexdebrie/b3f40efc3dd7664df5a20f5eee85e854/raw/ee3e6feccba2464cbbc2e185fb17961c53d2a7f5/stocks.csv'
df = pd.read_csv(url)
print(df)
symbols = df.groupby('symbol')
print(symbols.groups)

print("دستورات گروه بندی خاص")
def increased(idx):
    return df.loc[idx].close > df.loc[idx].open
print(df.groupby(increased).groups)
print(symbols['volume'].agg(np.mean))

for symbol, group in symbols:
    print(symbol)
    print(group)


aapl = symbols.get_group('AAPL')
print(aapl)

print(df.count())

print(df['volume'].value_counts(bins=4))


print("--------------------------------------------------")

print("الحاق Concatenation ")

df1 = pd.DataFrame(d, columns=['subject_id', 'student_name'])
print(df1)

data = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'student_name': ['Brian', 'William', 'Lilian', 'Grace', 'Caleb']
}
df2 = pd.DataFrame(data, columns=['subject_id', 'student_name'])
print(pd.concat([df1, df2]))

