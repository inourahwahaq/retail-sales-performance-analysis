import pandas as pd

# Load dataset
df = pd.read_csv("cleaned_superstore.csv")

# The same order ID is used by different customers on different dates,
# so one order is one order ID for one customer
orders = df[["Order.ID", "Customer.Name"]].drop_duplicates().shape[0]

# Business KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Total Sales:", total_sales)
print("Total Profit:", round(total_profit, 2))
print("Profit Margin %:", round(total_profit / total_sales * 100, 2))
print("Total Orders:", orders)
print("Total Customers:", df["Customer.Name"].nunique())
print("Average Order Value:", round(total_sales / orders, 2))

# Sales and profit by year
print("\nSales and Profit by Year")
print(df.groupby("Year")[["Sales", "Profit"]].sum().round(0))

# Sales and profit by category
print("\nSales and Profit by Category")
print(df.groupby("Category")[["Sales", "Profit"]].sum().round(0).sort_values("Sales", ascending=False))

# Region names repeat across markets, so regions are read inside their market
print("\nProfit by Market and Region")
print(df.groupby(["Market", "Region"])["Profit"].sum().round(0).sort_values(ascending=False))

# Top 10 products by sales
print("\nTop 10 Products by Sales")
print(df.groupby("Product.Name")["Sales"].sum().sort_values(ascending=False).head(10))

# Profit margin by discount level
df["Discount Level"] = pd.cut(df["Discount"], bins=[-0.01, 0, 0.2, 0.4, 1], labels=["No discount", "1-20%", "21-40%", "Over 40%"])
discount = df.groupby("Discount Level", observed=True)[["Sales", "Profit"]].sum()
discount["Margin %"] = (discount["Profit"] / discount["Sales"] * 100).round(1)

print("\nProfit Margin by Discount Level")
print(discount.round(0))
