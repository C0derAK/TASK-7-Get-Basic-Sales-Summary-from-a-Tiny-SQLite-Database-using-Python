import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect("sales_data.db")

# SQL query to summarize sales by product
query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"

# Load into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close connection
conn.close()

# Print results
print("Sales Summary:")
print(df)

# Plot bar chart for revenue by product
df.plot(kind="bar", x="product", y="revenue", legend=False, title="Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
