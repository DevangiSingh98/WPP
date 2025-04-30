import pandas as pd

asking_prices = pd.Series([13000, 15000, 18000, 11000, 17000])
fair_prices = pd.Series([13500, 16000, 17000, 12000, 17500])

good_deals = asking_prices < fair_prices


good_deal_indices = list(good_deals[good_deals].index)

print("Indices of good deals:", good_deal_indices)
