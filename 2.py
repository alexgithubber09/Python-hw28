with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Это тестовый файл для домашнего задания по программированию")

with open("test.txt", "r", encoding="utf-8") as file:
    print(file.read())