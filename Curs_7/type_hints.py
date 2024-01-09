def salut(nume: str) -> str:
    return 1
    return f"Salut {nume}"
# 
# @param nume: str
#
def salut_1(nume):
    if not isinstance(nume, str):
        raise ValueError()
    return 1

print(salut("Georgel"))
print(salut(1))