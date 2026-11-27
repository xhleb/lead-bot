"""Доп. задачи к 19: тот же приём на другом примере.

Запуск:  python warmup\04_extra.py   ->  «19.1–19.2: всё верно».
Проверки внизу не меняй.
"""

ALLERGENS = ["орех", "мёд", "креветк"]


# 19.1 Есть ли в описании блюда хоть один аллерген? Регистр не важен.
#      Одна строка: any(...).
def has_allergen(dish):
    return any(allergen in dish.lower() for allergen in ALLERGENS)


# 19.2 А КАКИЕ именно аллергены нашлись? Верни список (в порядке ALLERGENS).
#      Одна строка: comprehension с фильтром — шпаргалка, раздел 7, строка 3.
#      Подумай: что теперь слева (что кладём в результат), а что в if?
def found_allergens(dish):
    return [a for a in ALLERGENS if a in dish.lower()]


# 19.3 (последняя) Дано меню — список описаний блюд. Верни только БЕЗОПАСНЫЕ блюда.
#      Одна строка: comprehension с фильтром.
#      Фишка: внутри можно вызвать свою же функцию из 19.1 — не пиши проверку заново.
def safe_dishes(menu):
    pass


if __name__ == "__main__":
    assert has_allergen("Салат с курицей, ОРЕХАМИ и сыром") is True
    assert has_allergen("Суп томатный") is False
    assert has_allergen("") is False

    assert found_allergens("Креветки в соусе с орехом") == ["орех", "креветк"]
    assert found_allergens("Блины с мёдом") == ["мёд"]
    assert found_allergens("Суп томатный") == []

    print("19.1–19.2: всё верно")

    menu = ["Суп томатный", "Салат с орехами", "Блины с мёдом", "Паста карбонара"]
    if safe_dishes(menu) is not None:
        assert safe_dishes(menu) == ["Суп томатный", "Паста карбонара"]
        assert safe_dishes([]) == []
        print("19.3: всё верно")
