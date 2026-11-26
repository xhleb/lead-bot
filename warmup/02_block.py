"""Блок 2: списки, словари, циклы — на заявках.

Те же правила: пишешь тела функций, запускаешь
    python warmup\02_block.py
и добиваешься «Блок 2: всё верно». Проверки внизу не меняй.

Все задачи — про список заявок. Одна заявка выглядит так:
    {"name": "Anna", "phone": "+37120000001", "type": "bot", "urgent": True, "task": "..."}
В завтрашнем боте данные будут ровно такими.
"""


# 7. Найди заявку по телефону. Верни словарь заявки или None, если не нашлась.
#    Цикл + ранний return.
def find_by_phone(leads, phone):
    pass


# 8. Проверь заявку перед сохранением. Верни СПИСОК ошибок (строк).
#    Обязательные поля: "name", "phone", "task".
#    Поле отсутствует ИЛИ пустая строка / одни пробелы -> ошибка "нет поля <имя>".
#    Всё в порядке -> пустой список.
def validate(lead):
    pass


# 9. Сгруппируй имена по типу заявки: {"bot": ["Anna", "Liga"], "parser": ["Ivan"]}.
#    Порядок имён — как в исходном списке.
def group_by_type(leads):
    pass


# 10. Убери дубли по телефону: оставь ПЕРВУЮ заявку с каждым номером, порядок сохрани.
#     Подсказка: множество (set) «уже видел».
def dedupe(leads):
    pass


# 11. Сводка: верни {"total": всего, "urgent": срочных, "types": сколько РАЗНЫХ типов}.
def summary(leads):
    pass


if __name__ == "__main__":
    leads = [
        {"name": "Anna", "phone": "+37120000001", "type": "bot", "urgent": True, "task": "запись"},
        {"name": "Ivan", "phone": "+37120000002", "type": "parser", "urgent": False, "task": "цены"},
        {"name": "Liga", "phone": "+37120000003", "type": "bot", "urgent": True, "task": "заявки"},
        {"name": "Anna", "phone": "+37120000001", "type": "bot", "urgent": False, "task": "повтор"},
    ]

    assert find_by_phone(leads, "+37120000002")["name"] == "Ivan"
    assert find_by_phone(leads, "+37120000001")["task"] == "запись"   # первая, не последняя
    assert find_by_phone(leads, "+37199999999") is None
    assert find_by_phone([], "+37120000001") is None

    assert validate({"name": "Anna", "phone": "+371", "task": "бот"}) == []
    assert validate({"name": "Anna", "task": "бот"}) == ["нет поля phone"]
    assert validate({"name": "   ", "phone": "", "task": "бот"}) == ["нет поля name", "нет поля phone"]
    assert validate({}) == ["нет поля name", "нет поля phone", "нет поля task"]

    assert group_by_type(leads) == {"bot": ["Anna", "Liga", "Anna"], "parser": ["Ivan"]}
    assert group_by_type([]) == {}

    unique = dedupe(leads)
    assert [l["task"] for l in unique] == ["запись", "цены", "заявки"]
    assert dedupe([]) == []

    assert summary(leads) == {"total": 4, "urgent": 2, "types": 2}
    assert summary([]) == {"total": 0, "urgent": 0, "types": 0}

    print("Блок 2: всё верно")
