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
# EXPLORATORY ANALYSIS
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

print("Exploratory Analysis complete. Outputs saved.")

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
# LOSS DRIVERS (HIGH DISCOUNT)
# ======================

# Filter transactions with high discount and negative profit
high_discount_losses = df[
    (df["Discount"] >= 0.30) & (df["Profit"] < 0)
]

print("\nHigh-discount loss transactions:")
print(high_discount_losses.shape)

# ======================
# Loss by Category
# ======================
loss_by_category = (
    high_discount_losses
    .groupby("Category")["Profit"]
    .sum()
    .sort_values()
)

print("\nLoss by Category (Discount ≥ 30%):")
print(loss_by_category)

# ======================
# Loss by Sub-Category
# ======================
loss_by_subcategory = (
    high_discount_losses
    .groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)

print("\nLoss by Sub-Category (Discount ≥ 30%):")
print(loss_by_subcategory.head(10))  # worst offenders

# ======================
# Loss by Region
# ======================
loss_by_region = (
    high_discount_losses
    .groupby("Region")["Profit"]
    .sum()
    .sort_values()
)

print("\nLoss by Region (Discount ≥ 30%):")
print(loss_by_region)

# ======================
# Save summaries to Excel
# ======================
loss_by_category.to_excel("../outputs/loss_by_category_high_discount.xlsx")
loss_by_subcategory.to_excel("../outputs/loss_by_subcategory_high_discount.xlsx")
loss_by_region.to_excel("../outputs/loss_by_region_high_discount.xlsx")

# ======================
# Visualisations
# ======================

plt.figure()
loss_by_subcategory.head(10).plot(kind="bar", title="Top 10 Loss-Making Sub-Categories (Discount ≥ 30%)")
plt.ylabel("Total Loss")
plt.tight_layout()
plt.savefig("../charts/loss_by_subcategory_high_discount.png")
plt.close()

plt.figure()
loss_by_region.plot(kind="bar", title="Loss by Region (Discount ≥ 30%)")
plt.ylabel("Total Loss")
plt.tight_layout()
plt.savefig("../charts/loss_by_region_high_discount.png")
plt.close()

print("Analysis complete. Loss driver outputs saved.")

# ======================
# REGIONAL PROFITABILITY VS VOLUME
# ======================

# Aggregate by region
region_summary = df.groupby("Region").agg(
    total_sales=("Sales", "sum"),
    total_profit=("Profit", "sum"),
    avg_discount=("Discount", "mean"),
    order_count=("Profit", "count")
).reset_index()

# Calculate profit margin per region
region_summary["profit_margin"] = region_summary["total_profit"] / region_summary["total_sales"]

print("\nRegional summary:")
print(region_summary)

# High-discount losses per region (discount >= 0.3)
high_discount_losses_region = df[df["Discount"] >= 0.3].groupby("Region").agg(
    total_high_discount_loss=("Profit", "sum")
).reset_index()

# Merge with region_summary
region_summary = region_summary.merge(high_discount_losses_region, on="Region", how="left")

# Fill regions without high discount losses with 0
region_summary["total_high_discount_loss"] = region_summary["total_high_discount_loss"].fillna(0)

# Save to Excel
region_summary.to_excel("../outputs/region_profitability.xlsx", index=False)

print("\nRegional profitability summary saved.")

# ======================
# Visualisations: Total Sales vs Total Profit
# ======================

plt.figure(figsize=(8,6))
plt.bar(region_summary["Region"], region_summary["total_sales"], alpha=0.6, label="Total Sales")
plt.bar(region_summary["Region"], region_summary["total_profit"], alpha=0.8, label="Total Profit")
plt.title("Total Sales vs Total Profit by Region")
plt.ylabel("USD")
plt.legend()
plt.tight_layout()
plt.savefig("../charts/total_sales_vs_total_profit.png")
plt.close()

# Profit Margin Bar Chart
plt.figure(figsize=(8,6))
plt.bar(region_summary["Region"], region_summary["profit_margin"], color='skyblue')
plt.title("Profit Margin by Region")
plt.ylabel("Profit Margin")
plt.tight_layout()
plt.savefig("../charts/profit_margin_by_region.png")
plt.close()

print("Regional visuals saved.")