import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 📦 Step 1: Create the sales data
sales_data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Bread_Sold': [20, 25, 22, 30, 35, 40, 45],
    'Milk_Sold': [30, 28, 35, 25, 40, 38, 42],
    'Eggs_Sold': [50, 45, 48, 60, 55, 65, 70]
}

# Create DataFrame
df = pd.DataFrame(sales_data)
print("🏪 Mini Store Sales Data:")
print(df)
print("\n" + "="*50 + "\n")

# 🧮 Task 1: Total Sales Calculations
print("📊 TASK 1: TOTAL SALES ANALYSIS")
print("-" * 30)

# Total items sold per day
df['Total_Daily_Sales'] = df['Bread_Sold'] + df['Milk_Sold'] + df['Eggs_Sold']
print("Daily totals:")
for i, row in df.iterrows():
    print(f"{row['Day']}: {row['Total_Daily_Sales']} items")

print(f"\nTotal per product:")
bread_total = df['Bread_Sold'].sum()
milk_total = df['Milk_Sold'].sum()
eggs_total = df['Eggs_Sold'].sum()
print(f"🍞 Bread: {bread_total} units")
print(f"🥛 Milk: {milk_total} units")
print(f"🥚 Eggs: {eggs_total} units")
print(f"📈 Grand Total: {bread_total + milk_total + eggs_total} items")

print("\n" + "="*50 + "\n")

# 📈 Task 2: Trend Analysis
print("📈 TASK 2: TREND ANALYSIS")
print("-" * 25)

# Calculate day-to-day changes for each product
def analyze_trend(series, product_name):
    changes = series.diff().dropna()  # Calculate differences between consecutive days
    increases = (changes > 0).sum()
    decreases = (changes < 0).sum()
    no_change = (changes == 0).sum()
    
    print(f"\n{product_name} trend:")
    print(f"  Days with increases: {increases}")
    print(f"  Days with decreases: {decreases}")
    print(f"  Days with no change: {no_change}")
    print(f"  Average daily change: {changes.mean():.1f}")
    
    return increases, changes.mean()

bread_inc, bread_avg = analyze_trend(df['Bread_Sold'], "🍞 Bread")
milk_inc, milk_avg = analyze_trend(df['Milk_Sold'], "🥛 Milk")
eggs_inc, eggs_avg = analyze_trend(df['Eggs_Sold'], "🥚 Eggs")

# Find most consistently increasing product
trends = {'Bread': (bread_inc, bread_avg), 'Milk': (milk_inc, milk_avg), 'Eggs': (eggs_inc, eggs_avg)}
most_consistent = max(trends.keys(), key=lambda x: (trends[x][0], trends[x][1]))
print(f"\n🏆 Most consistently increasing: {most_consistent}")

print("\n" + "="*50 + "\n")

# 📊 Task 3: Visualization
print("📊 TASK 3: CREATING VISUALIZATIONS")
print("-" * 32)

# Create the line chart
plt.figure(figsize=(12, 8))

# Plot each product
days_numeric = range(len(df['Day']))
plt.plot(days_numeric, df['Bread_Sold'], marker='o', linewidth=2, label='🍞 Bread', color='goldenrod')
plt.plot(days_numeric, df['Milk_Sold'], marker='s', linewidth=2, label='🥛 Milk', color='lightblue')
plt.plot(days_numeric, df['Eggs_Sold'], marker='^', linewidth=2, label='🥚 Eggs', color='orange')

# Customize the chart
plt.title('📈 Weekly Sales Trends - Mini Store', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Units Sold', fontsize=12)
plt.xticks(days_numeric, df['Day'], rotation=45)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Add some styling
plt.gca().set_facecolor('#f8f9fa')
plt.gcf().patch.set_facecolor('white')

plt.show()

print("Chart displayed! 📊✨")

print("\n" + "="*50 + "\n")

# 🎯 Task 4: Bonus - Average Analysis
print("🎯 BONUS TASK: AVERAGE ANALYSIS")
print("-" * 28)

# Calculate averages
avg_bread = df['Bread_Sold'].mean()
avg_milk = df['Milk_Sold'].mean()
avg_eggs = df['Eggs_Sold'].mean()
avg_daily_total = df['Total_Daily_Sales'].mean()

print("📊 Average daily sales:")
print(f"🍞 Bread: {avg_bread:.1f} units")
print(f"🥛 Milk: {avg_milk:.1f} units")
print(f"🥚 Eggs: {avg_eggs:.1f} units")
print(f"📈 Total: {avg_daily_total:.1f} items")

print("\n🚨 Days exceeding average total sales:")
above_avg_days = df[df['Total_Daily_Sales'] > avg_daily_total]
for i, row in above_avg_days.iterrows():
    excess = row['Total_Daily_Sales'] - avg_daily_total
    print(f"  {row['Day']}: {row['Total_Daily_Sales']} items (+{excess:.1f} above average)")

if len(above_avg_days) == 0:
    print("  No days exceeded the average!")

print("\n" + "="*50 + "\n")

# 📋 Summary Report
print("📋 EXECUTIVE SUMMARY")
print("-" * 18)
print(f"🏪 Store Performance Overview:")
print(f"  • Total items sold this week: {bread_total + milk_total + eggs_total}")
print(f"  • Best selling product: {'🥚 Eggs' if eggs_total == max(bread_total, milk_total, eggs_total) else '🥛 Milk' if milk_total == max(bread_total, milk_total, eggs_total) else '🍞 Bread'}")
print(f"  • Most consistent growth: {most_consistent}")
print(f"  • Peak sales day: {df.loc[df['Total_Daily_Sales'].idxmax(), 'Day']}")
print(f"  • Days above average: {len(above_avg_days)}/7")

print("\n🎉 Analysis complete! Great job exploring the data! 🎉")