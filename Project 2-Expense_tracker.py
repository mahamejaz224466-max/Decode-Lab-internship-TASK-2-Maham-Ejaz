# Project 2: The Expense Tracker
# Let the user enter expense amounts one at a time. The program keeps a running total (the "accumulator pattern") and displays the
# Total Spent once the user is done.


def get_expense_input():
  
    raw = input("Enter an expense amount (or 'done' to finish): ").strip()

    if raw.lower() in ("done", "quit", "exit"):
        return None  
  
    try:
        amount = float(raw)
        if amount < 0:
            print("Expenses can not be negative. Try again.\n")
            return -1
        return amount
    except ValueError:
        print(f"'{raw}' isn't a valid number. Try again.\n")
        return -1


def track_expenses():    
    total = 0         
    expenses = []       

    print("-" * 40)
    print(" YOUR EXPENSE TRACKER")
    print("-" * 40)
    print("Enter each expense one at a time. Type 'done' when finished.\n")

    while True:
        amount = get_expense_input()

        if amount is None:          
            break
        if amount == -1:            
            continue

        total += amount              
        expenses.append(amount)
        print(f"Added ${amount:.2f}. Running total: ${total:.2f}\n")

    return total, expenses


def show_report(total, expenses):
    print("\nEXPENSE REPORT:")
    if not expenses:
        print("No expenses were recorded.")
    else:
        for index, amount in enumerate(expenses, start=1):
            print(f"{index}. ${amount:.2f}")
        print("-" * 24)
        print(f"Transactions: {len(expenses)}")
        print(f"FINAL TOTAL SPENT: ${total:.2f}")

def main():
    total, expenses = track_expenses()
    show_report(total, expenses)


if __name__ == "__main__":
    main()
