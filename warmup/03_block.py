"""Блок 3: f-строки, сортировка, any/all, dict comprehension.

Запуск:  python warmup\03_block.py   ->  «Блок 3: всё верно».
Проверки внизу не меняй.
"""


# 12. Цена для клиента: пробел между тысячами, 2 знака, знак евро.
#     1234.5 -> "1 234.50 €"      15 -> "15.00 €"
#     Подсказка: f"{x:,.2f}" даёт "1,234.50" — осталось заменить запятую.
def format_price(x):
    
    return f"{x:,.2f}".replace(",", " ") + " €"


# 13. Текст уведомления менеджеру в Telegram (многострочная строка).
#     Срочная заявка — заголовок "🔥 Срочная заявка #<id>", обычная — "Новая заявка #<id>".
#     Дальше строки "Имя: ...", "Телефон: ...", "Задача: ...". Строки разделены "\n".
#     Подсказка: тернарный оператор из шпаргалки (раздел 5) + f-строки.
def notify_text(lead):
    #hot = {"id": 7, "name": "Anna", "phone": "+37120000001", "task": "запись", "urgent": True}
    #cold = {"id": 8, "name": "Ivan", "phone": "+37120000002", "task": "цены", "urgent": False}

    header = f'🔥 Срочная заявка #{str(lead.get("id"))}' if lead.get("urgent") else f'Новая заявка #{str(lead.get("id"))}'
 
    body = f"Имя: {lead.get('name', 'Аноним')}\nТелефон: {lead.get('phone', 'не указан')}\nЗадача: {lead.get('task', 'не указана')}"

    return f"{header}\n{body}"

# 14. Отсортируй заявки: сначала срочные, внутри — по имени по алфавиту.
#     Верни НОВЫЙ список (исходный не меняй).
#     Подсказка: key может вернуть кортеж — сравнение идёт по первому элементу,
#     при равенстве — по второму. И помни: False < True.
def sort_leads(leads):
    
    return sorted(leads, key=lambda o: ( not o.get("urgent"), o.get("name", "")))


# 15. Словарь {имя: телефон} одной строкой — dict comprehension.
def phones_by_name(leads):
    return { lead.get("name"): lead.get("phone") for lead in leads if "name" in lead and "phone" in lead }


# 16. а) У ВСЕХ заявок есть непустой телефон?   б) Есть ХОТЯ БЫ ОДНА срочная?
#     Каждая — одна строка: all(...) / any(...).
def all_have_phone(leads):
    
    return all(lead.get("phone", "").strip() for lead in leads )


def any_urgent(leads):

    return any(lead['urgent'] for lead in leads if 'urgent' in lead )


if __name__ == "__main__":
    assert format_price(1234.5) == "1 234.50 €"
    assert format_price(15) == "15.00 €"
    assert format_price(1000000) == "1 000 000.00 €"

    hot = {"id": 7, "name": "Anna", "phone": "+37120000001", "task": "запись", "urgent": True}
    cold = {"id": 8, "name": "Ivan", "phone": "+37120000002", "task": "цены", "urgent": False}
    assert notify_text(hot) == "🔥 Срочная заявка #7\nИмя: Anna\nТелефон: +37120000001\nЗадача: запись"
    assert notify_text(cold).startswith("Новая заявка #8\n")

    leads = [
        {"name": "Ivan", "phone": "+37120000002", "urgent": False},
        {"name": "Liga", "phone": "+37120000003", "urgent": True},
        {"name": "Anna", "phone": "", "urgent": False},
        {"name": "Boris", "phone": "+37120000004", "urgent": True},
    ]
    original = [l["name"] for l in leads]
    assert [l["name"] for l in sort_leads(leads)] == ["Boris", "Liga", "Anna", "Ivan"]
    assert [l["name"] for l in leads] == original, "исходный список изменился!"

    assert phones_by_name(leads[:2]) == {"Ivan": "+37120000002", "Liga": "+37120000003"}
    assert phones_by_name([]) == {}

    assert all_have_phone(leads) is False          # у Anna пустой телефон
    assert all_have_phone(leads[:2]) is True
    assert any_urgent(leads) is True
    assert any_urgent([leads[0], leads[2]]) is False

    print("Блок 3: всё верно")
    print()
    print(notify_text(hot))   # посмотри, как это будет выглядеть в Telegram
