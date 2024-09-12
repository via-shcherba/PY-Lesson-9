
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
        
    elements = set(int(x.strip()) for x in elements)  # Remove whitespace and convert to integers
       
    print("Результат:", ", ".join(map(str, elements)))
except:
    print("Неверный формат ввода.")