def send_email(message, recipient, sender="university.help@gmail.com"):
    """Функция принимает имитирует работу почтового клиента с опциями изменения адреса отправителя"""
    white_list = ('.com', '.ru', '.net')  #  Список разрешенных доменов
    if recipient.endswith(white_list):  #  '.com', '.ru', '.net' - принимает кортеж, проверка окончания
        mail_suff = True
        print('not valid', mail_suff)
    else:
        mail_suff = False
        #  Проверка всех условий корректности адреса
    if "@" not in recipient or "@" not in sender or (
            sender == "university.help@gmail.com" and recipient == sender) or mail_suff == False:
        if "@" not in recipient or "@" not in sender or mail_suff == False:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        elif sender == "university.help@gmail.com" and recipient == sender:
            print("Нельзя отправить письмо самому себе!")
    else:
        if sender == "university.help@gmail.com":
            #print(f"{message} Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
        else:
            #print(f"{message} НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('test', 'test@mail.ru')
send_email('test', 'testmail.ru')
send_email('test', 'test@mail.de')
send_email('test', 'test@mail.гы')
send_email('test', 'test@mail.ru', 'test-univesity@mail.com')
