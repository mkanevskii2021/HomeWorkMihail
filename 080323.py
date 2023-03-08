#
# в listcompare цикл со звездлочками нужно оптимизировать ********
# если мы на шаге нашли общие элементы двух циклов нужно оптмизировать алгоритм и убрать их из дальнейшего рассмотрения


#1 day2/home.py 
#добавить обработку исключений везде где это нужно 
def getDictsByKeyValue(dicts, key, value):
    dictsres = list(filter(lambda dict: dict[key] == value, dicts))
    return dictsres

def getBeastByName(beasts, name):
    return getDictsByKeyValue(beasts,"Имя", name)[0]

def deleteBeastByName(beasts: list, name):
    beasts.remove(getDictsByKeyValue(beasts, "Имя", name)[0])
    
def addSerie(beasts, name, serie):
    getDictsByKeyValue(beasts, "Имя", name)[0]["Серии"].append(serie)
    
def delSerie(beasts, name, serie):
    getDictsByKeyValue(beasts, "Имя", name)[0]["Серии"].remove(serie)


lp = "Любимая фраза"
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
beasts2 = beasts.copy()

getBeastByName(beasts,"Лосяш")[lp] = "Святые угодники!"
getBeastByName(beasts,"Копатыч")[lp] = "Тысяча чертей!"
#deleteBeastByName(beasts, "Копатыч")


try:
    print(beasts)
    
except NameError:
     print("try again")
    
finally:
    print ("Смешарики  - мультик о сказачных животных")

#3 понять полностью day2 listcompare.py

#4 сделайте функцию которая из списка словарей отбирает словари в которых в заданных ключах значения равны заданым 
#например (имя = (Копатыч или Лосяш)) циклов нельзя и таких ключей может быть несколько

d1 = {"Имя": "Лосяш",
    "Цвет": "Шафрановый",
    "Серии": ["Герой Плутона", "Бабочка", "Долгая рыбалка"]}

d2 = {"Имя": "Копатыч",
    "Цвет": "Коричневый",
    "Серии": ["Долгая рыбалка", "Кулинария", "Танцор Диско"]}

s1 = set(d1["Серии"])
s2 = set(d2["Серии"])

print(list( s1 & s2))





#2 сделайте так чтобы список зверей читался из файла
import json


with open('clock.json') as file_object:
   contents = file_object.read()
   print(contents)
    