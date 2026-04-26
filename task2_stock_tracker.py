"""
CodeAlpha Internship - Task 2: Stock Portfolio Tracker
Author: CodeAlpha Intern
Description: A stock tracker that calculates total investment based on manually defined stock prices.
"""

import csv
import os
from datetime import datetime

# Hardcoded stock prices (in USD)
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 140.00,
    "MSFT": 375.00,
    "AMZN": 185.00,
    "META": 500.00,
    "NFLX": 620.00,
    "NVDA": 880.00,
}


def display_available_stocks():
    """Display all available stocks and their prices."""
    print("\n  📊 Available Stocks:")
    print("  " + "-" * 30)
    print(f"  {'Symbol':<10} {'Price (USD)':>12}")
    print("  " + "-" * 30)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>11.2f}")
    print("  " + "-" * 30)


def get_portfolio():
    """Get stock portfolio from user input."""
    portfolio = {}

    print("\n  Enter your stock holdings (type 'done' when finished):")
    print("  Tip: Stock symbols must be from the available list above.\n")

    while True:
        symbol = input("  Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  ⚠  '{symbol}' not found. Please choose from the available list.\n")
            continue

        try:
            qty = int(input(f"  Quantity for {symbol}: ").strip())
            if qty <= 0:
                print("  ⚠  Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  ⚠  Invalid quantity. Please enter a whole number.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
        else:
            portfolio[symbol] = qty

        print(f"  ✅ Added {qty} shares of {symbol} @ ${STOCK_PRICES[symbol]:.2f}\n")

    return portfolio


def display_portfolio(portfolio):
    """Display portfolio summary and calculate total investment."""
    if not portfolio:
        print("\n  ⚠  Your portfolio is empty.")
        return 0

    print("\n" + "=" * 52)
    print("          📈 YOUR STOCK PORTFOLIO SUMMARY")
    print("=" * 52)
    print(f"  {'Symbol':<8} {'Qty':>6} {'Price':>12} {'Value':>14}")
    print("  " + "-" * 46)

    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        print(f"  {symbol:<8} {qty:>6} ${price:>11.2f} ${value:>13.2f}")

    print("  " + "-" * 46)
    print(f"  {'TOTAL INVESTMENT':>28} ${total:>13.2f}")
    print("=" * 52)
    return total


def save_portfolio(portfolio, total):
    """Save portfolio to both .txt and .csv files."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save as .txt
    txt_filename = f"portfolio_{date_str}.txt"
    with open(txt_filename, "w") as f:
        f.write("=" * 52 + "\n")
        f.write("      STOCK PORTFOLIO REPORT — CodeAlpha\n")
        f.write("=" * 52 + "\n")
        f.write(f"  Generated on: {timestamp}\n\n")
        f.write(f"  {'Symbol':<8} {'Qty':>6} {'Price':>12} {'Value':>14}\n")
        f.write("  " + "-" * 46 + "\n")
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            f.write(f"  {symbol:<8} {qty:>6} ${price:>11.2f} ${value:>13.2f}\n")
        f.write("  " + "-" * 46 + "\n")
        f.write(f"  {'TOTAL INVESTMENT':>28} ${total:>13.2f}\n")
        f.write("=" * 52 + "\n")

    # Save as .csv
    csv_filename = f"portfolio_{date_str}.csv"
    with open(csv_filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Quantity", "Price (USD)", "Total Value (USD)", "Timestamp"])
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            value = price * qty
            writer.writerow([symbol, qty, f"{price:.2f}", f"{value:.2f}", timestamp])
        writer.writerow(["TOTAL", "", "", f"{total:.2f}", timestamp])

    print(f"\n  ✅ Portfolio saved to '{txt_filename}' and '{csv_filename}'")


def stock_tracker():
    """Main stock portfolio tracker function."""
    print("=" * 52)
    print("   📊 WELCOME TO STOCK PORTFOLIO TRACKER")
    print("        CodeAlpha Python Internship")
    print("=" * 52)

    display_available_stocks()
    portfolio = get_portfolio()
    total = display_portfolio(portfolio)

    if portfolio:
        save = input("\n  💾 Save portfolio to file? (yes/no): ").strip().lower()
        if save in ("yes", "y"):
            save_portfolio(portfolio, total)

    print("\n  Thank you for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    stock_tracker()
