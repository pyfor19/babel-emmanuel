from second import validate_display, validate, validate_string
from second import F_ERROR

print("THIRD")

d = validate("Emmanuel    G    Sandorfi")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)

"""
print("-" * 50)
d = validate("")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)

print("-" * 50)
d = validate("Emma23 Sandorfi")
if F_ERROR in d:
    print(d[F_ERROR])
print(d)



d = validate("18")
print(d)
validate_display("Albert Einstein")

print(re.match("^[A-Za-z]+$", "Emmm34 9080 NUEL"))
print(re.match("^[A-Za-z]+$", "Emmm12"))
exit(0)
"""
