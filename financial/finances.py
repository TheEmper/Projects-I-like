import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "financials.csv")
# loading the data into the file
df = pd.read_csv(csv_path)

# Calculating what equals what

df["Gross_Profit"] = df["Revenue"] - df["COGS"]
df["Gross_Margin"] = df["Gross_Profit"] / df["Revenue"]
df["Operating_Margin"] = df["Operating_Income"] / df["Revenue"]
df["Net_Margin"] = df["Net_Income"] / df["Revenue"]
df["Debt_Ratio"] = df["Total_Liabilities"] / df["Total_Assets"]
df["ROE"] = df["Net_Income"] / df["Equity"]
df["Current_Ratio"] = df["Current_Assets"] / df["Current_Liabilities"]

# Summarize
print("\n===== Financial Statement Analysis =====\n")
print(df[[
    "Year", "Revenue", "Net_Income", 
    "Gross_Margin", "Operating_Margin", "Net_Margin",
    "Debt_Ratio", "ROE", "Current_Ratio"
]])

# the chart
plt.figure(figsize=(10,6))

plt.plot(df["Year"], df["Gross_Margin"], marker="o", label="Gross Margin")
plt.plot(df["Year"], df["Operating_Margin"], marker="o", label="Operating Margin")
plt.plot(df["Year"], df["Net_Margin"], marker="o", label="Net Margin")

plt.title("Profitability Margins Over Time")
plt.xlabel("Year")
plt.ylabel("Ratio")
plt.legend()
plt.grid(True)
plt.show()
