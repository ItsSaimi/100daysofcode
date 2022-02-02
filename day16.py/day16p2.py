from prettytable import PrettyTable
table = PrettyTable()
# print(table)
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align= "l"
print(table)