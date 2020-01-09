"""
 UTILS.PY
 Catalog shared functions
"""


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
