
def shopping_cart(prices):
    if not prices:
        return 0

    total = 0

    for price in prices:
        if price < 0:
            return "Invalid price"
        total += price

    return total


print(shopping_cart([500, 200, 100]))
print(shopping_cart([1500, 2500, 300]))
print(shopping_cart([]))
