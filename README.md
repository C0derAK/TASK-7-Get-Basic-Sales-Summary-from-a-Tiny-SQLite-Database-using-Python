# Task 7: Basic Sales Summary using SQLite + Python

## 📌 Objective
Use SQL inside Python to pull simple sales info (like total quantity sold, total revenue), and display results with print statements and a simple bar chart.

---

## 🛠 Tools Used
- **Python** (`sqlite3`, `pandas`, `matplotlib`)
- **SQLite** (lightweight database, built into Python)
- **Jupyter Notebook** (`sales_summary.ipynb`)

---

## 📂 Files in Repo
- `sales_summary.ipynb` → Jupyter Notebook with full step-by-step solution  
- `sales_data.db` → Tiny SQLite database file with a single sales table  
- `sales_chart.png` → Bar chart showing revenue by product  
- `README.md` → Project explanation and instructions  

---

## 🚀 Steps Done
1. Connected Python to SQLite database (`sales_data.db`).
2. Created a `sales` table with columns: `product`, `quantity`, `price`.
3. Inserted sample sales data (Apples, Bananas, Oranges).
4. Ran SQL query to calculate:
   - **Total quantity sold per product**
   - **Total revenue (quantity × price)**
5. Loaded SQL query result into a pandas DataFrame.
6. Printed results in console.
7. Plotted a **bar chart of revenue by product** (`sales_chart.png`).

---

## ▶️ How to Run
1. Clone/download this repo  
2. Open the notebook in **Jupyter Notebook / Jupyter Lab / VS Code**  
3. Run all cells step by step  
   ```bash
   jupyter notebook sales_summary.ipynb

