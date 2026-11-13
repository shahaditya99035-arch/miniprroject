expenses = []
total = 0

print("Expense Tracker - type 'done' to stop")

while True:
    item = input("Enter item name (or done): ")
    if item.lower() == "done":
        break
    amount = float(input(f"Enter price of {item}: "))
    expenses.append((item, amount))
    total += amount

print("\n--- Your Expenses ---")
for item, amount in expenses:
    print(f"{item} : Rs. {amount}")

print(f"Total Expense: Rs. {total}")