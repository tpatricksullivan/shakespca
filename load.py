import pandas as pd
import pandasql

df = pd.read_csv("data/CSV/ubiquity.csv")
playmap = pd.read_csv("playmap.csv")

# Bring in better play names
q = """select playmap.Play, df.*
    from df
    inner join playmap
        on playmap.text_name = df.text_name"""
df = pandasql.sqldf(q, locals())

print(df)