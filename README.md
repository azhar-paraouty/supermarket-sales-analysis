# Supermarket Sales & Profit Analysis

## 🎯 Objective
To analyse sales and profit performance across regions, categories, and discount levels in order to identify profitable segments, loss-making areas, and pricing behaviours that impact business performance.

## 📊 Dataset
- Source: Kaggle – Sample Superstore Dataset
- Records: ~10,000 transactions
- Format: CSV

## 🛠 Tools Used
- Python (pandas, matplotlib)
- Excel (for cleaned outputs)
- VS Code

## A. 🔍 Key Analyses Performed
An initial exploratory analysis was conducted, resulting in three core visualisations:
- Profitability by product category (`profit_by_category.png`)
- Sales performance by region (`sales_by_region.png`)
- Relationship between discount levels and profitability (`discount_vs_profit.png`)

## B. ❓ Key Questions raised
1. **Discount–Profit Relationship**  
   At what discount levels does profitability decline, and is there an optimal discount range that maximises profit?

2. **Furniture Category Investigation**  
   Is the Furniture category inherently low profit-making, or is this driven by specific sub-categories or discount practices?

3. **Regional Profitability vs Volume**  
   Do high-sales regions also generate high profits, or are some regions high-volume but low-margin?

## C. 🔑 Key Insights
- Discounting beyond approximately **30%** consistently leads to negative profitability, suggesting margins cannot sustain aggressive price reductions.  
> Average profit peaks at lower discount levels, while deeper discounts are associated with increasing losses.

- High-discount losses are concentrated in:
  - Furniture → Tables  
  - Office Supplies → Binders  
  - Technology → Machines  

- Central and East regions account for the largest portion of high-discount losses.  
> These patterns suggest that certain sub-categories and regions are more sensitive to aggressive discounting.

- **Furniture category analysis:**  
  Losses are primarily driven by high-discount sales of `Tables`, while other sub-categories contribute smaller losses.  
> This indicates that profitability can be improved by managing discounts per sub-category.

- **Regional Profitability vs Volume:**  
  - **West**: Highest total sales and highest profit margin  
  - **East**: High sales, strong profit margin  
  - **Central**: Moderate sales, lower margin (affected by high-discount losses)  
  - **South**: Lowest sales, decent margin  

> Overall, high-sales regions generally generate high profits, but high-discount practices can significantly erode margins in specific regions (e.g., Central).

## 📁 Outputs
- **Cleaned dataset**
  - `supermarket_clean.xlsx`

- **Visualisations**
  - `discount_vs_profit.png`
  - `profit_by_category.png`
  - `sales_by_region.png`
  - `loss_by_subcategory_high_discount.png`
  - `loss_by_region_high_discount.png`
  - `total_sales_vs_total_profit.png`
  - `profit_margin_by_region.png`

- **Analytical summaries**
  - `descriptive_statistics.xlsx`
  - `discount_analysis.xlsx`
  - `loss_by_category_high_discount.xlsx`
  - `loss_by_subcategory_high_discount.xlsx`
  - `loss_by_region_high_discount.xlsx`
  - `region_profitability.xlsx`

## 🏁 Project 1 – Conclusion

This analysis investigated sales and profit performance across regions, product categories, and discount levels. Key findings include:  

- **Discount–Profit Relationship:** Profitability declines sharply at discounts above **30%**, highlighting the importance of strategic discounting.  
- **Furniture Category Investigation:** Losses in Furniture are driven primarily by high-discount sales of `Tables`, rather than the category as a whole (though the other 2 categories are also affected by sub-categories).  
- **Regional Profitability vs Volume:** High-sales regions generally generate high profits, with West and East performing best. However, high-discount sales in Central contribute to lower margins, illustrating the impact of discount practices on regional performance.  

**Skills demonstrated:**  
- Data cleaning and transformation (Excel & Python)  
- Exploratory data analysis (pandas, matplotlib)  
- Business-focused insight generation (identifying loss-making products, regions, and discount thresholds)  
- Reproducible analysis workflow and documentation for professional presentation  

> Overall, this project shows how structured data analysis can uncover actionable insights to improve pricing strategies, optimize regional sales performance, and enhance profitability.