from year import validate_year

"""
x = validate_year(1950)
print(f"retour {x} type {type(x)}")

x = validate_year("1950")
print(f"retour {x} type {type(x)}")

x = validate_year("1950xy")
print(f"retour {x} type {type(x)}")
"""

import unittest


class ValidateYearTestCase(unittest.TestCase):
    def test_validate_year(self):
        y = validate_year("13")
        self.assertEqual(y, 2013)
        y = validate_year(13)
        self.assertEqual(y, 2013)
        y = validate_year("80")
        self.assertEqual(y, 1980)
        y = validate_year("1651")
        self.assertEqual(y, 1651)


if __name__ == "__main__":
    unittest.main()
