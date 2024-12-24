import pandas as mypd
mypd_dataframe = mypd.read_csv('query_eg.csv', index_col='myname')
mypd_dataframe.sort_index(inplace=True)
mypd_dataframe.rename(columns={'mysalary':'My Salary'}, inplace=True)
print(mypd_dataframe)
print('-'*50)
# mypd_dataframe.query("My salary <45000", inplace=True) ----> Invalid
mypd_dataframe.query("`My Salary` <45000", inplace=True) # ----> valid
print(mypd_dataframe)