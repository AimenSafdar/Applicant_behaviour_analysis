import pandas as pd

df = pd.read_csv("Applicant behaviour data.csv")
df.head()
print(df.head())

##Basic checking
df.shape
print(df.shape)
df.info()
print(df.info())
df.describe()
print(df.describe())
print(df.columns)
print(df.dtypes)
##Data quality check
#checking for null values
print("The null value is:",df.isnull().sum())
#checking for duplicate values
print("The duplicated values are:",df.duplicated().sum())