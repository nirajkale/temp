import pandas as pd
import numpy as np

df = pd.read_excel(r'/Users/703235761MAC/Documents/niraj-git/ba/ba.xlsx', sheet_name='Data')
# sl451711825@outlook.com

#filter for members only
members_columns = df.columns[2]
sales_q = df[df.columns[6]]
sales_v = df[df.columns[7]]

groups = pd.DataFrame({
    'members': df[members_columns],
    'sales': sales_q * sales_v
}).groupby("members")

member_sales = groups.get_group('N')['sales'].sum()
non_member_sales = groups.get_group('Y')['sales'].sum()

member_sales_participation = member_sales*100 / (member_sales + non_member_sales)

groups = pd.DataFrame({
    'members': df[members_columns],
    'sales_q': sales_q
}).groupby("members")

member_sales_q = groups.get_group('N')['sales_q'].sum()
non_member_sales_q = groups.get_group('Y')['sales_q'].sum()

member_trnx_participation = member_sales_q *100 / (member_sales_q + non_member_sales_q )

#filter the main table
df = df[df[members_columns]=='Y']

sales_q = df[df.columns[6]]
sales_v = df[df.columns[7]]
transactions = df[df.columns[1]]
sub_category = df[df.columns[5]]
category = df[df.columns[4]]

#total member sales

sales = sales_v.sum()
visited_members = transactions.unique().shape[0]
num_transactions = transactions.shape[0]
sales_qunatity = sales_q.sum()