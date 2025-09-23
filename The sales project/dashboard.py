import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "sales.csv")
# loading the data into the file


df = pd.read_csv(csv_path)

# summarieze
total_sales = df["Sales"].sum()
sales_by_region = df.groupby("Region")["Sales"].sum()
sales_by_product = df.groupby("Product")["Sales"].sum()
sales_over_time = df.groupby("Date")["Sales"].sum()


print("\n===== Sales Dashboard =====")
print(f"Total Sales: ${total_sales:,.2f}\n")
print("Sales by Region:")
print(sales_by_region)
print("\nSales by Product:")
print(sales_by_product)

# making the charts/graphs

plt.figure(figsize=(12,6))

# 1. Sales over time
plt.subplot(1, 3, 1)
sales_over_time.plot(kind="line", marker="o")
plt.title("Sales Over Time")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)

# 2. Sales by region
plt.subplot(1, 3, 2)
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales ($)")

# 3. Sales by product

plt.subplot(1, 3, 3)
sales_by_product.plot(kind="bar", color="orange")
plt.title("Sales by Product")
plt.ylabel("Sales ($)")

plt.tight_layout()
plt.show()
