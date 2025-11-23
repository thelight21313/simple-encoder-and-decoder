import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
slovo = input("Enter a text: ")
character = list(slovo)
bob = []
normspisok = []
for i in range(len(character)):
    if character[i] != " ":
        normspisok.append(character[i])
for i in range(len(normspisok)):
    bob.append(normspisok[i])
    for i in range(5):
        bob.append(random.choice(alphabet))
for i in range(len(bob)):
    print(bob[i], end="")