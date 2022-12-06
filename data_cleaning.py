import pandas as pd
import csv

file = pd.read_csv("merged.csv")
del file["Luminosity"]
file.to_csv("cleaned_file.csv")
print(file)

