"""
Supermarket Sales Analysis
Author: Azhar Paraouty
Purpose: Business performance analysis using transactional data
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data_raw/SampleSuperstore.csv")

# Basic inspection
print(df.head())
print(df.info())

# ======================
# DESCRIPTIVE STATISTICS
# ======================

# Select numerical columns
numeric_cols = ["Sales", "Quantity", "Discount", "Profit"]

stats_summary = df[numeric_cols].describe()

print("\nDescriptive Statistics:")
print(stats_summary)

# Save statistics to Excel
stats_summary.to_excel("../outputs/descriptive_statistics.xlsx")

# Clean column names
df.columns = df.columns.str.strip()

# Save clean copy to Excel
df.to_excel("../data_clean/supermarket_clean.xlsx", index=False)

# ======================
# DISCOUNT ANALYSIS
# ======================

discount_analysis = (
    df.groupby("Discount")
      .agg(
          avg_profit=("Profit", "mean"),
          total_profit=("Profit", "sum"),
          order_count=("Profit", "count")
      )
      .reset_index()
)

print("\nDiscount analysis (top rows):")
print(discount_analysis.head())

print("\nDiscount analysis (bottom rows):")
print(discount_analysis.tail())

discount_analysis.to_excel("../outputs/discount_analysis.xlsx", index=False)

# ======================
# ANALYSIS
# ======================

# 1. Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure()
category_profit.plot(kind="bar", title="Profit by Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("../charts/profit_by_category.png")
plt.close()

# 2. Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure()
region_sales.plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("../charts/sales_by_region.png")
plt.close()

# 3. Discount vs Profit
discount_profit = df.groupby("Discount")["Profit"].mean()

plt.figure()
discount_profit.plot(kind="line", title="Average Profit vs Discount")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig("../charts/discount_vs_profit.png")
plt.close()

print("Analysis complete. Outputs saved.")