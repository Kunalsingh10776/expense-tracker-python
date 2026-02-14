# expense-tracker-python
This is a solid Python script! It’s clean, functional, and uses openpyxl effectively to bridge the gap between terminal input and Excel reporting.

To make this "GitHub ready," your README should explain what it is, how to set it up (especially the library dependency), and how to use it.

📊 Personal Expense Tracker (Python & Excel)
A lightweight terminal-based application that tracks your daily expenses and automatically generates structured reports and bar charts in an Excel workbook.

✨ Features
Data Persistence: Saves all entries to expenses.xlsx automatically.

Categorization: Group expenses by category (Food, Rent, Travel, etc.).

Summary Reports: View total spending and monthly breakdowns within the terminal.

Excel Visualization: Generates a dedicated "Charts" sheet in Excel with a Bar Chart of your spending.

Smart Sheets: Automatically creates "Expenses", "Summary", and "Charts" sheets if they don't exist.

🚀 Getting Started
Prerequisites
Python 3.x

openpyxl library

🛠️ How it Works
The script interacts with the Excel file in three main ways:

Expenses Sheet: Acts as a raw database for every transaction.

Summary Sheet: Uses Python dictionaries to aggregate totals per category.

Charts Sheet: Uses the openpyxl.chart module to draw a visual representation of the summary data.

📝 License
This project is open-source and available under the MIT License.
