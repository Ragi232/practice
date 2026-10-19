
def add_expense(name, amount):
    with open("expenses.txt", "a") as file:
        file.write(name + "," + str(amount) + "\n")
    print("Expense saved!")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                print(name, "-", amount, "naira")
    except FileNotFoundError:
        print("No expenses saved yet.")


def total_expenses():
    total = 0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                total += float(amount)
    except FileNotFoundError:
        return 0

    return total


add_expense("Food", 2000)
add_expense("Transport", 1000)
view_expenses()
print("Total spent:", total_expenses())
