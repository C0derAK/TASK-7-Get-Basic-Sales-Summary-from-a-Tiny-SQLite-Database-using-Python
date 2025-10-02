# Task 7: Basic Sales Summary using SQLite + Python

## Objective
Use SQL inside Python to pull simple sales info (total quantity, revenue) and display results with print and a simple bar chart.

## Tools
- Python (sqlite3, pandas, matplotlib)
- SQLite (built-in, no extra setup)

## Steps Done
1. Created a tiny SQLite database `sales_data.db` with one `sales` table.
2. Inserted some sample sales records (Apples, Bananas, Oranges).
3. Ran SQL query to calculate:
   - Total quantity sold per product
   - Total revenue (quantity × price)
4. Loaded results into pandas DataFrame.
5. Printed results in console.
6. Plotted revenue by product as bar chart (`sales_chart.png`).

## How to Run
```bash
python sales_summary.py
