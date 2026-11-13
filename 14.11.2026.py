def register_user():
    while True:
        login = input("Введите логин: ")
        if len(login) >= 5 and login[0].isalpha() and login.isalnum():
            break
        else:
            print("Ошибка: логин должен содержать не менее 5 символов, начинаться с буквы и состоять только из букв и цифр.")

    valid_domains = ('ru', 'su', 'рф')
    while True:
        email = input("Введите email: ")
        
        if email.startswith('.') or email.endswith('.') or email.startswith('@') or email.endswith('@'):
            print("Ошибка: email не должен начинаться или заканчиваться точкой или символом @.")
            continue
            
        if '@' not in email:
            print("Ошибка: адрес должен содержать символ @.")
            continue
            
        parts = email.split('@')
        if len(parts) != 2 or '.' not in parts[1]:
            print("Ошибка: адрес должен содержать точку после @.")
            continue
            
        domain = email.split('.')[-1]
        if domain not in valid_domains:
            print(f"Ошибка: допустимые домены – {', '.join(valid_domains)}.")
            continue
            
        break

    special_chars = "!@#$%^&*_"
    while True:
        password = input("Введите пароль: ")
        
        has_length = len(password) >= 8
        has_digit = False
        has_upper = False
        has_lower = False
        has_special = False
        
        for char in password:
            if char.isdigit():
                has_digit = True
            elif char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char in special_chars:
                has_special = True
                
        if not has_length:
            print("Ошибка: пароль должен быть длиной не менее 8 символов.")
        elif not has_digit:
            print("Ошибка: пароль должен содержать хотя бы одну цифру.")
        elif not has_upper:
            print("Ошибка: пароль должен содержать хотя бы одну заглавную букву.")
        elif not has_lower:
            print("Ошибка: пароль должен содержать хотя бы одну строчную букву.")
        elif not has_special:
            print(f"Ошибка: пароль должен содержать хотя бы один специальный символ из {special_chars}.")
        else:
            break

    print("Регистрация успешна!")

if __name__ == "__main__":
    register_user()
