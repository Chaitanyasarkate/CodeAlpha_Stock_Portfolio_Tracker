Stock Portfolio Tracker

A simple Python program to track stock investments.
Users can input stock symbols and quantities, and the program calculates the total investment value. Optionally, the results can be saved to a .txt or .csv file.

Features

Hardcoded stock prices for popular stocks like AAPL, TSLA, MSFT, GOOG, AMZN.

Accepts user input for stock symbols and quantities.

Calculates and displays total portfolio investment value.

Option to save the portfolio report as:

Text file (.txt)

CSV file (.csv)

Simple and interactive command-line interface.

Getting Started
Prerequisites

Python 3.x installed on your machine.
Download Python: https://www.python.org/downloads/

Installation

Clone the repository

git clone https://github.com/Chaitanyasarkate/stock-portfolio-tracker.git


Navigate to the project folder

cd stock-portfolio-tracker


Run the program

python stock_portfolio_tracker.py

How to Use

The program displays available stocks and their prices.

Enter stock symbols one by one and the quantity you own.

Type done when finished.

The program calculates the total investment value and displays a summary.

You can choose to save the report as .txt or .csv.

Example
Enter stock symbol: AAPL
Enter quantity for AAPL: 5
Enter stock symbol: TSLA
Enter quantity for TSLA: 2
Enter stock symbol: done

TOTAL INVESTMENT VALUE: $1400
Do you want to save this report? (y/n): y
Choose file format (1 or 2): 2
✅ Report saved as 'portfolio_report.csv'

Project Structure
stock-portfolio-tracker/

│

├── stock_portfolio_tracker.py   # Main Python script

├── README.md                    # Project documentation

└── .gitignore                   # Optional, to ignore unnecessary files

Technologies Used

Python 3.x

Built-in modules: csv, input/output, file handling

Author

Chaitanya sarkate:

GitHub: [https://github.com/your-username](https://github.com/Chaitanyasarkate/CodeAlpha_Stock_Portfolio_Tracker)

License

This project is open-source and free to use.
