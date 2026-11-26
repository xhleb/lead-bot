

#x = [1,2,3]; y = x; y.append(4); print(len(x)). Что выведет и почему? Ответ — комментарием.
#  выведет 4 потому что мы с конца списка добавляем 4, а y ссылается на тот же объект что и x.

#Функция is_even(n) возвращает True или False.
# if even - true, if not - false

#d = {"name": "Anna", "age": 20}. а) f-строкой вывести Anna, 20 лет; б) добавить "city": "Riga".


def anna_info():
    d = {"name": "Anna", "age": 20}
    d["city"] = "Riga"
    print(f"{d['name']}, {d['age']} years old, lives in {d['city']}.")

#words = ["bot", "api", "sql"] вывести как 1. bot, 2. api, 3. sql.
def print_words():
    words = ["bot", "api", "sql"]
    final_sentence = ""
    for i, word in enumerate(words, start=1):
        
        final_sentence += f"{i}. {word}, "
    print(final_sentence[:-2])  # Убираем последнюю запятую и пробел

#Одной строкой: квадраты чётных от 1 до 10, ответ [4, 16, 36, 64, 100].
def even_squares():
    print([n**2 for n in range(1, 11) if n % 2 == 0])

#print("5" + 3): что будет? Как получить 8, а как "53"? Ответ — комментарием.
# будет ошибка изза разносчти типов. Чтобы получить 8 нужно сделать int("5") + 3, а чтобы получить "53" нужно сделать "5" + str(3).


if __name__ == "__main__":
    anna_info()
    print_words()
    even_squares()
