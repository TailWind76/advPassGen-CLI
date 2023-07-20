import random

def generate_password(length=16):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?\"'"

    print("Будут ли использованы специальные символы в пароле? (да/нет)")
    use_special = input().lower() == "да"

    print("Будут ли использованы цифры в пароле? (да/нет)")
    use_digits = input().lower() == "да"

    print("Будут ли использованы заглавные буквы в пароле? (да/нет)")
    use_uppercase = input().lower() == "да"

    allowed_characters = lowercase_letters
    if use_special:
        allowed_characters += special_characters
    if use_digits:
        allowed_characters += digits
    if use_uppercase:
        allowed_characters += uppercase_letters

    if not allowed_characters:
        raise ValueError("Не выбраны допустимые символы для пароля")

    password = [random.choice(allowed_characters) for _ in range(length)]
    random.shuffle(password)
    password = ''.join(password)

    return password

if __name__ == "__main__":
    print("Введите длину пароля (по умолчанию 16):")
    try:
        password_length = int(input())
        generated_password = generate_password(password_length)
    except ValueError:
        generated_password = generate_password()

    print("Сгенерированный пароль:", generated_password)
