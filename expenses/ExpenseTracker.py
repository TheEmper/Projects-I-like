import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "expenses.csv")
# loading the data into the file
df = pd.read_csv(csv_path, parse_dates=["Date"])

# Defining what can be included in which category
categories = {
    "Groceries": ["walmart", "kroger", "aldi", "costco"],
    "Transport": ["uber", "lyft", "gas", "shell", "chevron"],
    "Entertainment": ["netflix", "spotify", "movie", "theater"],
    "Food & Drink": ["starbucks", "mcdonald", "burger", "restaurant"],
    "Shopping": ["amazon", "target", "mall"],
    "Rent & Utilities": ["rent", "electric", "water", "internet"],
    "Travel": ["delta", "airlines", "hotel"],
}

# Categorizing each expense
def categorize(description):
    desc = str(description).lower()
    for cat, keywords in categories.items():
        if any(keyword in desc for keyword in keywords):
            return cat
    return "Other"

df["Category"] = df["Description"].apply(categorize)

# Summarize 
df["Month"] = df["Date"].dt.to_period("M")
summary = df.groupby(["Month", "Category"])["Amount"].sum().unstack(fill_value=0)

print("\nExpense Summary by Month:")
print(summary)

# Making the chart

summary.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Monthly Expenses by Category")
plt.ylabel("Amount ($)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
