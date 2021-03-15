import pandas as pd
from pandas.io.parsers import read_csv
import plotly.express as px

df = pd.read_csv("data.csv")
#fig = px.line(df, x="Year", y="Per capita income", color="Country", title='Per Capita Income')
#fig = px.(df, x='Country', y='InternetUsers')
fig = px.scatter(df, x="date", y="cases", color="Country" , size_max=60)
fig.show()
