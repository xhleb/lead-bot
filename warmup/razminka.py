

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


def has_allergen(dish) :
    return any(a in dish.lower() for a in ALLERGENS)


def found_allergens(dish):
    return [a for a in ALLERGENS if a in dish.lower()]

def safe_dishes(menu):
    return [dish for dish in menu if not has_allergen(dish)]