def calculate_due(total_amount, amount_paid):
    if amount_paid > total_amount:
        print("You have overpaid. Please check the amount.")
        return 0
    else:
        return total_amount - amount_paid


total = float(input("Enter the total bill amount: ₹ "))
paid = float(input("Enter the amount paid: ₹ "))


due = calculate_due(total, paid)


if due > 0:
    print(f"Amount still due: ₹ {due:.2f}")
elif due == 0:
    print("Bill fully paid. No due amount.")