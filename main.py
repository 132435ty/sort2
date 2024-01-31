strings = ["При ве т", "Pyt  hon", "Кодир овани е"]

def remove(word):
    return word.replace(" ", "")

modified_strings = list(map(remove, strings))

for string in modified_strings:
    print(string)
