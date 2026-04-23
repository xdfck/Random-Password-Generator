import random
import string

def generate_password(length, use_digits, use_letters, use_special):
    if not (use_digits or use_letters or use_special):
        raise ValueError("Выберите хотя бы один тип символов.")
    if length < 1:
        raise ValueError("Длина пароля должна быть больше 0.")

    chars = ''
    if use_digits:
        chars += string.digits
    if use_letters:
        chars += string.ascii_letters
    if use_special:
        chars += string.punctuation

    return ''.join(random.choices(chars, k=length))
