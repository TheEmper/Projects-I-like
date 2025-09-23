import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(BASE_DIR, "customers.csv")
# loading the data into the file
df = pd.read_csv(csv_path)

# Clustering features
X = df[["Age", "Annual_Income", "Spending_Score"]]

# scaling the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Running kmeans
kmeans = KMeans(n_clusters=4, random_state=42)
df["Segment"] = kmeans.fit_predict(X_scaled)

# summarize
print("\nCustomer Segmentation Results:")
print(df.groupby("Segment")[["Age", "Annual_Income", "Spending_Score"]].mean())

# plot chart
plt.figure(figsize=(8,6))
plt.scatter(df["Annual_Income"], df["Spending_Score"], 
            c=df["Segment"], cmap="viridis", s=80, alpha=0.7, edgecolors="k")

plt.xlabel("Annual Income ($)")
plt.ylabel("Spending Score")
plt.title("Customer Segments")
plt.colorbar(label="Segment")
plt.show()
