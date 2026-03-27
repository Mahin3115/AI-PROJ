# AI Student Expense Tracker (CLI)

## Project Overview

The AI Student Expense Tracker is a command-line based application designed to help students efficiently track, manage, and analyze their daily expenses. It provides intelligent insights into spending habits using basic AI logic, enabling users to make better financial decisions.

---

## Features

* Add new expenses with category and amount
* View all recorded expenses
* Calculate total spending
* AI-based insights on spending patterns
* Alerts for excessive spending
* Data stored locally using JSON

---

## AI Functionality

The application uses simple AI techniques such as:

* Pattern recognition (category-wise spending analysis)
* Decision-making (detects highest expense category)
* Smart suggestions (alerts for overspending)

---

## Technologies Used

* Python 3.x
* JSON (for data storage)

---

## Project Structure

```id="mmwg4k"
expense_tracker/
│── main.py              # CLI interface
│── expense_manager.py  # Core expense logic
│── ai_insights.py      # AI analysis module
│── data.json           # Data storage file
│── README.md           # Project documentation
```

---

## Installation & Setup

### 1. Clone the Repository

```id="xhphot"
git clone https://github.com/Mahin3115/AI-PROJ/
```

### 2. Navigate to Project Folder

```id="parccu"
cd expense-tracker
```

### 3. Run the Application

```id="07hurz"
python main.py
```

---

## Usage Guide

Once the program starts, you will see a menu:

```id="fhx0pt"
===== Student Expense Tracker =====
1. Add Expense
2. View Expenses
3. Total Spending
4. AI Insights
5. Exit
```

### Example Workflow:

1. Choose option 1 to add expense
2. Enter category (e.g., Food, Travel)
3. Enter amount
4. View insights using option 4

---

## Example Output

```id="unw0dc"
AI Insights:
Highest spending category: Food (₹2500)
You are spending too much on Food. Try to reduce it.
```

---

## Data Storage

* All expenses are stored in data.json
* Data is saved automatically after each entry
* Format:

```id="re4ksc"
[
  {"category": "Food", "amount": 200},
  {"category": "Travel", "amount": 100}
]
```

---

## Error Handling

* Handles invalid menu choices
* Prevents crashes on empty data
* Validates user input

---

## Objectives

* Help students track daily expenses
* Promote financial awareness
* Provide intelligent spending insights
* Demonstrate AI concepts in a CLI application

---

## Real-World Application

* Personal finance management
* Budget tracking tools
* Expense monitoring systems

---

## Future Enhancements

* Monthly budget tracking
* Graph visualization
* Machine learning-based expense prediction
* User authentication system

---

## Author

* Name: Your Name
* Course: Fundamentals of AI and ML

---

## License

This project is for educational purposes.
