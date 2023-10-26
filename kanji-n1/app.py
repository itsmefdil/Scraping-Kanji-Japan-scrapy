import pandas as pd

html = "https://nipponbako.com/list-of-kanji/jlpt-n3"
csv = "kanji-n1.csv"

# 1. Read all HTML tables from a given URL
tables = pd.read_html(html)

# 2. Filter the first table (tables[0]) to exclude the first 2 rows
filtered_table = tables[0].iloc[1:]


# 3. Write the filtered table to the CSV file
filtered_table.to_csv(csv, index=False)
