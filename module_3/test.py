def test_send_email(message, recipient, *, sender="university.help@gmail.com"):
    """Задача "Рассылка писем"""
    white_list = ('.com', '.ru', '.net')  # проверить окончание на @/com/ru/net
    at = '@'
    # sender != recipient print("Нельзя отправить письмо самому себе!"
    if recipient.find(at) > 0:  # Если адрес содержит @
        for mail_suff in white_list:  # Если правильный домен
            #print(mail_suff)
            if recipient.find(mail_suff) > 0:
                print("Отправлено", recipient.rfind(mail_suff), mail_suff)
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    return



test_send_email('Test', 'test@mail.ru')
test_send_email('Test', 'testmail.de')
test_send_email('Test', 'testmail.de')
test_send_email('Test', 'testmail.de')



