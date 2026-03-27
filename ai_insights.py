from expense_manager import load_data

def analyze_expenses():
    data = load_data()
    
    if not data:
        print("No data to analyze.")
        return

    category_totals = {}

    for exp in data:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\n📊 AI Insights:")

    # Highest spending category
    max_cat = max(category_totals, key=category_totals.get)
    print(f"🔴 Highest spending category: {max_cat} (₹{category_totals[max_cat]})")

    # Suggestion
    if category_totals[max_cat] > 2000:
        print(f"⚠️ You are spending too much on {max_cat}. Try to reduce it.")
    else:
        print("✅ Your spending is under control!")

    # Category breakdown
    print("\n📂 Category-wise Spending:")
    for cat, amt in category_totals.items():
        print(f"{cat}: ₹{amt}")