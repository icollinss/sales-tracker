import csv
import argparse
from datetime import datetime

FILE="sales.csv"

# Ensure sales.csv exists with headers
def initialize_file():
    try:
        with open(FILE, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'item', 'amount'])
    except FileExistsError:
        pass
# Add a new sale entry
def add_sale(amount):
    today = datetime.now().strftime("%Y-%m-%d")
    with open(FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([today, 'sale', amount])
    print(f"Added sale of amount: {amount}, on date: {today}")
# View total sales
def total_sales():
    total = 0
    try:
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total += float(row["amount"])
    except FileNotFoundError:
        print("No sales recorded yet.")
        return

    print(f"Total sales: {total}")

# List sales
def list_sales():
    try:
        with open(FILE, "r") as f:
            reader = csv.DictReader(f)
            print("Date         | Amount")
            print("----------------------")
            for row in reader:
                print(f"{row['date']} | {row['amount']}")
    except FileNotFoundError:
        print("No sales data yet.")

# CLI Setup
parser = argparse.ArgumentParser(description="Sales Tracker CLI Tool")
parser.add_argument("action", choices=["add", "total", "list"], help="Action to perform")
parser.add_argument("--amount", type=float, help="Amount of sale for 'add' action")

args = parser.parse_args()

initialize_file()

if args.action == "add":
    if not args.amount:
        print("Error: You must provide --amount when using 'add'")
    else:
        add_sale(args.amount)

elif args.action == "total":
    total_sales()

elif args.action == "list":
    list_sales()