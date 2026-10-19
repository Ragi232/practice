
def withdraw(balance, amount):
    if amount <= 0:
        return "Enter a valid amount"
    elif amount > balance:
        return "Insufficient balance"
    else:
        balance = balance - amount
        return balance


print(withdraw(5000, 2000))
print(withdraw(1000, 1500))
print(withdraw(3000, 0))
