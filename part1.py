# %%
import pandas as pd
import numpy as np


# %%
car = pd.read_csv("quikr_car.csv")

# %%
car.shape

# %%
car.head()

# %%
car.info()

# %% [markdown]
# # Quality of data
# 1. Need to have consistent name
# 2. Year has few non numeric values
# 3. Need to change data type of Year to Int
# 4. Company has few numeric values and dataype need to be changed to String
# 5. Price datatype is object need to change it to int
# 6. price has commas
# 7. kms in last need to remove, nan values, need to remove few records
# 8. fuel_type has nan values

# %%
car = car[car["year"].str.isnumeric()]
car["year"] = car["year"].astype(int)
# %%
