calls = 0  #  Счётчик вызова функций


def count_calls() -> None:
    """Функция при каждом выполнении
    увеличивает глобальную переменную счетчика вызова функций на +1"""
    global calls
    calls += 1
    return


def string_info(string):
    """Функция принимает строку, возвращает кортеж с её длиной, в верхнем и нижнем регистре"""
    string_length = len(string)
    string_upper = string.upper()
    string_lowercase = string.lower()
    result = (string_length, string_upper, string_lowercase)
    count_calls()  # Счётчик
    return result


def is_contains(string: str, list_to_search: []) -> bool:
    """Функция ищет строку в подстроке без учёта регистра"""
    string = string.lower()
    count_calls()  # Счётчик
    for el in list_to_search:
        if el.lower() == string:
            print("YES", string, el)
            return True
    print("No matches")
    return False


print(string_info("test"))
print(string_info("произвольное кол-во раз"))
print(string_info("возвращает кортеж с её длиной"))
print(is_contains('TesT', ['te', 'Test', 'TEST']))
print(is_contains('ror', ['Error', 'Test', 'TEST', 'Ror']))
print(calls)
