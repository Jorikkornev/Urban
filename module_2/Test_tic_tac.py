#  Глобальные переменные
errors = {"is_err": False, "err_text": "", "input_text": "Введите два числа через пробел: ", "err_pos": 0}


# TODO Разобраться в необходимости наличия errors, если исправлять ошибки в функции
# TODO Сделать одну большую функцию проверки на ошибки?
# TODO Добавить имя функции в errors?

# Проверка на 2 значения, если 3 - возвращает 2, если 1 - просит ввести ещё одно
def is_count(sings, errs):
    # Выполняется если флаг ошибки False
    if len(sings) == 2:
        errs["is_err"] = False
        return *sings, *errs
    elif len(sings) > 2:
        sings = sings[0:1]
        return sings
    else:
        errs["err_text"] = "Введите ещё одно число "
        errs["is_err"] = True
        errs["err_pos"] = 1
        print("count error")
        return *sings, *errs


# Проверка на int
def is_int(sings, errs):
    # Выполняется если флаг ошибки False
    if not errs["is_err"]:
        for t in sings:
            # У int нет isnumeric, continue
            if type(t) is int:
                continue
            # Если переводится из строки в число
            elif t.isnumeric():
                int(t)
                errs["is_err"] = False
            # Заполнение "errors, если не число
            else:
                errs["err_text"] = f"{t} - не число, повторите ввод "
                errs["err_pos"] = sings.index(t)
                errs["is_err"] = True
                return *sings, *errs
        return sings


"""
def check_data(errs):
    # Переменные
    # Ввод двух чисел через пробел/запятую
        if errs["is_err"] is False:
            nums = input(errors["input_text"])
            # Разбивка строки на list
            nums = nums.split()
            # Функции проверки
            is_int(nums, errs)
            print("If вышел ", nums)
            
        #  Возвращает флаг проверки и результат в переменные строки и ряда
        if errs["is_err"] is True:
            print(errs)
            return errs
        else:
            return nums
"""
# Ввод значений
nums = input(errors["input_text"])
nums = nums.split()
# Функция проверки
is_count(nums, errors)
is_int(nums, errors)
if errors["is_err"] is False:
    print(nums)
    print("Вышли")
else:
    while errors["is_err"] is True:
        # Рекурсия
        # Исправление ошибок при проверке - в функции проверки на ошибку!
        nums.insert(errors["err_pos"], input(errors["err_text"]))  # Для is_count
        nums[errors["err_pos"]] = input(errors["err_text"])  # Для is_num
        is_count(nums, errors)
        is_int(nums, errors)
        print("else: ", nums, errors)
