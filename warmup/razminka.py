

ALLERGENS = ["орех", "мёд", "креветк"]

dish = "Салат с курицей, ОРЕХАМИ и сыром"
##По памяти напиши:
#список ALLERGENS (те же три аллергена);
#has_allergen(dish): есть ли в блюде хоть один аллерген;
#found_allergens(dish): какие именно аллергены нашлись;
#safe_dishes(menu): только безопасные блюда.

#Каждая функция пишется в одну строку после return.

#Если какая-то не вспоминается, сначала напиши её через обычный for (как делал на бумаге), потом сожми в одну строку.
#Сравни свой код с 04_extra.py и напиши мне, где разошлось. Это займёт пару слов.

TYPE_KEYWORDS = { "food" : ["pizza", "burger", "salad"],
                    "drink" : ["coffee", "tea", "juice"] }

task = "Нужен бот, который будет собирать данные о ценах на pizza и coffee"

def classify(task):
    task_l = task.lower()
    for type_name, keywords in TYPE_KEYWORDS.items():
        if any ( word in task_l for word in keywords):
            return type_name
    return "other"