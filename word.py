
def count_words(sentence):
    words = sentence.split()
    return len(words)


def show_result(sentence):
    total = count_words(sentence)
    return "Word count: " + str(total)


print(show_result("I am learning Python"))
print(show_result("Functions make code reusable"))
print(show_result("Python is fun"))
