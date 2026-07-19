import pandas as pd 

df = pd.read_csv("data.csv")
# print(df.loc[0])
# Average house price
group = df.groupby("suburb")
av_price = group["price"].mean()
print(av_price)


# Price by suburb
# Bedrooms vs price
# Best value suburbs


