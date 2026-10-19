
def deposit(balance, amount):
    if amount <= 0:
        return "Enter a valid amount"

    new_balance = balance + amount
    return new_balance


print(deposit(5000, 2000))
print(deposit(1000, 500))
print(deposit(3000, 0))
