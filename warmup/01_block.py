"""Блок 1: функции и return.

Правила:
- Пиши тело функций вместо `pass`. Функции ВОЗВРАЩАЮТ результат (return), а не печатают.
- Запусти:  python warmup\01_block.py
- Если в консоли «Блок 1: всё верно» — готово. Если AssertionError — смотри,
  на какой строке упало, и чини.
- Сами проверки (assert внизу) не меняй.
"""


# 1. Верни True, если n чётное, иначе False.
#    Подвох: можно уложиться в одну строку без if.
def is_even(n):
    return n % 2 == 0  # Альтернатива в одну строку


# 2. Очисти телефон: убери пробелы, дефисы и скобки.
#    "+371 (20) 123-456"  ->  "+37120123456"
def clean_phone(phone):
    return phone.replace(" ", "").replace("-", "").replace("(", "").replace(")","")


# 3. Заявка — это словарь. Верни строку "Имя: задача".
#    Если ключа "name" нет — вместо имени "Аноним".
#    Подсказка: в шпаргалке, раздел 4.
def format_lead(lead):
    return f"{lead.get('name', 'Аноним')}: {lead.get('task', '')}"


# 4. Посчитай слова в тексте: верни словарь {слово: сколько раз}.
#    Регистр не важен: "Бот" и "бот" — одно слово.
#    "Нужен бот бот для записи Бот" -> {"нужен": 1, "бот": 3, "для": 1, "записи": 1}
def count_words(text):
    word_count = {}
    for i in text.lower().split():
        word_count[i] = word_count.get( i, 0) + 1
    return word_count


# 5. Дан список заявок. Верни список ИМЁН только срочных заявок (urgent == True).
#    Одной строкой — через comprehension.
def urgent_names(leads):
    return [lead["name"] for lead in leads if lead.get("urgent") == True]


# Бонус (необязательно): перепиши задачу 4 из диагностики без += и среза —
# через ", ".join(...) и comprehension. Одна строка.
def numbered(words):
    return ", ".join(f"{i}. {word}" for i, word in enumerate(words, start=1))


if __name__ == "__main__":
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True

    assert clean_phone("+371 (20) 123-456") == "+37120123456"
    assert clean_phone("20000000") == "20000000"

    assert format_lead({"name": "Anna", "task": "бот для записи"}) == "Anna: бот для записи"
    assert format_lead({"task": "парсер цен"}) == "Аноним: парсер цен"

    assert count_words("Нужен бот бот для записи Бот") == {"нужен": 1, "бот": 3, "для": 1, "записи": 1}
    assert count_words("") == {}

    leads = [
        {"name": "Anna", "urgent": True},
        {"name": "Ivan", "urgent": False},
        {"name": "Liga", "urgent": True},
    ]
    assert urgent_names(leads) == ["Anna", "Liga"]
    assert urgent_names([]) == []

    print("Блок 1: всё верно")

    if numbered(["bot", "api", "sql"]) is not None:
        assert numbered(["bot", "api", "sql"]) == "1. bot, 2. api, 3. sql"
        print("Бонус: верно")
