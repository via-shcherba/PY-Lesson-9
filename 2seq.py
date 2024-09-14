
try:
    
    user_input = input("Введите элементы списка (через запятую, точку с запятой или слэш): ")
    
    if ',' in user_input:
        elements = user_input.split(',')
    elif ';' in user_input:
        elements = user_input.split(';')
    elif '/' in user_input:
        elements = user_input.split('/')
    else:
        print("Неверный формат ввода.")     
    
    # Create a dictionary to count occurrences of each number
    count_dict = {}
    for num in elements:
        num = num.strip()  # Remove any extra spaces
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Filter out only unique elements (those that appear exactly once)
    unique_elements = [num for num, count in count_dict.items() if count == 1]
       
    print("Результат:", ", ".join(map(str, unique_elements)))
except:
    print("Неверный формат ввода.")