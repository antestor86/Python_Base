# validate_registrations.py
# -*- coding: utf-8 -*-

from typing import Tuple

ERROR_TEXT = {
    IndexError: 'НЕ присутствуют все три поля',
    NameError: 'Поле «Имя» содержит НЕ только буквы',
    SyntaxError: 'Поле «Имейл» НЕ содержит @ и точку',
    ValueError: 'Поле «Возраст» НЕ представляет число от 10 до 99',
}

SEPARATOR = '        '  # восемь пробелов как в примере


def validate_record(line: str) -> Tuple[str, str, int]:
    """
    Проверяет одну строку данных. При нарушении правил
    выбрасывает исключения строго по заданию.
    Возвращает кортеж (name, email, age) при успехе.
    """
    parts = line.split()

    # 1) Присутствуют все три поля (ровно три токена)
    if len(parts) != 3:
        raise IndexError

    name, email, age_str = parts

    # 2) Имя содержит только буквы (включая кириллицу)
    if not name.isalpha():
        raise NameError

    # 3) E-mail содержит и '@', и '.'
    if '@' not in email or '.' not in email:
        raise SyntaxError

    # 4) Возраст — число от 10 до 99
    if not age_str.isdigit():
        raise ValueError
    age = int(age_str)
    if not (10 <= age <= 99):
        raise ValueError

    return name, email, age


def main():
    src = 'registrations.txt'
    good_log = 'registrations_good.log'
    bad_log = 'registrations_bad.log'

    try:
        with open(src, 'r', encoding='utf-8') as fin, \
             open(good_log, 'w', encoding='utf-8') as fgood, \
             open(bad_log, 'w', encoding='utf-8') as fbad:

            for line in fin:
                # сохраняем исходную строку без завершающего \n, но со всеми пробелами
                raw = line.rstrip('\n')

                try:
                    validate_record(raw)
                except Exception as e:
                    # маппинг типа исключения -> текст ошибки по условию
                    msg = ERROR_TEXT.get(type(e), f'Непредвиденная ошибка: {type(e).__name__}')
                    # строка + пробелы + текст ошибки
                    fbad.write(f'{raw}{SEPARATOR}{msg}\n')
                else:
                    # корректные данные пишем "как есть"
                    fgood.write(raw + '\n')

    except FileNotFoundError:
        # Можно заменить на логирование/print при желании.
        raise FileNotFoundError(
            f'Файл {src!r} не найден. Поместите registrations.txt рядом со скриптом.'
        )


if __name__ == '__main__':
    main()
