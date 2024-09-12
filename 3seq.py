def get_list_input(prompt):
    user_input = input(prompt)
    if ',' in user_input:
        elements = user_input.split(',')
    elif ';' in user_input:
        elements = user_input.split(';')
    elif '/' in user_input:
        elements = user_input.split('/')
    else:
        elements = user_input.split()
    
    # Convert input to integers and remove extra spaces
    return set(int(x.strip()) for x in elements)
try:
    list1 = get_list_input("Введите элементы 1-го списка: ")
    list2 = get_list_input("Введите элементы 2-го списка: ")

    result_list = list1 - list2

    print("Результат:", ", ".join(map(str, result_list)))
except:
    print("Неверный формат ввода.")