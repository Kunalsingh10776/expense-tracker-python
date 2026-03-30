💸 Expense Tracker – Excel Based
A command-line personal expense tracker built with Python that stores all data in an Excel workbook (expenses.xlsx). Add expenses, view summaries, and generate bar charts — all from the terminal.

📋 Features
#FeatureDescription1Add ExpenseRecord date, category, item, and amount2View ExpensesList all saved expenses3Total ExpenseShow the sum of all expenses4Category SummaryGroup and total expenses by category5Monthly SummaryGroup and total expenses by month6Excel ChartGenerate a bar chart inside the Excel file

🛠️ Requirements

Python 3.x
openpyxl

Install the dependency with:
bashpip install openpyxl

🚀 Getting Started
bashpython main.py
On the first run, an expenses.xlsx file is automatically created in the same directory. On subsequent runs, the existing file is loaded and updated.

🖥️ Usage
After running the script, you'll see an interactive menu:
===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Total Expense
4. Category Summary
5. Monthly Summary
6. Create Excel Chart
7. Exit
Enter the number for the option you want and follow the prompts.
Adding an Expense
Enter date (DD/MM/YYYY): 28/03/2026
Category: Food
Description: Lunch at canteen
Amount: 85
✅ Expense added & saved to Excel

📁 Excel File Structure
The generated expenses.xlsx contains three sheets:
SheetContentsExpensesAll raw expense records (Date, Month, Category, Item, Amount)SummaryCategory-wise totals (updated when option 4 or 6 is selected)ChartsBar chart visualizing spending by category

📂 Project Structure
expense-tracker/
│
├── main.py          # Main application file
├── expenses.xlsx    # Auto-generated data file (created on first run)
└── README.md        # Project documentation

⚠️ Notes

Date must be entered in DD/MM/YYYY format.
The expenses.xlsx file is created in the same directory as main.py.
The chart is embedded inside the Excel file under the Charts sheet — open the file in Excel or LibreOffice Calc to view it.
The Summary sheet is automatically refreshed whenever option 4 (Category Summary) or 6 (Create Excel Chart) is selected.


📌 Example Output
📋 ALL EXPENSES
1. 28/03/2026 | Food | Lunch at canteen | ₹85.0
2. 28/03/2026 | Transport | Bus fare | ₹20.0

💰 TOTAL EXPENSE: ₹105.0

📅 MONTHLY SUMMARY
03-2026: ₹105.0
