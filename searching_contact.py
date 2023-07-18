from user import fill_person


def searching_contact():
    search = input('Введите фамилию контакта для поиска: ').title()
    for name, surname, second_name, number in fill_person():
        if search == surname:
            print(surname, name, second_name, number)
            break
        else:
            print('Такого контакта не существует')
            break
