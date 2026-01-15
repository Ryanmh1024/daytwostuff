# %%
# @Ryanmh1024 ➜ /workspaces/daytwostuff (main)

#%%
# The environment should not be included in the repo because it
# could be system specific and any packages will go into the
# requirements.txt file

#%%
# (.venv) @Ryanmh1024 ➜ /workspaces/daytwostuff (main)
# The terminal display "path" is different because it has a
# .venv at the beginning

# %%
import pandas as pd
df = pd.read_csv('boardgamedata.csv')
df.head()

#%%
# There are local extensions and then codespaces extensions
# which are in separate spots

# 3 Advantages of Data Wrangler
# 1. It displays preliminary graphs for each column
# 2. It displays how many missing values are in each column
# 3. It displays how many distinct values are in each column

# %%
import plotly
print(plotly.__version__)
# %%
# We use a requirements.txt so that all the specific packages
# for the project are included in the repo so any person that
# wants to use the project can just download everything and use it immediately