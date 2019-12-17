""" 
SETUP v0.1
Programme qui affiche le setup de la machine python 
Changelog : 
- dec 19 : initiatiliation 
"""

import sys
import os
import datetime


def printseparator():
    """ fonction qui affiche une ligne de séparation """
    print("-" * 50)


# import requests

a = "Bonjour Monde !"
print(a)  # j'affiche l'objet #

printseparator()
print(sys.executable)
print(sys.platform)
print(sys.path)

print(sys.version_info)
v = sys.version_info
# print(type(v))  # type de sys
# print(dir(v))   # introspection de sys

print(f"Python version {v.major}.{v.minor}.{v.micro}")
# print("Python version {}.{}.{}".format(v.major, v.minor, v.micro))

# print("Python version %s.%s.%s" % (v.major, v.minor, v.micro))  # Version 2.7, deprécié
print("Environnement PythonPath : " + os.getenv("PYTHONPATH", "Vide"))

printseparator()
print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
print(f"Date et Heure {dt} - Année {dt.year}")

printseparator()

help(printseparator)
