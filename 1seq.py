num_elements = int(input("Введите количество элементов: "))

numbers = []

for i in range(1, num_elements + 1):
    element = int(input(f"Введите {i} элемент: "))
    numbers.append(element)

numbers.sort()

print("Вывод:", numbers)