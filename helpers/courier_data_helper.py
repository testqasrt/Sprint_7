import random
import string

# Данные по зарегистированному пользователю
REGISTERED_USER_DATA = dict(
    login='sdfg',
    password='password',
    firstName='first_nffame',
    id=381280
)


def generate_random_register_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload
