AB = []


def add_abit():
    print("+ Новий абітурієнт: ")
    name = input("\tФІО: ")
    gender = input("\tСтать: ")
    spec = input("\tСпеціальність: ")
    print("\tРезультати вступних іспитів (3 предмета): ")
    exam = [input("\t\tПерший предмет: "), input("\t\tДругий предмет: "), input("\t\tТретій предмет: ")]

    AB.append({
        'NAME': name,
        'GENDER': gender,
        'SPEC': spec,
        'EXAM': exam
    })

    question()


def view_abit(ab=None):
    quantity = 0
    number = 1

    average_grade = int(input("Введіть бажаний середній бал за яким будуть відсортовані абітурієнти: "))

    for abit in ab:
        grades = 0
        for grade in abit['EXAM']:
            grades += int(grade)

        average = grades / 3

        if average <= average_grade:
            quantity += 1

    if quantity == 0:
        print(f"\nАбітурієнтів в яких середній бал нижче ніж {average_grade} НЕ ЗНАЙДЕНО!")
        question()
    else:
        print(f"\nЗнайдено {quantity} абітурієнтів в яких середній бал нижче ніж {average_grade}.\n")

    for abit in ab:
        grades = 0
        for grade in abit['EXAM']:
            grades += int(grade)

        average = grades / 3

        if average <= average_grade:
            print(f"Абітурієнт номер {number}: ")

            print(f"\tФІО: \t\t{abit['NAME']}")
            print(f"\tСтать: \t\t{abit['GENDER']}")
            print(f"\tСпеціальність: \t{abit['SPEC']}")
            print(f"\tІспити: \t{', '.join(abit['EXAM'])} (Середній бал: {'%.1f' % average})\n")

            number += 1

    input()
    question()


def question():
    command = input("Щоб додати абітурієнта - натисніть на 'Enter' / Щоб вивести на екран всіх абітурієнтів напишіть 'V': ")
    if command == 'V':
        stop = False
        view_abit(AB)
        return stop
    else:
        add_abit()


if input("Щоб додати нового абітурієнта - натисніть на 'Enter'") == '':
    add_abit()


input()
