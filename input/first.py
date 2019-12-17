# Premier traitement


fullname = input("Quel est votre prénom et nom ?")
print(fullname)

names = fullname.split()
print(names)
print(type(names))

len_listnames = len(names)
print(len_listnames)
if len_listnames == 2:
    print("Prénom " + names[0] + " Nom: " + names[1])
elif len_listnames == 3:
    print(f"Prénom {names[0]}, Milieu {names[1]} Nom {names[2]}")
elif len_listnames == 1:
    print("Nom seul: " + names[0])
else:
    print("Format : Prénom <Milieu> Nom")
    print("Que faire de : " + " ".join(names[3:]))

