
def check_number(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"


for number in range(1, 6):
    print(number, check_number(number))
