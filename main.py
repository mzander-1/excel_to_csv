import pandas as pd

# Read the data from the excel file
readed_excel = pd.read_excel("data.xls")

# Save the data to a csv file
readed_excel.to_csv("data.csv", index=False)