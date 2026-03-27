import json
import os

FILE = "data.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(category, amount):
    data = load_data()
    data.append({"category": category, "amount": amount})
    save_data(data)

def view_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return
    for i, exp in enumerate(data, 1):
        print(f"{i}. {exp['category']} - ₹{exp['amount']}")

def get_total():
    data = load_data()
    return sum(exp["amount"] for exp in data)