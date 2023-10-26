import pandas as pd

html = "https://www.bahasajepangbersama.com/2016/07/daftar-kanji-jlpt-level-n3.html"
csv = "my_file.csv"

# 1. Read all HTML tables from a given URL
tables = pd.read_html(html)

# 2. Filter the first table (tables[0]) to exclude the first 2 rows
filtered_table = tables[0].iloc[1:]

# 3. Write the filtered table to the CSV file
filtered_table.to_csv(csv, index=False)
