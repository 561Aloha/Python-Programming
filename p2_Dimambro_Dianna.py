"""a) Write a list comprehension for tuples with distinct integers satisfying a mathematical condition.
b) Write list comprehensions for manipulating strings in a given list.
c) Write a list comprehension for formatting full names.
d) Write a list comprehension for finding anagrams.
e) Write a dictionary comprehension for mapping strings to their lengths.
f) Write a dictionary comprehension for mapping vowels to their positions in a text."""


#a)
result = [(a, b, c, d) 
for a in range(1, 11) 
for b in range(1, 11) 
for c in range(1, 11) 
for d in range(1, 11) 
if a != b and a != c 
and a != d and b != c 
and b != d and c != d 
and a**2 + b**2 == c**2 + d**2]

for tuple in result:
    print(tuple)

print()

#problem b
original_list = ['One', 'SEVEN', 'three', 'two', 'Ten']
partb = [(s.lower(), len(s)) for s in original_list if len(s) < 5]
print(partb)
print()
    


#problem c
names = ['Christopher Ashton Kutcher', 'Elizabeth Stamatina Fey']
partc = [f"{first} {middle[0]}. {last}" 
    for i in names
    for first, middle, last in [i.split()]]
print(partc)


#Problem d
list1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
list2 = ["Bowels", "Sample", "Altars", "Stop", "Course", "Smart"]

partd = [(w1, w2) 
    for w1 in list1 
    for w2 in list2 
    if sorted(w1.lower()) == sorted(w2.lower())]

print()
print(partd)



#Problem e
s = ['one', 'two', 'three']#keys
parte = {word: len(word) 
    for word in s}
print()
print(parte)
print(s)
print()

#problem f
text = {i: c.lower().strip() for i, c in enumerate("Hello world")}
vowels = "aeiou"
partf= {k: v for k, v in text.items() if v and v in vowels}
print("answer f:", partf)

