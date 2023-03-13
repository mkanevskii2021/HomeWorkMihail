from functools import reduce

"""
li  = 'persons_data_new.txt'
with open('persons_data_new.txt') as file_object:
    contents = file_object.read()
print(contents)

red = reduce(lambda x,y: x+y, li)
print(red)



#multiply = lambda x,y: x * y
#print(multiply(21, 2))

#mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
#zolushka = list(filter(lambda x: x == 'мак', mixed))
 
#print (zolushka)

li = [9,2,3,4,5,6,7,8,9,10]

# reduce 
# на каждом шаге!!!
# применяем функцию с двумя параметрами  один текущий элемент второй результат предыдущего reduce
# 1 - iter R = 1     -- x + y всегда первый это уже результат
# 2 - iter x = 1 y = 2 R = 3
# 3 - iter x = 3 y = 3 R = 6
# 4 - iter x = 6 y = 4 R = 10
# 5 - iter x = 10 y = 5 R = 15

r = li[0]
print(
    f"шаг 1 предыдущий результат {r} текущий элемент {r} результат операции {r}")
for i in range(1, len(li)):
    r = r + li[i]
    print(f"шаг {i+1} предыдущий результат {r - li[i]} текущий элемент {li[i]} результат операции {r}")
print(r)

red = reduce(lambda x,y: x+y, li)
print(red)

"""


with open('advs.txt') as file_object:
    S = file_object.read()
print(S)

L = S.split()
U = set(L)
M = {}
for word in U:
    M[word] = L.count(word)

print (M)
print (len(U))
