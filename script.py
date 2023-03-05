"""
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

a = True
b = False
print (a != b)
"""

a = True
b = False
f = 1
if (f):
    print (True)
    
l = [1,2,3,4,5,6]

l = []
n = 1
while n < 12:
    l.append(n)
    n = n+1
print (l)

l = []
for i in range (1,27):
    if not i%2: # 0 если кратно 2
        l.append(i)
print (l)

l = [x for x in range (1,11)]
l =[]
l = [x for x in range (1,11) if x%2]
print (l)

l = [x for x in range (1,11)]
l =[]
l = [x for x in range (1,11) if not x%2]
print (l)

l = [x for x in range (1,101) if not x%2 and x%3 and not x%5]
# четное число и одновременно не делится на три и одновременно делится на 5
print (l)

# and or
a = True
b = False
c = True

print (a and b) # False
print (a and c) # True
print (a or b) # True
print ((a and c) or b) # True
print (a or b or c) # True
print (a and b and c) # False


w = "miChael jAckson"
print (w.title()) # Michael Jackson
print(w.upper()) # MICHAEL JACKSON
print(w.lower()) # michael jackson

for c in w.lower():
    print (c)
print (len (w))

w = list(w.lower())
print (w)
w[4] = "c"
w = "".join(w) # (x for x in w)
print (w)


w = "miChae2321l jA3434cks4on"
print (w.title()) # Michael Jackson
print(w.upper()) # MICHAEL JACKSON
print(w.lower()) # michael jackson

for c in w.lower():
    print (c)
print (len (w))

w = list(w.lower())
print (w)
w = "".join(x for x in w if x.isalpha() or x == " ") # (x for x in w)
print (w)
print (w.title())

# строки посмотреть
"зима 32нео крестьянин торжествуя на 42на на"

# split




"""
l = []
for word in phraza:
    good = True
    for letter in word:
        if not letter.isalpha():
            good = False
    if good:
        l.append(word)    

         
    
"""

w = "зима 32нео крестьянин торжествуя на 42на на"
a = (w.split())
print (type(a))
print (a[0], a[2], a[3], a[4], a[6])


fraza = "зима 32нео крестьянин торжествуя на 42на на"
w = (fraza.split())
w = " ".join(x for x in w if x.isalpha() or x == " ") 
print (type(w))
print (w)