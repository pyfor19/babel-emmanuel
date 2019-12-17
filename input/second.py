# Second traitement

# INPUT
# VALIDATION
# AFFICHAGE

import re


def manage_input():
    in_fullname = input("Quel est votre prénom et nom ?")
    print(in_fullname)
    d = validate(in_fullname)
    print(d)


F_FIRST = "firstname"
F_LAST = "lastname"
F_MIDDLE = "middlename"
F_FULL = "fullname"
F_ERROR = "error"


def validate_string(input):
    """ si la string input contient juste des caractères A-Z,
        renvoie True, sinon False
    """
    # si vide
    # enleve les espaces
    # regarde si AZ ou az
    print(input)
    if not len(input):
        return False
    r = re.match("^[A-Za-z]+$", input)
    print(r)
    return True if r else False


def validate(fullname):
    """ validation et affichage d'une string 
        selon format Prénom <Milieu> Nom 
    """
    names = fullname.split()
    len_listnames = len(names)
    # vérifier que chaque str de names ne comporte que des lettres de l'aphabert
    type(names)
    print(len_listnames)
    for n in names:
        # n = n.strip()  # enlève les espaces devant, derrière
        if not validate_string(n):
            # return error
            return {F_ERROR: "Erreur de validation sur " + n}

    d = {}
    if len_listnames == 2:
        d[F_FIRST] = names[0]
        d[F_LAST] = names[1]
    elif len_listnames == 3:
        d[F_FIRST] = names[0]
        d[F_MIDDLE] = names[1]
        d[F_LAST] = names[2]
    elif len_listnames == 1:
        d[F_LAST] = names[0]
    else:
        error = "Format : Prénom <Milieu> Nom\n"
        if len_listnames == 0:
            error += "Valeur manquante"
        else:
            error += "Que faire de : " + " ".join(names[3:])
        d[F_ERROR] = error
    return d


def validate_display(fullname):
    """ validation et affichage d'une string 
        selon format Prénom <Milieu> Nom 
    """
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


if __name__ == "__main__":
    manage_input()
