# нельзя использовать циклы и условия
# Добавление любимых фраз Копатыча и Лосяша
# addPhrase(beasts, "Лосяш", "Хрю")
# print(beasts)
# Поиск серий, в которых участвуют оба персонажа
# allSeries(beasts)
# print(seriesSets(beasts))
# Удаление серии Герой Плутона из списка серий Лосяша
# l = getBeast(beasts,'Лосяш')
# l['Серии'].remove('Герой Плутона')
# print(l)
# seriesRemove(beasts, 'Лосяш', 'Герой Плутона')
# print(getBeast(beasts,'Лосяш'))
# Замена цвета Копатыча на Светло-коричневый
# l = getBeast(beasts,'Копатыч')
# l['Цвет'] = "Светло-коричневый"
# print(l)
# changeColor(beasts,"Копатыч","Светло-коричневый")
# print(getBeast(beasts,'Копатыч'))
# Добавление данных о любом другом смешарике пользователем
# addBeast(beasts)
# print(beasts)
# Подсчет количества записанных смешариков
# ???
# Создание второй структуры, идентичной первой, удаление оттуда записи про Копатыча так чтобы оригинальная структура не поменялась
# Создавайте )
# deleteBeast(omg,'Копатыч')



beasts = list()

beasts.append({
    "Имя": "Лосяш",
    "Цвет": "Шафрановый",
    "Серии": ["Герой Плутона", "Бабочка", "Долгая рыбалка"]
})

beasts.append({
    "Имя": "Копатыч",
    "Цвет": "Коричневый",
    "Серии": ["Долгая рыбалка", "Кулинария", "Танцор Диско"]
})

beasts.append({
    "Имя": "Хрю",
    "Цвет": "Красный",
})

print (beasts)


def getBeastByName(beasts, name):
    beast = list(filter(lambda beast: beast["Имя"] == name, beasts))[0]
    return beast

print(getBeastByName(beasts,"Хрю"))

beasts.append({"Fraza": "JJJJJJJJJJ"})
print (beasts)









