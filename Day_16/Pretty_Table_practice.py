# Installed prettytable package and trying its features

from prettytable import PrettyTable

T1 = PrettyTable()

T1.field_names = ["Pokemon","Type"]
T1.add_row(["Pikachu","Electric"])
T1.add_row(["Squirtle","Water"])
T1.add_row(["Charmander","Fire"])

#print(T1)

T1.align = "l"

print(T1)