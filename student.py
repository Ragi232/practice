
def get_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def save_result(name, score):
    grade = get_grade(score)

    with open("results.txt", "a") as file:
        file.write(f"{name},{score},{grade}\n")

    print(name, "got grade", grade)


def view_results():
    try:
        with open("results.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No results saved yet.")


save_result("Ada", 85)
save_result("John", 56)
view_results()
