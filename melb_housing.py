import pandas as pd 

df = pd.read_csv("data.csv")
# print(df.loc[0])
# Average house price
average_price = df["price"].mean()
# print(average_price)

# Price by suburb
group = df.groupby("suburb")
av_price = group["price"].mean()
# print(av_price)


#average price per bedroom
group = df.groupby("bedrooms")
av_price = group["price"].mean()
print(av_price)

#Best value suburbs
group = df.groupby("suburb")
least_dist = group["distance_from_cbd_km"].max()
print(least_dist)