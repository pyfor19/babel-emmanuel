"""
 UTILS.PY
 Catalog shared functions
"""
import os
import xlrd
from django.conf import settings


def get_century(year):
    """
    get_century - get century from int year and return int century
    """
    if year > 100:
        century = year % 100
        if century == 0:
            century_birth = year // 100
        else:
            century_birth = year // 100 + 1
    else:
        century_birth = 1
    return century_birth


def xls_reader(modelname, sourcefile):
    """ permet de lire un fichier xls du répertoire /scrap/ grace à l'import xlrd 
        
        input :
        modelname : DeweyTest
        sourcefile : "scrap/La_Dewey_simplifiee.xls"
        
        return: nb of items processed, 0 if none or error
    """
    path = os.path.join(settings.BASE_DIR, sourcefile)

    # ouverture du classeur
    try:
        classeur = xlrd.open_workbook(path)
    except Exception as e:
        print(f"Erreur ouverture {path} : {str(e)}")
        return 0

    # Récupération du nom de toutes les feuilles sous forme de liste
    nom_des_feuilles = classeur.sheet_names()

    # Récupération de la première feuille
    feuille = classeur.sheet_by_name(nom_des_feuilles[0])
    for i in range(0, 109):
        # for j in range(0, 1):
        # print(u"Lecture des cellules:")
        # print("A1: {}".format(feuille.cell_value(i, j)))
        if feuille.cell_value(i, 1):
            item, is_created = modelname.objects.update_or_create(
                number=feuille.cell_value(i, 1), name=feuille.cell_value(i, 2)
            )
            item.save()
            print(
                "{} Number: {}".format(
                    "ADD" if is_created else "UPD", feuille.cell_value(i, 1)
                )
            )
            # elif !(feuille.cell_value(i, 1)) and feuille.cell_value(i, 2):
            # self.name = feuille.cell_value(i, 2)

    rc = i
    return rc
