import pandas as pd
import numpy as np

df = pd.read_excel(r'/Users/703235761MAC/Documents/niraj-git/ba/ba.xlsx', sheet_name='Data')

sales_q = df[df.columns[6]]
sales_v = df[df.columns[7]]
transactions = df[df.columns[1]]
sub_category = df[df.columns[5]]
category = df[df.columns[4]]

# required overview
total_sales = sales_v.sum()
unique_trans = np.unique(transactions)
unique_trans_count= len(unique_trans)
sales_quantity = sales_q.sum()

#ave transactions
df_transactions = pd.DataFrame({
    'trnx': transactions,
    'trnx_value': sales_q * sales_v
})

ave_transaction_value = df_transactions.groupby("trnx").agg(np.sum).mean()

#items per trans
df_transactions_q = pd.DataFrame({
    'trnx': transactions,
    'sales_q': sales_q
})
items_per_trans = df_transactions_q.groupby('trnx').agg(np.sum).mean()

#price per item

price_per_item = pd.DataFrame({
    'sub_category': sub_category,
    'sales_v': sales_v
}).groupby('sub_category').agg(np.sum).mean()

print(df.head())