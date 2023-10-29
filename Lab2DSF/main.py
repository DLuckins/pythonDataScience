# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"dataset.xlsx")

df.plot.line(y="NewTime")
df.hist("NewTime")
df.hist("NewTime", cumulative=True, density=True, bins=100, histtype='step')
df.plot.line(y="Total")
df.hist("Total")
df.hist("Total", cumulative=True, density=True, bins=100, histtype='step')
df.plot.bar(y="Rate")

stats1 = df["NewTime"].describe(percentiles=[0.9, 0.95, 0.99])
stats2 = df["Total"].describe(percentiles=[0.9, 0.95, 0.99])
stats3 = df["Rate"].describe(percentiles=[0.9, 0.95, 0.99])
n = len(df['NewTime'])
print(df)
print(stats1, "\nSkewness:", stats1.skew(), "\nKurtosis:", stats1.kurtosis())
print(stats2, "\nSkewness:", stats1.skew(), "\nKurtosis:", stats1.kurtosis())
print(stats3, "\nSkewness:", stats1.skew(), "\nKurtosis:", stats1.kurtosis())
print(df["Rate"].value_counts())
plt.show()
